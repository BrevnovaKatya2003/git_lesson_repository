import speech_recognition as sr
import sys
import webbrowser
import pyttsx3

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk('я вас слушаю')

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Говорите!')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language='ru-RU').lower()
        print('Вы сказали:' + zadanie)
    except sr.UnknownValueError:
        talk('Я вас не понял')
        zadanie = command()
    return zadanie

def makeSomething(zadanie):
    if 'открыть сайт' in zadanie:
        talk('Уже открываю')
        url = 'https://www.google.com'
        webbrowser.open(url)
    elif 'стоп' in zadanie or 'всё' in zadanie or 'пока' in zadanie:
        talk('Да, конечно, без проблем.....До свиданье')
        sys.exit()
    elif "как тебя зовут" in zadanie:
        talk('Меня зовут Игорь')
    elif "какая сегодня погода" in zadanie:
        talk('вот.....посмотрите')
        url = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&aqs=chrome..69i57j69i65.2332j0j7&sourceid=chrome&ie=UTF-8'
        webbrowser.open(url)
    elif "привет" in zadanie:
        talk('приветствую пользователь')
    elif "расскажи стишок" in zadanie:
        talk('цвет настраенья чёрный....................в руках записка то что ты приёмный')
    elif "как дела" in zadanie:
        talk('у меня всё хорошо.........................................спасибо')
    elif 'какие новости' in zadanie:
        talk('а вот какие')
        url = 'https://www.google.com/search?q=%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8&hl=ru&source=lnms&tbm=nws&sa=X&ved=0ahUKEwiR163kjf_fAhUQy6QKHeD8CD4Q_AUIDigB&biw=1707&bih=804&dpr=1.13'
        webbrowser.open(url)


while True:
    makeSomething(command())