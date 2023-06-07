import soundfile as sf
from crontab import CronTab

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


def create_cron_job(directory_path, hour, minute):
    cron = CronTab(user=True)

    # Check if the cron job already exists
    for job in cron:
        if job.command == f'find {directory_path} -type f -mtime +1 -delete':
            print("Cron job already exists. Skipping creation.")
            return

    # Create a new cron job
    new_job = cron.new(command=f'find {directory_path} -type f -mtime +1 -delete')
    new_job.setall(f'{minute} {hour} * * *')
    cron.append(new_job)
    cron.write()
    print("Cron job created successfully.")


