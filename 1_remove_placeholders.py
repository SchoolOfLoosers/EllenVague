from pathlib import Path
import os
import re

story_directory = os.path.join(os.getcwd(),'game','story')

for root, dirs, file in os.walk(story_directory):
    for script in file:
        if script.endswith('rpy'):
            filepath = os.path.join(root, script)
            rplce = ""
            with open(filepath, "r") as rfile:
                s = rfile.read()
                if re.search('menu .*?menu_name',s):
                    print("Removing placeholder in file: "+ script)
                    rplce = re.sub('menu .*?menu_name', "menu", s)
                if re.search(r'^[\t\s]*?dialog[\s\t$\n]?',s, re.MULTILINE):
                    print("Removing placeholder in file: "+ script)
                    rplce = re.sub(r'[\t\s]*?dialog[\s\t$\n]?', "\n", s,re.MULTILINE)
                if re.search(r'\"Text to say\"\n',s, re.MULTILINE):
                    print("Removing placeholder in file: "+ script)
                    rplce = re.sub(r'\"Text to say\"\n', "\"Text to say\" #todo\n", s,re.MULTILINE)
            if rplce!= "":
                with open(filepath, "w") as wfile:
                    wfile.write(rplce)