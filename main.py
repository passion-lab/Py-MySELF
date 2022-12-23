from selfGUI import Self_Ask_GUI, Self_Bio_GUI
from pyttsx3 import init as tts_init
from selfINFO import SelfINFO
from time import sleep


TTS = tts_init()
TTS.setProperty('rate', 200)
RESUME = SelfINFO("./RESUME.ini")
ASK = Self_Ask_GUI()


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
    ASK.start()
    salutation, theme = ASK.get_answers()
    # salutation = "Sir"

    APP = Self_Bio_GUI(theme)
    APP.create_new_window(no_title_bar=True)
    APP.main_window()
    temp = APP.initial_banner()
    # temp.after(5000, lambda: temp.pack_forget())
    # APP.create_two_columns()
    # For testing purposes only
    # APP.left_panel.configure(highlightthickness=1, highlightbackground="blue", highlightcolor="blue")
    # APP.right_panel.configure(highlightthickness=1, highlightbackground="green", highlightcolor="green")

    def skill(**edu):
        speak(f"Speaking about my institutional education, I appeared {edu['_master'][1]} in {edu['_master'][3]}"
              f"with {edu['_master'][4]} marks. Before that, I passed {edu['_bachelor'][1]} with {edu['_bachelor'][4]} "
              f"marks in {edu['_bachelor'][3]}. From the {edu['_hs'][0]} board, I passed {edu['_hs'][1]} in "
              f"{edu['_hs'][3]} with {edu['_hs'][4]} of the total marks. {edu['_mp'][0]} was the board from which I "
              f"appeared in the {edu['_mp'][1]} examination in {edu['_mp'][2]} with {edu['_mp'][4]} marks.")

        _skills = RESUME.get_options('KEY_SKILLS')
        _ = APP.create_skills(_skills)
        _.after(1000, lambda: certification(_skills))

    def education(**prj):
        speak(f"I've done a number of projects, which are also in active development and have future  plans of "
              f"improvements too. Some of the featured projects are listed here. The first one is {prj['_p1'][:2]}."
              f"Then, {prj['_p2'][:2]}. {prj['_p3'][0]} is the third one, which is {prj['_p3'][1]}. Next, "
              f"{prj['_p4'][:2]}. Last but not the least, the fifth featured project is {prj['_p5'][:2]}. Click on "
              f"the hyperlink after each project's title to visit the GitHub repository for the respective project.")

        _mp, _hs, _bachelor, _master = RESUME.get_options("MP_EDUCATION"), RESUME.get_options("HS_EDUCATION"), \
                                       RESUME.get_options("BACHELOR_EDUCATION"), RESUME.get_options("MASTER_EDUCATION")
        _ = APP.create_education(mp=_mp, hs=_hs, bachelor=_bachelor, master=_master)
        _.after(1000, lambda: skill(_master=_master, _bachelor=_bachelor, _hs=_hs, _mp=_mp))

    def project_experience(**ttl):
        speak(f"Hello {salutation}. I'm expressing my heartfelt regard to you for giving me a chance to present "
              f"myself as a {ttl['_designation']}. The first and the foremost thing is that, I'm a {ttl['_title']}.")

        _project_1, _project_2 = RESUME.get_options("PROJECT_1"), RESUME.get_options("PROJECT_2")
        _project_3, _project_4 = RESUME.get_options("PROJECT_3"), RESUME.get_options("PROJECT_4")
        _project_5 = RESUME.get_options("PROJECT_5")
        _ = APP.create_project_experience(_project_1, _project_2, _project_3, _project_4, _project_5)
        _.after(1000, lambda: education(_p1=_project_1, _p2=_project_2, _p3=_project_3, _p4=_project_4, _p5=_project_5))

    def conclusion(*add_skill):
        speak(f"Besides Python what's my key skill, I also have some additional skills. Some of worth mentioning"
              f"additional skills I know are: {add_skill[0]}")

    def additional_skills(**cont):
        speak(f"If your kind consider allow you, kindly don't hesitate to contact me by calling me at "
              f"{cont['_mob'].replace('/', 'or')}, leaving a mail at {cont['_mail']}, visiting my website {cont['_web']}"
              f", going further to my repositories at {cont['_gh']} or by reaching me at my address that is {cont['_ad']}")

        _additional_skills = RESUME.get_options("ADDITIONAL_SKILLS")
        _ = APP.create_additional_skills(_additional_skills)
        _.after(1000, lambda: conclusion(_additional_skills))

    def contact(**add):
        speak(f"Just for a bit of my additional information, I've keen interests in {add['_interest']}."
              f"I'm eager to {add['_curiosity']}.")

        _mobile, _email, _website, _github, _address = RESUME.get_options("CONTACT")
        _ = APP.create_contact(mobile=_mobile, email=_email, website=_website, github=_github, address=_address)
        _.after(1000, lambda: additional_skills(_mob=_mobile, _mail=_email, _web=_website, _gh=_github, _ad=_address))

    def additional(**lang):
        for i in range(1, 4):
            globals()[f'lang_{i}'] = lang[f'_lang{i}'].split(" - ")[1]
            globals()[f'lang_{i}_fluency'] = language_fluency(int(lang[f'_lang{i}'].split(" - ")[0].strip("%")))
        speak(f"I can read, write and speak in {globals()['lang_1']}, {globals()['lang_2']} "
              f"{globals()['lang_1_fluency']}. In addition, I known {globals()['lang_3']} {globals()['lang_3_fluency']}")

        _interest, _curiosity = RESUME.get_options("HOBBIES")
        _ = APP.create_additional_info(interests=_interest, curiosities=_curiosity)
        _.after(1000, lambda: contact(_interest=_interest, _curiosity=_curiosity))

    def communication(**cert):
        speak(f"For the name of a certificate degree, I've one IT certification on {cert['_name']} which was from the "
              f"session {cert['_year'].replace(' - ', 'to')}.")

        _languages = RESUME.get_options("COMMUNICATION")
        _lang1, _lang2, _lang3 = _languages
        _ = APP.create_communication(languages=_languages)
        _.after(1000, lambda: additional(_lang1=_lang1, _lang2=_lang2, _lang3=_lang3))

    def certification(*skills):
        speak(f"In {skills[0][0]}, which is my primary skill, I know nearly about {skills[0][1].replace('-', 'of')}.")

        _name, _year = RESUME.get_options("IT_CERTIFICATION")
        _ = APP.create_certification(_name, _year)
        _.after(1000, lambda: communication(_name=_name, _year=_year))

    def title():
        _title, _name, _designation = RESUME.get_options("TITLE")
        _ = APP.create_title(title=_title, name=_name, designation=_designation)
        _.after(1000, lambda: project_experience(_title=_title, _name=_name, _designation=_designation))

    def launch():
        temp.pack_forget()
        APP.create_two_columns()
        speak(f"Good morning {salutation}, I'm feeling too excited to present myself to you.")
        APP.window.after(1000, title)

    temp.after(5000, launch)
    # -------
    APP.display_window()
