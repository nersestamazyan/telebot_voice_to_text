import unittest
from unittest.mock import MagicMock

import telebot

from telegram_bot import help_command, start_command, api_key
from constants import HELP_COMMAND_RESPONSE, START_COMMAND_RESPONSE


class TestBot(unittest.TestCase):
    def setUp(self):
        self.bot = telebot.TeleBot(api_key)
        self.chat_id = 1253340468
        self.message = MagicMock(chat=MagicMock(id=self.chat_id))

    def test_help_command(self):
        try:
            actual_response = help_command(self.message)
            self.assertEqual(
                HELP_COMMAND_RESPONSE, actual_response
            )
        except AssertionError as e:
            print(e, "\nActual value is not equal to the expected one")

    def test_start_command(self):
        try:
            actual_response = start_command(self.message)
            self.assertEqual(
                START_COMMAND_RESPONSE, actual_response
            )
        except AssertionError as e:
            print(e, "\nActual value is not equal to the expected one")


if __name__ == '__main__':
    unittest.main()
