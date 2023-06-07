import yaml
import os


def get_telegram_bot_configs():
    try:
        # Read the config file
        with open('config.yml', 'r') as file:
            config = yaml.safe_load(file)

        # Access the values
        api_key = config['api_key']
        bot_name = config['bot_name']
        openai_key = config['openai_key']
    except (yaml.YAMLError, FileNotFoundError, KeyError):
        api_key = os.environ['API_KEY']
        bot_name = os.environ['BOT_NAME']
        openai_key = os.environ['OPENAI_KEY']
    return api_key, bot_name, openai_key
