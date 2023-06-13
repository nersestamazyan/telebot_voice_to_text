import os
import unittest
from unittest.mock import MagicMock

import telebot
from jiwer import wer

from helpers import get_wer_for_file, get_text_from_voice, get_list_of_all_test_wav_files
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

    # To run all the WER tests as one
    # def test_wer_all(self):
    #     test_results = []
    #     wav_file_list = get_list_of_all_test_wav_files(path=PATH_OF_TEST_WAV_FILES)
    #     for i, (resampled_file_name, reference) in enumerate(zip(wav_file_list, self.reference)):
    #         print(resampled_file_name)
    #         print("This was the original text\n", reference)
    #         recognized_transcript = get_text_from_voice(resampled_file_name)
    #
    #         word_error_rate = wer(reference, hypothesis=recognized_transcript)
    #         print("This is the recognized transcript\n", recognized_transcript)
    #         print(f"The word error rate is {word_error_rate}")
    #         test_result = {
    #             'resampled_file_name': resampled_file_name,
    #             'reference': reference,
    #             'recognized_transcript': recognized_transcript,
    #             'word_error_rate': word_error_rate
    #         }
    #         test_results.append(test_result)
    #
    #     return test_results

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

# def run_tests():
#     suite = unittest.TestSuite()
#     suite.addTest(TestBot('test_help_command'))
#     suite.addTest(TestBot('test_start_command'))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
