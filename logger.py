import sys


def log(text):
    print(text, file=sys.stdout)
    sys.stdout.flush()
