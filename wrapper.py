import os
import yaml


def get_telegram_bot_configs():
    try:
        # Check if running on AWS environment
        if os.environ.get('ENVIRONMENT') == 'aws':
            api_key = os.environ['API_KEY']
            bot_name = os.environ['BOT_NAME']
            openai_key = os.environ['OPENAI_KEY']
        else:
            # Read the config file
            with open('config.yml', 'r') as file:
                config = yaml.safe_load(file)

            # Access the values
            api_key = config['api_key']
            bot_name = config['bot_name']
            openai_key = config['openai_key']
    except (yaml.YAMLError, FileNotFoundError, KeyError, TypeError):
        # Handle the case if any of the values are missing
        raise Exception('Bot token is not defined')

    return api_key, bot_name, openai_key
