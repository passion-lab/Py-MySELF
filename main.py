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


def language_fluency(rate: int | float):
    if rate >= 95:
        return "advanced"
    elif rate >= 75:
        return "more or less fluently"
    elif rate >= 55:
        return "average"
    elif rate >= 35:
        return "somewhat"


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

    def education():
        _mp, _hs, _bachelor, _master = RESUME.get_options("MP_EDUCATION"), RESUME.get_options("HS_EDUCATION"), \
                                       RESUME.get_options("BACHELOR_EDUCATION"), RESUME.get_options("MASTER_EDUCATION")
        APP.create_education(mp=_mp, hs=_hs, bachelor=_bachelor, master=_master)

    def project_experience():
        _ = APP.create_project_experience()
        _.after(1000, education)

    def contact():
        _mobile, _email, _website, _github, _address = RESUME.get_options("CONTACT")
        speak(f"")
        _ = APP.create_contact(mobile=_mobile, email=_email, website=_website, github=_github, address=_address)
        _.after(1000, project_experience)

    def additional():
        _interest, _curiosity = RESUME.get_options("HOBBIES")
        speak(f"Just for a bit of my additional information, I've keen interests in {_interest}."
              f"I'm eager to {_curiosity}.")
        _ = APP.create_additional_info(interests=_interest, curiosities=_curiosity)
        _.after(1000, contact)

    def communication():
        _languages = RESUME.get_options("COMMUNICATION")
        _lang1, _lang2, _lang3 = _languages
        # speak("I can read, write and speak in {} {}".format(_lang1.split("; ")[0], language_fluency(_lang1.split("; ")[1])))
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

    # -------
    APP.display_window()
