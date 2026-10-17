import winsound

from tts_with_rvc import TTS_RVC

tts = TTS_RVC(
    # Заменить path на название модели в models/
    model_path="voices/model/{path}.pth",
    index_path="voices/model/{path}.index",
    device="cuda:0",
    f0_method="rmvpe",
)

tts.set_voice("ru-RU-DmitryNeural")

def play(text: str):
    audio_path = tts(
        text=text,
        pitch=0,
        index_rate=0.75,
    )

    print(audio_path)
    winsound.PlaySound(audio_path, winsound.SND_FILENAME)
