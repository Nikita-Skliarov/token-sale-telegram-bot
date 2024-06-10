# Telegram Bot for Token Sales

This README provides an overview of the Telegram bot designed to facilitate token sales. The bot allows users to place orders, verifies subscriptions in a list of channels, and more.

## Features

- **Subscription Verification:** The bot checks if users are subscribed to a list of channels before processing their orders.
- **Token Sale Updates:** Users receive real-time updates on token sales and related information.

## Installation

To install and run the Telegram bot, follow these steps:

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/yourusername/telegram-token-sale-bot.git
    cd telegram-token-sale-bot
    ```

2. **Install Dependencies:**
    ```sh
    pip install python-telegram-bot
    ```

3. **Set Up Environment Variables:**
    - Create a `.env` file in the project root directory.
    - Add the necessary environment variables such as API keys and channel lists (see [Tutorial: Creating a Telegram Bot](#tutorial-creating-a-telegram-bot)).

4. **Run the Bot:**
    ```sh
    python main.py
    ```

## Usage

1. **Start a Conversation:** Start a conversation with the bot on Telegram.
2. **Fill Out the Order Form:** Follow the prompts to fill out the order form.
3. **Subscription Verification:** The bot will verify your subscriptions and process the order accordingly.

## License

This project is licensed under the [MIT License](LICENSE).

---

## Tutorial: Creating a Telegram Bot

To create a Telegram bot, follow these steps:

1. **Contact BotFather:**
    - Open Telegram and search for `BotFather`.
    - Start a chat with `BotFather` and follow the instructions to create a new bot.
    - Save the API token provided by `BotFather`.

2. **Set Up Environment Variables:**
    - Create a `.env` file in the root of your project.
    - Add the following lines, replacing the placeholders with your actual values:
        ```env
        TELEGRAM_API_KEY=your_telegram_api_key
        CHANNEL_LIST=channel1,channel2,channel3
        ```

3. **Update Bot Configuration:**
    - Open `config.py` (or the relevant configuration file in your project).
    - Ensure the environment variables are loaded correctly, for example:
        ```python
        import os
        from dotenv import load_dotenv

        load_dotenv()

        TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
        CHANNEL_LIST = os.getenv('CHANNEL_LIST').split(',')
        ```

---

Feel free to contribute to this project by submitting issues or pull requests. Happy coding!
