from gtts import gTTS
import os

def text_to_speech_file(text, folder):
    tts = gTTS(text=text, lang='en')
    save_path = os.path.join("user_uploads", folder, "audio.mp3")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    tts.save(save_path)
    print(f"Audio saved at {save_path}")
    return save_path

# text_to_speech_file("hlo my name is sohrab and i am a student of btech","fca3ff39-b8e3-11f0-b25d-78af080840d4")