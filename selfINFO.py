from configparser import ConfigParser, ParsingError, NoSectionError
from os import PathLike


class SelfINFO:

    def __init__(self, resume_ini_file):
        self.ini = ConfigParser()
        self.read_resume(resume_ini_file)
        self.sections = self.ini.sections()

    def read_resume(self, file_path):
        if isinstance(file_path, (str, bytes, PathLike)):
            try:
                self.ini.read(file_path)
            except ParsingError:
                raise ParsingError
        else:
            raise OSError

    def get_options(self, section: str):
        if section in self.sections:
            values = []
            for option in self.ini.options(section):
                values.append(self.ini.get(section, option))
            return values
        else:
            raise NoSectionError(f"ERROR! No section found with the name '{section}'.")


if __name__ == '__main__':
    info = SelfINFO("./RESUME.ini")
    print(info.sections)

