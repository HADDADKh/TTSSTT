from gtts import gTTS
import speech_recognition as sr
r=sr.Recognizer();

def TTS(question, i):
   language='fr'
   myob=gTTS(question,lang=language,slow=False)
   myob.save('Question'+str(i)+'.mp3')
   return myob
   
def STT(voix):
	with sr.AudioFile(voix) as source:
	 audio=r.listen(source)
	print(r.recognize_google(audio))

#def play(voix):
#   from pygame import mixer
#   mixer.init()
#   mixer.music.load(voix)
#   mixer.music.play()
   
			
theFile= open('Question.txt', 'r') 
#print ("error")   
for lignenumber,ligne in enumerate(theFile) :
	   #Afficher la question
	   
	   print(ligne)
	   
	   #Tranformation de Texte en Voix
	   
	   voix=TTS(ligne, lignenumber)
print("\n")	
print("Exemple de transformation Voix au texte \n")
print("\n")
#Speach to text
STT("Rep1.wav")

	   	 
theFile.close()
