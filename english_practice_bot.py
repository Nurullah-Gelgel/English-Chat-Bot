import speech_recognition as sr
import pyttsx3
from poe_api_wrapper import AsyncPoeApi
import asyncio
import language_tool_python
import json

tokens = {
    'p-b': '',
    'p-lat': ''
}

# Konuşma geçmişi ve kullanıcı profili
conversation_history = []
user_profile = {
    "goal": "general",  # Hedef: "business", "daily" gibi seçenekler eklenebilir
    "mistakes": [],
    "feedback": {}
}

# Dilbilgisi denetimi için araç oluştur
tool = language_tool_python.LanguageTool('en-US')

async def fetch_response(client, message):
    response = ""
    async for chunk in client.send_message(bot="gpt3_5", message=message):
        response += chunk["response"]
    return response

def grammar_check(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text, matches

def suggest_alternatives(text):
    # Basit kelime önerileri (bu fonksiyon geliştirilebilir)
    # Örneğin: kelime yerine sinonim önerileri
    alternatives = {
        "good": ["excellent", "great", "fine"],
        "bad": ["terrible", "poor", "subpar"]
    }
    words = text.split()
    suggested_text = ' '.join([alternatives.get(word, [word])[0] for word in words])
    return suggested_text

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def update_profile(mistakes):
    user_profile["mistakes"].extend(mistakes)
    # Belirli aralıklarla ilerlemeyi güncelleme
    # Örneğin, her 10 konuşmada bir geri bildirim
    if len(conversation_history) % 10 == 0:
        provide_feedback()

def provide_feedback():
    # Kullanıcının yaptığı hataları analiz ederek geri bildirim sağlar
    mistake_count = len(user_profile["mistakes"])
    print(f"İlerleme Geri Bildirimi: Toplam {mistake_count} hata tespit edildi.")
    user_profile["feedback"] = {
        "total_mistakes": mistake_count,
        "last_update": len(conversation_history)
    }

async def main():
    recognizer = sr.Recognizer()
    
    # Mikrofonu başlat ve çevresel gürültüyü ayarla sadece bir kez
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
    
    # API'yi başlat ve bir kez oluştur
    client = await AsyncPoeApi(tokens=tokens).create()
    
    print("Sesli sohbet başlıyor. Çıkmak için 'exit' komutunu verin.")
    
    while True:
        with sr.Microphone() as source:
            print("Dinliyorum...")
            try:
                # Ses kaydını al, 5 saniye timeout
                audio = recognizer.listen(source, timeout=1)
                message = recognizer.recognize_google(audio)
                print(f"Sen: {message}")
                
                # Konuşma geçmişine mesajı ekle
                conversation_history.append(f"You: {message}")
                
                # Dilbilgisi denetimi yap
                corrected_message, matches = grammar_check(message)
                if corrected_message != message:
                    print(f"Dilbilgisi Hatası Düzeltilmiş Mesaj: {corrected_message}")
                    message = corrected_message
                    # Dilbilgisi hatalarını güncelle
                    update_profile(matches)
                
                # Kelime önerileri sun
                suggested_message = suggest_alternatives(message)
                if suggested_message != message:
                    print(f"Kelime Önerileri: {suggested_message}")

                if message.lower() == "exit":
                    print("Çıkış yapılıyor...")
                    break

                # API'den yanıt al
                response = await fetch_response(client, message)
                print(f"Bot: {response}")
                
                # Konuşma geçmişine bot yanıtını ekle
                conversation_history.append(f"Bot: {response}")

                # Bot'un yanıtını sesli olarak oku
                speak(response)

            except sr.UnknownValueError:
                print("Sesi anlayamadım, lütfen tekrar söyleyin.")
            except sr.RequestError as e:
                print(f"Google Speech Recognition servisi erişilemedi; {e}")
            except Exception as e:
                print(f"Beklenmeyen bir hata oluştu: {e}")

    # Kullanıcı profilini bir dosyaya kaydet (gelişim takibi için)
    with open('user_profile.json', 'w') as f:
        json.dump(user_profile, f, indent=4)

# Asenkron kodu çalıştır
if __name__ == "__main__":
    asyncio.run(main())
