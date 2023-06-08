import os
import uuid

import requests
import telebot
import openai

from wrapper import get_telegram_bot_configs
from helpers import resample_the_audio_file, convert_to_dict
from constants import WORKDIR, TELEGRAM_DOWNLOAD_URL, HELP_COMMAND_RESPONSE, START_COMMAND_RESPONSE

api_key, bot_name, openai_key = get_telegram_bot_configs()
bot = telebot.TeleBot(api_key)
openai.api_key = openai_key


# Define the help command handler
@bot.message_handler(commands=['help'])
def help_command(message):
    print("Help command received")
    help_response = convert_to_dict(bot.reply_to(message, HELP_COMMAND_RESPONSE))
    return help_response.get("text")


# Define the start command handler
@bot.message_handler(commands=['start'])
def start_command(message):
    print("Start command received")
    start_response = vars(bot.reply_to(message, START_COMMAND_RESPONSE))
    return start_response.get("text")


# Define the voice message handler
@bot.message_handler(content_types=['voice'])
def voice_message(message):
    try:
        voice = message.voice
        file_id = voice.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        file_url = f"{TELEGRAM_DOWNLOAD_URL}{bot.token}/{file_path}"
        print(f"Audio received.")
        if not os.path.exists(WORKDIR):
            os.mkdir(WORKDIR)
        print("Getting working directory")
        # Defining the file name on the instance
        unique_id = str(uuid.uuid4().hex)
        file_name_on_machine = f"{WORKDIR}{unique_id}.ogg"
        print(f"File name is {file_name_on_machine}")

        # Downloading the voice message
        download_the_voice_message(message, file_url, file_name_on_machine)

        # Resampling the audio file
        resampled_file_name = resample_the_audio_file(file_name_on_machine)
        # Getting text from the audio file and sending it to the bot
        text_message = get_text_and_send_to_bot(resampled_file_name, message)
        return resampled_file_name, text_message
    except Exception as e:
        bot.reply_to(message, "An error occurred while processing the voice message.")
        print(e)


def get_text_and_send_to_bot(resampled_file_name, message):
    audio_file = open(resampled_file_name, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    response_dict = vars(transcript)
    text_message = response_dict.get('_previous').get("text")
    print(text_message)
    bot.reply_to(message, text_message)
    return text_message


def download_the_voice_message(message, file_url, file_name_on_machine):
    # Download the audio file using requests library
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(file_name_on_machine, 'wb') as file:
            file.write(response.content)
        print("Audio file downloaded successfully.")
        return file_name_on_machine
    else:
        bot.reply_to(message, "An error occurred while downloading the audio file.")
        print("An error occurred while downloading the audio file.")
