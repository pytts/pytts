from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import inspect
import os

script_location_with_name = inspect.stack()[0][1]
script_location = os.path.dirname(script_location_with_name)
words_dir_location = os.path.join(script_location, 'words')

class Pytts():
    def __init__(self):
        # Get audio files
        self.words = os.listdir(words_dir_location)
        # Only use filters that are m4a
        self.words = list(filter(lambda filename: filename.endswith('.m4a'), self.words))
        # Remove the extension
        self.words = list(map(lambda filename: filename.replace('.m4a', ''), self.words))
    def speak(self, text):
        words = text.split(' ')
        print(words)
        audio = None
        for word in words:
            if not audio:
                audio = self.get_word(word)
            else:
                audio = audio + self.get_word(word)
        audio.export('output.mp3', format='mp3')
    def get_word(self, word):
        audio = self.get_word_from_list(word)
        if not audio:
            audio = self.get_google_tts_word(word)
        
        return audio
    

    def get_google_tts_word(self, word):
        mp3_fp = BytesIO()
        tts = gTTS(word)
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        audio = AudioSegment.from_mp3(mp3_fp)
        return audio
    def get_word_from_list(self, word):
        print(word, self.words, os.path.join(words_dir_location, f'{word}.m4a'))
        if word in self.words:
            filename = os.path.join(words_dir_location, f'{word}.m4a')
            return AudioSegment.from_file(filename, 'm4a')
        return None
