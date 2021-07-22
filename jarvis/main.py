from commands import _commands
from Global.print_talk import print_talk


def run_jarvis():
    _commands()


while True:
    try:
        run_jarvis()
    except:
        print_talk("Error")
        break
