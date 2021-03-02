from os.path import dirname, abspath
import subprocess

path = dirname(abspath(__file__))


def setup():
    subprocess.call("py -m pip install --upgrade pip",               shell=True)
    subprocess.call(f"py -m pip install -r {path}/requirements.txt", shell=True)
