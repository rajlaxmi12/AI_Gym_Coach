    
from io import BytesIO
from gtts import gTTS

class TextToSpeech:
    def speak(self, text, lang="en"):
        cleaned = (text or "").strip()

        if not cleaned:
            return

        buffer = BytesIO()

        gTTS(text=cleaned, lang=lang).write_to_fp(buffer)

        buffer.seek(0)

        audio = buffer.read()

        with open("test.mp3", "wb") as f:
            f.write(audio)

        print("Saved test.mp3")

        return audio