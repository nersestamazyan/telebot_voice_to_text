import os

import openai
import soundfile as sf
from jiwer import wer

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
