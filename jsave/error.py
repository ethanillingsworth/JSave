from colorxs import Color

class Error():
    def __init__(self, code: int, string: str, fatal: bool = False):
        if fatal:
            print(f"{Color.RED}FATAL: {string}")
        else:
            print(f"{Color.DARK_YELLOW}WARN: {string}")


        quit(f"{Color.DARK_YELLOW}Code: J{code}{Color.CLEAR}")

    