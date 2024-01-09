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
            if rplce!= "":
                with open(filepath, "w") as wfile:
                    wfile.write(rplce)