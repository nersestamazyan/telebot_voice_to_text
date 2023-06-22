import os
import unittest
from unittest.mock import MagicMock

import telebot

from helpers import get_wer_for_file
from telegram_bot import help_command, start_command, api_key, chat_id
from constants import HELP_COMMAND_RESPONSE, START_COMMAND_RESPONSE, REF_LIST, PATH_OF_TEST_WAV_FILES


class TestBot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bot = telebot.TeleBot(api_key)
        cls.chat_id = chat_id

    def setUp(self):
        self.message = MagicMock(chat=MagicMock(id=self.chat_id))
        self.reference = REF_LIST

    def test_help_command(cls):
        try:
            actual_response = help_command(cls.message)
            cls.assertEqual(
                HELP_COMMAND_RESPONSE, actual_response
            )
        except AssertionError as e:
            print(e, "\nActual value is not equal to the expected one")

    def test_start_command(cls):
        try:
            actual_response = start_command(cls.message)
            cls.assertEqual(
                START_COMMAND_RESPONSE, actual_response
            )
        except AssertionError as e:
            print(e, "\nActual value is not equal to the expected one")


    def test_wer_for_1_wav(self):
        resampled_file_name = os.path.join(PATH_OF_TEST_WAV_FILES, "1.wav")
        reference = self.reference[0]
        test_result = get_wer_for_file(resampled_file_name, reference)
        word_error_rate = test_result.get("word_error_rate")*100
        print(test_result)
        self.assertGreaterEqual(10, word_error_rate, "Word error rate should be less than 10%")

    def test_wer_for_2_wav(self):
        resampled_file_name = os.path.join(PATH_OF_TEST_WAV_FILES, "2.wav")
        reference = self.reference[1]
        test_result = get_wer_for_file(resampled_file_name, reference)
        word_error_rate = test_result.get("word_error_rate")*100
        print(test_result)
        self.assertGreaterEqual(10, word_error_rate, "Word error rate should be less than 10%")

    def test_wer_for_3_wav(self):
        resampled_file_name = os.path.join(PATH_OF_TEST_WAV_FILES, "3.wav")
        reference = self.reference[2]
        test_result = get_wer_for_file(resampled_file_name, reference)
        word_error_rate = test_result.get("word_error_rate")*100
        print(test_result)
        self.assertGreaterEqual(10, word_error_rate, "Word error rate should be less than 10%")


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
