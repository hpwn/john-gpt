import os
import asyncio
from twitchio.ext import commands
from pydub import AudioSegment
import requests
import subprocess
import time

# Constants for your setup
TTS_MODEL_URL = (
    "http://localhost:8000/generate_audio"  # Placeholder URL for your TTS model
)
CHATBOT_MODEL_URL = (
    "http://localhost:8000/generate_response"  # Placeholder URL for your chatbot model
)
AUDIO_FOLDER = "path/to/your/audio_folder"  # Folder where audio files will be saved
TWITCH_TOKEN = "ctvbx62ohsd2epfp80v7syu7emekz3"
TWITCH_REFRESH_TOKEN = "2vx9w0znsskof17u8v1yi7c2peb15aa50rl0gsmt569olzxrcu"
TWITCH_CHANNEL = "hp_az"
TWITCH_NICK = "hp_az"


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TWITCH_TOKEN, prefix="!", initial_channels=[TWITCH_CHANNEL]
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message):
        print(f"Message from {message.author.name}: {message.content}")
        if message.echo:
            return

        # Process message
        # response_text = get_chatbot_response(message.content)
        # audio_file_path = generate_tts_audio(response_text)

        # Do something with the audio file, e.g., move it to the monitored folder
        # move_audio_to_folder(audio_file_path, AUDIO_FOLDER)


def get_chatbot_response(message):
    # This function sends the chat message to the chatbot model and gets a response
    # Replace with actual code to invoke your local chatbot model
    response = requests.post(CHATBOT_MODEL_URL, json={"message": message})
    return response.text


def generate_tts_audio(text):
    # This function sends the text to the TTS model and gets an audio file
    # Replace with actual code to invoke your local TTS model
    response = requests.post(TTS_MODEL_URL, json={"text": text})
    audio_content = response.content
    audio_file_path = save_audio_file(audio_content)
    return audio_file_path


def save_audio_file(audio_content):
    # This saves the audio content to a file
    file_path = os.path.join(AUDIO_FOLDER, "output.mp3")
    with open(file_path, "wb") as audio_file:
        audio_file.write(audio_content)
    return file_path


def move_audio_to_folder(file_path, folder):
    # This moves the audio file to the specified folder
    dest_path = os.path.join(folder, os.path.basename(file_path))
    os.rename(file_path, dest_path)
    print(f"Moved audio file to {dest_path}")


# Run the bot
bot = Bot()
bot.run()
