from colorxs import Color

class Error():
    def __init__(self, code: int, string: str, fatal: bool = False):
        if fatal:
            print(f"{Color.RED}FATAL: {string}")
            quit(f"{Color.DARK_YELLOW}Code: J{code}{Color.CLEAR}")
        else:
            print(f"{Color.DARK_YELLOW}WARN: {string}")
            print(f"{Color.DARK_YELLOW}Code: J{code}{Color.CLEAR}")


