from selfGUI import Self_Ask_GUI, Self_Bio_GUI
from pyttsx3 import init as tts_init
from selfINFO import SelfINFO
from time import sleep


TTS = tts_init()
TTS.setProperty('rate', 200)
RESUME = SelfINFO("./RESUME.ini")
# ASK = Self_Ask_GUI()


# Speak function
def speak(text: str):
    # TTS.say(text)
    # TTS.runAndWait()
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ASK.start()
    # salutation, theme = ASK.get_answers()
    salutation = "Sir"

    APP = Self_Bio_GUI(theme='Dark')
    APP.create_new_window(no_title_bar=True)
    APP.main_window()
    APP.create_two_columns()
    # For testing purposes only
    APP.left_panel.configure(highlightthickness=1, highlightbackground="blue", highlightcolor="blue")
    APP.right_panel.configure(highlightthickness=1, highlightbackground="green", highlightcolor="green")

    def additional():
        _interest, _curiosity = RESUME.get_options("HOBBIES")
        speak(f"Just for a bit of my additional information, I've keen interests in {_interest}."
              f"I'm eager to {_curiosity}.")
        _ = APP.create_additional_info(interests=_interest, curiosities=_curiosity)

    def communication():
        _languages = RESUME.get_options("COMMUNICATION")
        speak("")
        _ = APP.create_communication(languages=_languages)
        _.after(1000, additional)

    def certification():
        _name, _year = RESUME.get_options("IT_CERTIFICATION")
        speak(f"For the certificate degree, I've only one certification on {_name}.")
        _ = APP.create_certification(_name, _year)
        _.after(1000, communication)

    def title():
        _title, _name, _designation = RESUME.get_options("TITLE")
        speak(f"Hello, {salutation}. I'm expressing my heartfelt regard to you for giving me a chance to present "
              f"myself.")
        speak(f"The first and the foremost thing is that, I'm a {_title}, and act primarily as a {_designation}.")
        _ = APP.create_title(title=_title, name=_name, designation=_designation)
        _.after(1000, certification)

    APP.window.after(1000, title)
    title, name, designation = RESUME.get_options("TITLE")

    # -------
    APP.display_window()
