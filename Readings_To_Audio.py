from gtts import gTTS
import os
import textract

list_of_files_to_process = []

for file in os.listdir("text/"):
    list_of_files_to_process.append(file)


for item in list_of_files_to_process:
    text = textract.process("text/" + item)
    text = text.decode('utf-8')

    tts = gTTS(text=text, lang='en')
    tts.save(item + ".mp3")



