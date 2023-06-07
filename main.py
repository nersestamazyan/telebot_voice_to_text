from telegram_bot import bot
from helpers import create_cron_job
from constants import WORKDIR


if __name__ == "__main__":
    # Deleting the old audio files
    create_cron_job(directory_path=WORKDIR, hour=20, minute=25)
    # Start the bot
    print("Bot is polling")
    bot.polling()

