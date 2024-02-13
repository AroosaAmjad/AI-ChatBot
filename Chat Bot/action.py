import textTOspeech
import speechTOtext
import datetime
import webbrowser
import weather

def action(data):

    user_data = data.lower()

    if "what is your name" in user_data:
        textTOspeech.text_to_speech("My name is virtual assistant.")
        return "My name is virtual assistant."

    elif "hello" in user_data or "hi" in user_data:
        textTOspeech.text_to_speech("Hey there! How can I help you?")
        return "Hey there! How can I help you?"

    elif "good morning." in user_data:
        textTOspeech.text_to_speech("Good morning. Hope you will have a great day.")
        return "Good morning. Hope you will have a great day."

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour: ", (str)(current_time.minute) + "Minute"
        textTOspeech.text_to_speech(Time)
        return Time

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        textTOspeech.text_to_speech("Music is ready")
        return "Music is ready"

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        textTOspeech.text_to_speech("Youtube is ready.")
        return "Youtube is ready."

    elif "google" in user_data:
        webbrowser.open("https://google.com/")
        textTOspeech.text_to_speech("Google is ready.")  
        return "Google is ready."

    elif "weather" in user_data:
        ans = weather.weather()
        textTOspeech.text_to_speech(ans)
        return ans

    elif "bye" in user_data:
        textTOspeech.text_to_speech("Bye! TC")
        return "Bye! TC"

    else:
        textTOspeech.text_to_speech("Sorry. I am unable to understand.")
        return "Sorry. I am unable to understand."

