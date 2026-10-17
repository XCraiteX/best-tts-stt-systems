from RealtimeSTT import AudioToTextRecorder

def on_final(text):

    print("FINAL:", text)

if __name__ == "__main__":

    print('Запуск..')
    recorder = AudioToTextRecorder(
        model="large-v3-turbo",
        device="cuda",
        compute_type="int8_float16",
        language="ru",
        beam_size=1,
        enable_realtime_transcription=False,
        post_speech_silence_duration=0.3,
        spinner=False,
    )

    print("Слушаю...")
    while True:
        recorder.text(on_final)