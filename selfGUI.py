from tkinter import (
    Tk,
    StringVar,
    Frame, Label, Canvas, PhotoImage, Message, Button
)
from webbrowser import open_new_tab


class Self_GUI_Styles:

    def __init__(self):
        # TODO: External font (.ttf and/or .otf) files will be included and ability to read here
        # TODO: Getting rid of installed fonts only
        # Fonts
        self.font = {
            "title"   : ('Candara Light', 40),
            "heading" : ('Candara Bold', 12),
            "emphasis": ('Candara', 25),
            "subtitle": ('Candara Italic', 10),
            "body"    : ('Candara', 12),
            "section" : ('Candara Bold', 30)
        }

        # Font Icons
        self.icon = {
            "action": ('Segoe UI Symbol', 20),
            "button": ()
        }

        # Colors
        self.color_fg = {
            "Light": {
                "highlight": "#32AB90",
                "title"   : "black",
                "heading" : "grey",
                "emphasis": "black",
                "subtitle": "darkgrey",
                "body"    : "black",
                "action"  : "lightgrey",
                "section" : "#EEEEEE"
            },
            "Dark": {
                "highlight": "#4EFFD7",
                "title"   : "white",
                "heading" : "grey",
                "emphasis": "darkgrey",
                "subtitle": "white",
                "body"    : "lightgrey",
                "action"  : "#2D2D2D",
                "section" : "#3D3D3D"
            }
        }
        self.color_bg = {
            "Light": {
                "BG"    : "lightgrey",
                "others": "white"
            },
            "Dark" : {
                "BG"    : "#0D0D0D",
                "others": "#1d1d1d"
            },
        }


class Self_Ask_GUI(Self_GUI_Styles):

    def __init__(self):
        super().__init__()
        # Defines variables individually (might be same or different) for each instance
        self.window: Tk | None = None  # empty Tkinter window will be used by all the methods(self) in this class
        self.screen_w = 0  # replaced by the host screen width once create_new_window() method is called
        self.screen_h = 0  # replaced by the host screen height once create_new_window() method is called
        self.geometry = {  # default values of a window's geometry and to save from the previous used values
            "w": 200,
            "h": 200,
            "x": 100,
            "y": 100
        }
        self.theme = "Light"  # default theme used if not set or skipped
        self.salutation = "Sir"  # default salutation used if not set or skipped
        self.ask_window_passed = False  # detects if the question/ask window(s) is/are displayed

    # TODO: User should call methods inside from their main file
    # Runs required methods from here
    def start(self):
        # Do if asking windows are not displayed yet
        if not self.ask_window_passed:
            win = self.create_new_window(no_title_bar=True)
            win_w, win_h, win_x, win_y = self.place_window_center(win, 500, 200, y_offset=-50)
            self.ask_window(width=win_w, height=win_h, x=win_x, y=win_y, save_geometry=True,
                            heading="KINDLY SAY,", question="What would I call you for?", options=("Sir", "Madam"))
            self.display_window()

        # Do if asking windows are displayed already
        # Exits in this case
        # self.close_window()
        self.window = None

    def create_new_window(self, no_title_bar: bool = False) -> Tk:
        """
        Creates and returns a new Tk() window instance that can be used throughout this class with self.
        It also updates the screen_w and screen_h attributes with the actual width and height of the
        host screen respectively.

        :param no_title_bar: If default window's title bar will present or not.
        :type no_title_bar: bool
        :return: Tkinter window instance
        :rtype: Tk
        """
        new_window = Tk()
        new_window.overrideredirect(no_title_bar)

        self.window = new_window  # updates the attribute with newly created Tkinter window instance
        self.screen_w = new_window.winfo_screenwidth()  # updates the attribute with host screen width
        self.screen_h = new_window.winfo_screenheight()  # updates the attribute with host screen height

        return new_window  # returns the newly created Tkinter window for further use where is requires

    def ask_window(self, width: int = 200, height: int = 200, x: int = 100, y: int = 100, save_geometry: bool = True,
                   heading: str = "HEADING",
                   question: str = "What do you want to know?",
                   options: tuple[str, str] = ("Option 1", "Option 2")) -> Tk:
        """
        Creates and displays the ask window with the provided heading, question and two options
        along with a skipping button to skip the window and proceed to the next.

        :param width: Width of this window (default is 200)
        :type width: int
        :param height: Height of this window. (default is 200)
        :type height: int
        :param x: X position of this window. (default is 100)
        :type x: int
        :param y: Y position of this window. (default is 100)
        :type y: int
        :param save_geometry: If the provided width, height, x, y will be stored for future use. If False, previously
                              saved values (if so) or default values is used currently. (default is True)
        :type save_geometry: bool
        :param heading: Question heading for better understanding.
        :type heading: str
        :param question: Actual question that you are interested to know for.
        :type question: str
        :param options: Two options e.g., ("A", "B") for possible answers of the question.
        :type options: tuple(str, str)
        :return: The whole question window itself.
        :rtype: Tk
        """
        # Saves the geometry by overwriting the default values for future use and if it is false,
        # it uses default or previously saved values (if so)
        if save_geometry:
            self.geometry['w'], self.geometry['h'], self.geometry['x'], self.geometry['y'] = width, height, x, y
        self.window.geometry(f"{self.geometry['w']}x{self.geometry['h']}+{self.geometry['x']}+{self.geometry['y']}")

        self.window.configure(background=self.color_bg[self.theme]['others'])
        # Whole window frame
        window_frame = Frame(self.window, background=self.color_bg[self.theme]['others'])
        window_frame.pack(fill="both", expand=True, padx=10)

        # Skip button
        skip = Label(window_frame, text="", anchor="e", font=self.icon['action'],
                     background=self.color_bg[self.theme]['others'], foreground=self.color_fg[self.theme]['action'])
        skip.pack(fill="x", padx=10, anchor="n")
        # Hide the question window on click for the next
        skip.bind('<Button-1>', lambda e=None: self.assign_salutation_theme())
        # Skip button appears in mouse hover on window
        window_frame.bind('<Enter>', lambda e=None: skip.configure(text="\uE0E3"))
        window_frame.bind('<Leave>', lambda e=None: skip.configure(text=""))

        # Heading and the Question
        Label(window_frame, text=heading, font=self.font['heading'], background=self.color_bg[self.theme]['others'],
              foreground=self.color_fg[self.theme]['heading']).pack(anchor="w")
        Label(window_frame, text=question, font=self.font['emphasis'], background=self.color_bg[self.theme]['others'],
              foreground=self.color_fg[self.theme]['emphasis']).pack(anchor="w")

        # Options frame for displaying the both side-by-side
        option_frame = Frame(window_frame, background=self.color_bg[self.theme]['others'])
        option_frame.pack(fill="x", pady=(20, 0))
        # Option 1
        option_1 = Label(option_frame, text=options[0], font=self.font['body'], anchor="e",
                         background=self.color_bg[self.theme]['others'], foreground=self.color_fg[self.theme]['body'])
        option_1.pack(side="left", fill="x", expand=True, padx=20)
        # Selects option 1 on click and hide the question window for the next
        option_1.bind('<Button-1>', lambda e=None: self.assign_salutation_theme(options[0]))
        # Option 2
        option_2 = Label(option_frame, text=options[1], font=self.font['body'], anchor="w",
                         background=self.color_bg[self.theme]['others'], foreground=self.color_fg[self.theme]['body'])
        option_2.pack(side="left", fill="x", expand=True, padx=20)
        # Selects option 2 on click and hide the question window for the next
        option_2.bind('<Button-1>', lambda e=None: self.assign_salutation_theme(options[1]))

        return self.window  # returns the whole ask window itself

    def assign_salutation_theme(self, arg: str | None = None):
        """ Assigns selected answers to the specified attribute. Also hides the window on click and do the next. """
        # TODO: Question options should be automated here
        if arg in ["Sir", "Madam"]:  # if it is question 1
            self.salutation = arg
        elif arg in ["Dark", "Light"]:  # else if it is question 2
            self.theme = arg

        # self.window.destroy()  # closes the current question window on click of any
        self.close_window()
        if not self.ask_window_passed:  # if not the two question windows are displayed already
            self.ask_window_passed = True
            # Creates and new window instance and display the question window again for the second time
            self.create_new_window(no_title_bar=True)
            self.ask_window(save_geometry=False, heading="CHOOSE YOUR FLAVOR,",
                            question="Which theme would you prefer?", options=("Dark", "Light"))
            self.display_window()
        else:  # else goto the start method again for task continuation
            self.start()

    def display_window(self):
        self.window.mainloop()

    def close_window(self):
        self.window.destroy()

    def get_answers(self):
        return self.salutation, self.theme

    @staticmethod
    def place_window_center(win: Tk, w: int, h: int, x_offset: int = 0, y_offset: int = 0):
        x = int(win.winfo_screenwidth() / 2 - w / 2 + x_offset)
        y = int(win.winfo_screenheight() / 2 - h / 2 + y_offset)
        # self.geometry['w'], self.geometry['h'], self.geometry['x'], self.geometry['y'] = w, h, x, y
        return w, h, x, y


class Self_Bio_GUI(Self_Ask_GUI):

    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        self.left_panel: Frame | None = None
        self.right_panel: Frame | None = None

    # Just for testing purpose
    def launch(self):
        from time import sleep

        self.create_new_window(no_title_bar=True)
        self.main_window()
        self.create_two_columns()
        self.left_panel.configure(highlightthickness=1, highlightbackground="blue", highlightcolor="blue")
        self.right_panel.configure(highlightthickness=1, highlightbackground="green", highlightcolor="green")

        self.display_window()

    def main_window(self):
        self.window.geometry(f"{self.screen_w}x{self.screen_h}")
        self.window.resizable(False, False)
        self.window.configure(background=self.color_bg[self.theme]['BG'])

    # Created two side panels on left and right
    def create_two_columns(self):
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=6)

        left_panel = Frame(self.window, bg=self.color_bg[self.theme]['BG'])
        left_panel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        right_panel = Frame(self.window, bg=self.color_bg[self.theme]['BG'])
        right_panel.grid(row=0, column=1, padx=10, pady=0, sticky="nsew")

        self.left_panel, self.right_panel = left_panel, right_panel

    # Frame template for each section based on provided side panel
    def create_section(self, side_panel: Frame, pad_y: tuple[float, float] = (0, 0)):
        # frame = Frame(side_panel, background=self.color_bg[self.theme]['others'])
        # frame.pack(side="top", fill="x")
        canvas = Canvas(side_panel, background=self.color_bg[self.theme]['others'], bd=0, highlightthickness=0)
        canvas.pack(side="top", fill="x", pady=pad_y)
        return canvas

    def create_section_name(self, section: Frame | Canvas, title: str):
        Label(section, text=title, font=self.font['section'], bg=self.color_bg[self.theme]['others'], pady=0, padx=0,
              fg=self.color_fg[self.theme]['section']).place(height=80, width=150, x=0, y=0)

    def create_title(self, title, name, designation):
        title_frame = self.create_section(self.left_panel)
        title_frame.configure(background=self.color_bg[self.theme]['BG'])
        Label(title_frame, text=title, font=self.font['title'], bg=self.color_bg[self.theme]['BG'],
              fg=self.color_fg[self.theme]['title'], anchor="w").pack(padx=10, pady=(20, 0), anchor="w")
        subtitle_frame = Frame(title_frame, bg=self.color_bg[self.theme]['BG'])
        subtitle_frame.pack(padx=10, pady=(0, 20), anchor="w")
        Label(subtitle_frame, text=name, font=self.font['heading'], bg=self.color_bg[self.theme]['BG'],
              fg=self.color_fg[self.theme]['highlight'], anchor="w").grid(row=0, column=0, sticky="w")
        Label(subtitle_frame, text=designation, font=self.font['heading'], bg=self.color_bg[self.theme]['BG'],
              fg=self.color_fg[self.theme]['heading'], anchor="w").grid(row=0, column=1, sticky="w")

        return title_frame

    def create_certification(self, name, year):
        title_frame = self.create_section(self.left_panel, (5, 0))
        Label(title_frame, text="IT", font=self.font['heading'],
              bg=self.color_bg[self.theme]['others'], fg=self.color_fg[self.theme]['heading'], anchor="w",
              ).pack(padx=10, pady=(10, 0), anchor="w")
        Label(title_frame, text=name, font=self.font['body'], bg=self.color_bg[self.theme]['others'],
              fg=self.color_fg[self.theme]['body'], anchor="w").pack(padx=10, pady=(0, 10), anchor="w")

        return title_frame

    def create_additional_info(self, interests, curiosities):
        title_frame = self.create_section(self.left_panel, (5, 0))
        Label(title_frame, text="INTERESTS IN", font=self.font['heading'],
              bg=self.color_bg[self.theme]['others'], fg=self.color_fg[self.theme]['heading'], anchor="w",
              ).pack(padx=10, pady=(10, 0), anchor="w")
        Label(title_frame, text=interests, font=self.font['body'], bg=self.color_bg[self.theme]['others'],
              wraplength=500, justify="left",
              fg=self.color_fg[self.theme]['body'], anchor="w").pack(padx=10, pady=(0, 5), anchor="w")

        Label(title_frame, text="CURIOSITY TO", font=self.font['heading'],
              bg=self.color_bg[self.theme]['others'], fg=self.color_fg[self.theme]['heading'], anchor="w",
              ).pack(padx=10, pady=(0, 0), anchor="w")
        Label(title_frame, text=curiosities, font=self.font['body'], bg=self.color_bg[self.theme]['others'],
              fg=self.color_fg[self.theme]['body'], anchor="w").pack(padx=10, pady=(0, 10), anchor="w")

        return title_frame

    def create_communication(self, languages: list):
        title_frame = self.create_section(self.left_panel, (5, 0))
        Label(title_frame, text="READ, WRITE AND SPEAK IN", font=self.font['heading'],
              bg=self.color_bg[self.theme]['others'], fg=self.color_fg[self.theme]['heading'], anchor="w",
              ).pack(padx=10, pady=(10, 0), anchor="w")

        grid_frame = Frame(title_frame)
        grid_frame.pack(fill="x", padx=10, pady=(0, 10))
        for i, language in enumerate(languages):
            grid_frame.columnconfigure(i, weight=1)
            # Label(title_frame, text=language, font=self.font['body'], bg=self.color_bg[self.theme]['others'],
            #       fg=self.color_fg[self.theme]['body'], anchor="w").pack(padx=10, pady=(0, 10) if i == 2 else 0,
            #                                                              anchor="w", side="left")
            Label(grid_frame, text=language, font=self.font['body'], bg=self.color_bg[self.theme]['others'],
                  fg=self.color_fg[self.theme]['body'], anchor="w").grid(row=0, column=i, sticky='ew')

        return title_frame

    def create_contact(self, mobile, email, website, github, address):
        title_frame = self.create_section(self.left_panel, (5, 0))
        Label(title_frame, text="MODE OF CONTACT", font=self.font['heading'],
              bg=self.color_bg[self.theme]['others'], fg=self.color_fg[self.theme]['heading'], anchor="w",
              ).pack(padx=10, pady=(10, 0), anchor="w")
        Label(title_frame, text=mobile, font=self.font['body'], bg=self.color_bg[self.theme]['others'],
              fg=self.color_fg[self.theme]['body'], anchor="w").pack(padx=10, pady=(0, 0), anchor="w")
        Label(title_frame, text=email, font=self.font['body'], bg=self.color_bg[self.theme]['others'],
              fg=self.color_fg[self.theme]['body'], anchor="w").pack(padx=10, pady=(0, 0), anchor="w")
        Label(title_frame, text=website, font=self.font['body'], bg=self.color_bg[self.theme]['others'],
              fg=self.color_fg[self.theme]['body'], anchor="w").pack(padx=10, pady=(0, 0), anchor="w")
        Label(title_frame, text=github, font=self.font['body'], bg=self.color_bg[self.theme]['others'],
              fg=self.color_fg[self.theme]['body'], anchor="w").pack(padx=10, pady=(0, 0), anchor="w")
        Label(title_frame, text=address, font=self.font['body'], bg=self.color_bg[self.theme]['others'],
              fg=self.color_fg[self.theme]['body'], anchor="w").pack(padx=10, pady=(0, 10), anchor="w")

        return title_frame

    def create_additional_skills(self, add_skills: list):
        title_frame = self.create_section(self.left_panel, (5, 0))
        Label(title_frame, text="ADDITIONAL SKILLS INCLUDE", font=self.font['heading'],
              bg=self.color_bg[self.theme]['others'], fg=self.color_fg[self.theme]['heading'], anchor="w",
              ).pack(padx=10, pady=(10, 0), anchor="w")
        Label(title_frame, text=" | ".join(add_skills), font=self.font['body'], bg=self.color_bg[self.theme]['others'],
              fg=self.color_fg[self.theme]['body'], anchor="w", wraplength=500, justify='left').pack(
            padx=10, pady=(0, 10), anchor="w")

        return title_frame

    def create_right_section(self, section_name):
        bg_frame = Frame(self.right_panel, bg=self.color_bg[self.theme]['BG'], height=1000)
        bg_frame.pack(side="top", fill="both")
        Label(bg_frame, text=section_name, font=self.font["section"], bg=self.color_bg[self.theme]['BG'],
              fg=self.color_fg[self.theme]["section"]).pack(side="top", anchor="e")

        return bg_frame

    def create_project_experience(self, project_1: list, project_2: list, project_3: list,
                                  project_4: list, project_5: list):
        projects = {
            1: (project_1[0], project_1[1], project_1[2], project_1[3]),
            2: (project_2[0], project_2[1], project_2[2], project_2[3]),
            3: (project_3[0], project_3[1], project_3[2], project_3[3]),
            4: (project_4[0], project_4[1], project_4[2], project_4[3]),
            5: (project_5[0], project_5[1], project_5[2], project_5[3])
        }

        bg_frame = self.create_right_section("PROJECTS")
        # Adding required amount of blanks texts for background frame's space
        for _ in range(int(len(projects) * 2.8)):
            Label(bg_frame, text="").pack()
        fg_frame = Frame(bg_frame, bg=self.color_bg[self.theme]['others'])
        fg_frame.place(x=0, y=30, relwidth=1.0, relheight=1.0)

        i = 0
        for _, project in projects.items():
            title_frame = Frame(fg_frame, bg=self.color_bg[self.theme]['others'])
            title_frame.pack(fill="x", padx=10, pady=(10, 0) if i == 0 else 0)
            title_frame.columnconfigure(2, weight=1)
            Label(title_frame, text=project[0], font=self.font['heading'], justify='left',
                  bg=self.color_bg[self.theme]['others'], fg=self.color_fg[self.theme]['highlight'], anchor="w",
                  ).grid(row=0, column=0, sticky="w")
            Label(title_frame, text=project[1], font=self.font['subtitle'], justify='left',
                  bg=self.color_bg[self.theme]['others'], fg=self.color_fg[self.theme]['heading'], anchor="w",
                  ).grid(row=0, column=1, sticky="w")
            Button(title_frame, text="[  GitHub Repo ]", bd=0, bg=self.color_bg[self.theme]['others'], cursor="hand2",
                   fg=self.color_fg[self.theme]['heading'], activebackground=self.color_bg[self.theme]['others'],
                   activeforeground=self.color_fg[self.theme]['highlight'], anchor="e",
                   command=lambda link=project[3]: open_new_tab(link)).grid(row=0, column=2, sticky="e")
            Label(fg_frame, text=project[2], font=self.font['body'], bg=self.color_bg[self.theme]['others'],
                  fg=self.color_fg[self.theme]['body'],
                  anchor="w").pack(padx=10, pady=(0, 10) if i == 4 else 0, anchor="w")

        return bg_frame

    def create_education(self, mp: list, hs: list, bachelor: list, master: list):
        qualifications = {
            "MASTER"          : (master[0], master[1], master[2], master[3], master[4]),
            "BACHELOR"        : (bachelor[0], bachelor[1], bachelor[2], bachelor[3], bachelor[4]),
            "HIGHER SECONDARY": (hs[0], hs[1], hs[2], hs[3], hs[4]),
            "SECONDARY"       : (mp[0], mp[1], mp[2], mp[3], mp[4])
        }
        bg_frame = self.create_right_section("EDUCATION")
        # Adding required amount of blanks texts for background frame's space
        for _ in range(int(len(qualifications) * 2.8)):
            Label(bg_frame, text="").pack()
        fg_frame = Frame(bg_frame, bg=self.color_bg[self.theme]['others'])
        fg_frame.place(x=0, y=30, relwidth=1.0, relheight=1.0)
        for i, qualification in enumerate(qualifications):
            title_frame = Frame(fg_frame, bg=self.color_bg[self.theme]['others'])
            title_frame.pack(padx=10, pady=(10, 0), anchor="w")
            Label(title_frame, text=qualifications[qualification][1].upper(),
                  font=self.font['heading'], bg=self.color_bg[self.theme]['others'],
                  fg=self.color_fg[self.theme]['highlight'], anchor="w").grid(row=0, column=0, sticky='w')
            Label(title_frame, text=qualifications[qualification][0],
                  font=self.font['subtitle'], bg=self.color_bg[self.theme]['others'],
                  fg=self.color_fg[self.theme]['heading'], anchor="w").grid(row=0, column=1, sticky='w')
            Label(fg_frame, text=f"In {qualifications[qualification][3]} with {qualifications[qualification][4]} marks "
                                 f"during {qualifications[qualification][2]}.", font=self.font['body'],
                  bg=self.color_bg[self.theme]['others'],
                  fg=self.color_fg[self.theme]['body'], anchor="w").pack(padx=10, pady=(0, 0), anchor="w")

        return bg_frame

    def create_skills(self, skills: list):
        bg_frame = self.create_right_section("KEY SKILLS")
        # Adding required amount of blanks texts for background frame's space
        for _ in range(3):
            Label(bg_frame, text="").pack()
        fg_frame = Frame(bg_frame, bg=self.color_bg[self.theme]['others'])
        fg_frame.place(x=0, y=30, relwidth=1.0, relheight=1.0)

        title_frame = Frame(fg_frame, bg=self.color_bg[self.theme]['others'])
        title_frame.pack(fill='x', padx=10, pady=(10, 0), anchor='w')
        title_frame.columnconfigure(1, weight=1)
        Label(title_frame, text=skills[0].upper(),
              font=self.font['heading'], bg=self.color_bg[self.theme]['others'],
              fg=self.color_fg[self.theme]['highlight'], anchor="w").grid(row=0, column=0, sticky='w')
        button = Label(title_frame, text=f"[  {skills[2]} ]", bg=self.color_bg[self.theme]['others'], cursor='hand2',
                       fg=self.color_fg[self.theme]['heading'], activeforeground=self.color_fg[self.theme]['highlight'])
        button.grid(row=0, column=1, sticky='e')
        button.bind('<Button-1>', lambda e=None: open_new_tab(f"https://www.github.com/{skills[2]}"))
        button.bind('<Enter>', lambda e=None: button.configure(fg=self.color_fg[self.theme]['highlight']))
        button.bind('<Leave>', lambda e=None: button.configure(fg=self.color_fg[self.theme]['heading']))

        text_frame = Frame(fg_frame)
        text_frame.pack(fill="x", padx=10)
        for i in range(3):
            text_frame.columnconfigure(i, weight=1)
            text_frame.rowconfigure(i, weight=1)
            Label(text_frame, text=skills[1].split(";")[i], font=self.font['body'], anchor="w",
                  bg=self.color_bg[self.theme]['others'], fg=self.color_fg[self.theme]['body']).grid(row=0, column=i,
                                                                                                     sticky="nsew")
            Label(text_frame, text=skills[1].split(";")[i + 3], font=self.font['body'], anchor="w",
                  bg=self.color_bg[self.theme]['others'], fg=self.color_fg[self.theme]['body']).grid(row=1, column=i,
                                                                                                     sticky="nsew")
        return bg_frame
