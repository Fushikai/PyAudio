import speech_recognition as sr


#estrutura para captura de audio.
r = sr.Recognizer()
#print(sr.Microphone().list_microphone_names())
with sr.Microphone(1) as mic:
    r.adjust_for_ambient_noise(mic)
    print("teste gravar audio")
    audio = r.listen(mic)
    #para nao ter erro é recognize_ibm, recognize_google.
    texto = r.recognize_google(audio, language="pt-BR")
    print(texto)