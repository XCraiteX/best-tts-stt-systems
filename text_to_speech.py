import asyncio
from io import BytesIO
from time import sleep
import edge_tts

import pygame

VOICE = "ru-RU-DmitryNeural"
pygame.mixer.init()

async def make_speech_bytes(text: str) -> bytes:
    buffer = BytesIO()

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="+0%",
    )

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            buffer.write(chunk["data"])

    return buffer.getvalue()

def say(text: str):
    audio_bytes = asyncio.run(make_speech_bytes(text))

    audio_buffer = BytesIO(audio_bytes)
    audio_buffer.seek(0)

    pygame.mixer.music.load(audio_buffer, "mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        sleep(0.05)

    