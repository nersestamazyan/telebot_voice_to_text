import os

import openai
import soundfile as sf
from jiwer import wer
import numpy as np

from constants import WORKDIR


def resample_the_audio_file(file_name_on_machine):
    file_name_with_extension = file_name_on_machine.split("/")[-1]
    file_name = file_name_with_extension.split(".")[0]
    resampled_file_name = f"{WORKDIR}resampled_{file_name}.wav"
    print('File name is', file_name)
    print('Resampled file name is', resampled_file_name)
    audio, samplerate = sf.read(file_name_on_machine)
    print("file read successfully")
    # Resample and save the audio to the file
    sf.write(resampled_file_name, audio, 32000, 'PCM_16')
    print("Voice message received and resampled!")
    return resampled_file_name


def convert_to_dict(telegram_object):
    converted_dict = vars(telegram_object)
    return converted_dict


def get_text_from_voice(resampled_file_name):
    with open(resampled_file_name, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        response_dict = convert_to_dict(transcript)
        if response_dict.get('_previous').get("text") != '':
            text_message = response_dict.get('_previous').get("text")
        else:
            text_message = 'The voice message was empty'
        return text_message


def get_list_of_all_test_wav_files(path):
    file_list = []
    for file_name in os.listdir(path):
        if file_name.endswith(".wav"):
            file_list.append(os.path.join(path, file_name))
            file_list = sorted(file_list, key=lambda x: os.path.basename(x))
    print(file_list)
    return file_list


# Using jiwer library
def get_wer_for_file(resampled_file_name, reference):
    print(resampled_file_name)
    print("This was the original text\n", reference)
    recognized_transcript = get_text_from_voice(resampled_file_name)

    word_error_rate = wer(reference, hypothesis=recognized_transcript)
    print("This is the recognized transcript\n", recognized_transcript)
    print(f"The word error rate is {word_error_rate}")

    test_result = {
        'resampled_file_name': resampled_file_name,
        'reference': reference,
        'recognized_transcript': recognized_transcript,
        'word_error_rate': word_error_rate
    }

    return test_result


def calculate_wer(resampled_file_name, reference):
    recognized_transcript = get_text_from_voice(resampled_file_name)
    # Split both texts to get lists of words
    split_recognized_text = recognized_transcript.split()
    word_list_for_reference = reference.split()
    word_count_for_reference = len(word_list_for_reference)
    word_count_for_recognized_text = len(split_recognized_text)
    # Use numpy zeros to get a matrix with the lengths + 1 of the texts
    distance = np.zeros((word_count_for_reference + 1, word_count_for_recognized_text + 1))
    # Filling the first row and column with the numbers in ascending order of the words count
    for i in range(word_count_for_reference + 1):
        distance[i, 0] = i
    for j in range(word_count_for_recognized_text + 1):
        distance[0, j] = j
    # Iterating over the words in both predefined and recognized texts
    for i in range(1, word_count_for_reference + 1):
        for j in range(1, word_count_for_recognized_text + 1):
            # If the words are the same, then no operation is needed
            if word_list_for_reference[i - 1] == split_recognized_text[j - 1]:
                distance[i, j] = distance[i - 1, j - 1]
            else:
                # Otherwise we need to count the number of actions to make the words match
                # We count it for three different operations - substitution, insertion, and deletion, and we need to
                # take the minimum number as the less, the better
                substitution = distance[i - 1, j - 1] + 1
                insertion = distance[i, j - 1] + 1
                deletion = distance[i - 1, j] + 1
                distance[i, j] = min(substitution, insertion, deletion)
    # Finally, in order to get the word error rate, we get the value of the last cell, and then divide it to
    # the total number of the predefined text
    word_error_rate = distance[word_count_for_reference, word_count_for_recognized_text] / word_count_for_reference
    return word_error_rate


# Using the function above
def get_wer_for_one_file(resampled_file_name, reference):
    word_error_rate = calculate_wer(resampled_file_name, reference)
    print(f"The word error rate is {word_error_rate}")

    test_result = {
        'resampled_file_name': resampled_file_name,
        'reference': reference,
        'word_error_rate': word_error_rate
    }

    return test_result

