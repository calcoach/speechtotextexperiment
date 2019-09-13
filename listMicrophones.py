import speech_recognition as sr

list = sr.Microphone.list_microphone_names()

print(list)