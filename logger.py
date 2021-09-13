import sys


def log(text):
    print(text, file=sys.stderr)
    sys.stderr.flush()
