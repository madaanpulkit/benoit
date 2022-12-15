import os, glob
import pyttsx3
import re
import random

engine = pyttsx3.init()
path = 'text_files'

engine.setProperty("rate", 200)
voices = engine.getProperty("voices")
num_voices = len(voices)
voice_examples = [0] * num_voices

for filename in glob.glob(os.path.join(path, '*.txt')):
    sentence_counter = 0
    print(filename)
    text = ''
    with open(os.path.join(os.getcwd(), filename), 'r', encoding='utf-8') as f:
        count = 0
        for line in f:
            count += 1
            
            rand = random.randint(0,num_voices - 1)
            voice_examples[rand] = voice_examples[rand] + 1
            engine.setProperty("voice", voices[rand].id)
            filename_new = re.sub('\.txt$', '', filename) + '-' + str(count)
            audio_name = filename_new + '.mp3'
            engine.save_to_file(line, audio_name)
            engine.runAndWait()
    
#0 is Male, 1 is Female
print(voice_examples)