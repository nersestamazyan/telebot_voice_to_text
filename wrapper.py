import yaml


def get_telegram_bot_configs():
    try:
        with open('config.yml', 'r') as file:
            config = yaml.safe_load(file)
        api_key = config['api_key']
        bot_name = config['bot_name']
        openai_key = config['openai_key']
        chat_id = config['chat_id']
    except (yaml.YAMLError, KeyError, TypeError):
        raise Exception('A config is not defined')

    return api_key, bot_name, openai_key, chat_id
