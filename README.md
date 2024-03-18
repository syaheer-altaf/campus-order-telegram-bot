# Campus Orders Telegram Bot

## About

Not long ago, I created a Telegram bot designed to streamline the order-taking process for food delivery within campus boundaries. Utilizing Google Sheets API as the backbone for our database, this setup allows for an efficient and organized way to handle customer orders. The entire structure of this codebase has been made freely available, aiming to aid others in deploying similar solutions in their environments.

## Getting Started

Follow these step-by-step instructions to set up your own order-taking Telegram bot using Python and Google Sheets API.

### Prerequisites

Ensure you have Python installed on your system. This project requires Python 3.x.

### Installation

1. **Install necessary Python modules**

   To interact with the Telegram Bot API and Google Sheets, you'll need to install a couple of Python libraries. Open your terminal or command prompt and execute the following commands:

   - For Telegram Bot API:

     ```
     pip install python-telegram-bot
     ```

   - For Google Sheets and Google Auth libraries:

     ```
     pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
     ```

2. **Create your Telegram Bot**

   - Use BotFather on Telegram to create your own bot. Follow the instructions provided by BotFather to get your API token.
   - Place your API token in the `api.py` file. Remember, it's crucial not to share your API token with others.
   - For detailed instructions on creating a Telegram bot, visit [this guide](https://flowxo.com/how-to-create-a-bot-for-telegram-short-and-simple-guide-for-beginners/).

3. **Set up Google Workspace API**

   - Enable Google Sheets API and generate OAuth credentials as per the instructions found [here](https://developers.google.com/sheets/api/quickstart/python).
   - Rename the generated JSON file to `credentials.json` and place it in the `_sheets` directory.

4. **Configure Google Spreadsheet**

   - Create a new Google Spreadsheet and note its ID from the URL: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`.
   - Enter the spreadsheet ID in `/_sheets/sheets.py` in the designated variable. Upon the first run, a `token.json` file will be automatically created for authentication purposes.

5. **Customize and Run**

   - Modify the code in `main.py`, `data_list.py`, `texts.py`, and `pricing.py` according to your specific needs.
   - Execute `python3 main.py` to start the server on your desktop and begin processing orders through your Telegram bot.

## Usage

Once everything is set up, your Telegram bot is ready to take orders. Users can interact with the bot to place their orders, which will then be organized and stored in the designated Google Sheets document, accessible campus-wide.

## Contributing

Feel free to fork this project and contribute to expanding its capabilities. Your contributions towards making this project more efficient and adaptable are highly appreciated.

## License

This project is free to use and does not require licensing.

Enjoy building your own Telegram Bot!