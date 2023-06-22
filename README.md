# telebot_voice_to_text
This program is a Telegram Bot. It converts the voice message to a text.

#Install the dependency libraries
pip install -r requirements.txt

There may be problems with soundfile lib
To solve the problem, follow these steps:
1. pip install --upgrade soundfile
2. pip install --force-reinstall soundfile
3. pip install --upgrade pip wheel
4. python -m pip install --force-reinstall soundfile

To run the program can create a docker image e.g.
docker build -t image_name
docker run -it -v ./:/opt image_name
