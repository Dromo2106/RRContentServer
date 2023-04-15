import subprocess
import os
name=input("Enter New Name:")
subprocess.run(["mkdocs","new", name])
os.chdir(name)
print("done")
subprocess.run(["mkdocs","serve"])