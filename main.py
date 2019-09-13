import speech_recognition as sr
import keyboard

def callback(sr,audio):
 text = r.recognize_google(audio)
 print('Digiste : {}'.format(text))

def heardComand(comand):
 if(comand == 'close'):
  keyboard.minimice()

 if(comand.__contains__('abre') | comand.__contains__('abrir')):
  open(comand)

#instance recognizer
r = sr.Recognizer()
sr.energy_threshold = True
#this is for adjust the
sr.dynamic_energy_adjustment_damping = 0.15
key  = "AIzaSyCfHMlG2Tv4_cvfbxearIsaBk3cmumemaw";

with sr.Microphone() as source:
 r.adjust_for_ambient_noise(source)

 while (True):
   print("Di algo")
   audio = r.listen(source)

   try:
    text = r.recognize_google(audio,key,"es-CO")
    heardComand(text)
    print('Digiste : {}'.format(text))
    #r.listen_in_background(source,callback(r,audio),None)

    #print(text)

   except sr.RequestError as e:
    print(e)


