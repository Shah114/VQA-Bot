# Importing Modules
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes,
    filters, MessageHandler, ConversationHandler)
from io import BytesIO
from PIL import Image
import config
import google.generativeai as genai
from easygoogletranslate import EasyGoogleTranslate

# Assigning API key and token
genai.configure(api_key=config.api_key)

application = ApplicationBuilder().token(config.bot_token).build()

asking_image, asking_question = 0, 1

# Translate to English
translator_to_en = EasyGoogleTranslate(
    source_language='az',
    target_language='en',
    timeout=10)

# Translate to Azerbaijani
translator_to_az = EasyGoogleTranslate(
    source_language='en',
    target_language='az',
    timeout=10)

# Defining Bot Functions
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am Murtuza! Please, type something so I can respond!')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Welcome to VQA Bot! Upload an image with text prompt and ask what you want...')
    return asking_image

async def get_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo # if not == ()
    context.user_data['image'] = photo

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Great! Now, what is your question?')
    return asking_question

async def vqa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text # is not == None
    photo = context.user_data['image']

    if text and photo:
        photo_id = photo[-1].file_id # photo_id = 123243434454
        photo_file = await context.bot.get_file(photo_id)

        stream = BytesIO()
        await photo_file.download_to_memory(out=stream)

        stream.seek(0)

        image = Image.open(stream).convert('RGB')
        question = text

        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        result = model.generate_content([question, image])

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=result.text)

    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='No photo or prompt provided.')

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Conversation canceled.')
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Main Part
if __name__ == "__main__":
    print('Starting bot...')
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            asking_image: [MessageHandler(filters.PHOTO & (~filters.COMMAND), get_image)],
            asking_question: [MessageHandler(filters.TEXT & (~filters.COMMAND), vqa)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    application.add_handler(conversation_handler)
    application.add_handler(CommandHandler('help', help_command))
    
    # Errors
    application.add_error_handler(error)

    print('Polling...')
    application.run_polling()