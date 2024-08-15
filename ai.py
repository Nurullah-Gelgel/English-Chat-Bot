import speech_recognition as sr
import pyttsx3
from poe_api_wrapper import AsyncPoeApi
import asyncio

tokens = {
    'p-b': '',
    'p-lat': ''
}

async def fetch_response(client, history):
    response = ""
    async for chunk in client.send_message(bot="gpt3_5", message=history):
        response += chunk["response"]
    return response

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def correct_mistakes(response):
    # Hataları düzeltmek için basit bir işlev
    corrected_response = response.replace("your wrong word", "your correct word")
    return corrected_response

async def main():
    recognizer = sr.Recognizer()
    
    # Mikrofonu başlat ve çevresel gürültüyü ayarla sadece bir kez
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
    
    # API'yi başlat ve bir kez oluştur
    client = await AsyncPoeApi(tokens=tokens).create()
    
    print("English speaking practice has started. Say 'exit' to stop.")
    
    conversation_history = ""  # Konuşma geçmişini tutmak için bir değişken
    
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            try:
                # Ses kaydını al, 5 saniye timeout
                audio = recognizer.listen(source, timeout=5)  
                message = recognizer.recognize_google(audio)
                print(f"You: {message}")

                if message.lower() == "exit":
                    print("Exiting...")
                    break

                # Konuşma geçmişine yeni mesajı ekle
                conversation_history += f"\nYou: {message}"

                # API'den yanıt al
                response = await fetch_response(client, conversation_history)

                # Yanıtı düzeltme
                corrected_response = correct_mistakes(response)
                
                # Konuşma geçmişine botun yanıtını ekle
                conversation_history += f"\nBot: {corrected_response}"
                print(f"Bot: {corrected_response}")

                # Düzeltme yaptıysa, kullanıcıya bilgi ver
                if corrected_response != response:
                    print("Correction made.")
                    speak(f"Correction made: {corrected_response}")
                else:
                    speak(corrected_response)

            except sr.UnknownValueError:
                print("I couldn't understand the speech, please try again.")
            except sr.RequestError as e:
                print(f"Google Speech Recognition service is unavailable; {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

# Asenkron kodu çalıştır
if __name__ == "__main__":
    asyncio.run(main())
