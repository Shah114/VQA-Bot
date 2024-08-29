# VQA-Bot
This repository contains a Visual Question Answering (VQA) ChatBot that leverages the Gemini API and a Telegram bot for interaction. The bot also includes translation capabilities, allowing it to translate questions and answers between English and Azerbaijani. <br/>
<br/>

## Features
* Visual Question Answering: Users can send an image and ask questions related to the content of the image. The bot processes the image and provides relevant answers.
* Google Generative AI Integration: Enhances the bot's ability to generate more accurate and context-aware responses.
* Gemini API Integration: Utilizes the Gemini API for handling image-related queries.
* Telegram Bot Integration: Connects with Telegram via the Telegram bot token, allowing users to interact with the bot through the Telegram app.
* Translation Support: Incorporates the EasyGoogleTranslate module to translate text between English and Azerbaijani.
* Configuration Management: A config.py file is used to securely manage the Gemini API key and Telegram bot token.
* Requirements: A requirements.txt file is provided to easily install all necessary Python libraries. <br/>
<br/>

## Installation
1. Clone the Repository
   ```bash
   git clone https://github.com/Shah114/vqa-chatbot.git
   cd vqa-chatbot
   ```
2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Setup Configuration <br/>
   Create a config.py file in the root directory and add your Gemini API key and Telegram bot token.
   ```python
   # config.py
   api_key = 'your_gemini_api_key'
   bot_token = 'your_telegram_bot_token'
   ```
4. Run the Bot
   ```bash
   python main.py
   ```
<br/>

## Usage
* Interacting with the Bot: After running the bot, you can interact with it through your Telegram app by sending images and asking related questions.
* Translation: The bot can translate questions and answers between English and Azerbaijani, enhancing communication for users who prefer either language. <br/>
<br/>

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
