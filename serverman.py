import subprocess
import os
from appJar import gui

def new():
    name=input("Enter New Name:")
    subprocess.run(["mkdocs","new", name])
    os.chdir(name)
    print("done")
    subprocess.run(["mkdocs","serve"])
def start():
    subprocess.run(["mkdocs","serve"])
def build():
    subprocess.run(["mkdocs","build"])

app = gui("RRS 4.0")
app.addButton("New",new)
app.addButton("start",start)
app.go()