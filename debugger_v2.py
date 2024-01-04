import os
import re
from PIL import Image
import random
import subprocess

#section global variables
all_defined_labels = []
all_defined_menus = []
all_defined_characters = []
all_defined_variables = []
all_existing_images = []

all_referenced_jumps = []
all_referenced_variables = []
all_referenced_characters = []
all_referenced_images = []


def get_all_script_filepaths():
    exclude_script_files = ['gui.rpy', 'options.rpy','screens.rpy']
    return_script_files = []
    foldername = os.path.join(os.getcwd(),"game")
    for root, dirs, file in os.walk(foldername):
        for script in file:
            if script.endswith('rpy'):
                if not script in exclude_script_files:
                    return_script_files.append(os.path.join(root, script))
    return return_script_files

def get_plain_text_from_script_file(script):
    with open(script, encoding="utf8") as f:
        scriptlines = f.readlines()
        #scriptlines = clean_up_script_file(scriptlines)
        return scriptlines

def check_for_image_reference(line):
    global all_referenced_images
    if re.match(r'[\s\t]*?scene\s',line["Line content"]):
        line["Line content"] = re.search(r'[\s\t]*?scene\s(.*?)(\s|\n|$)',line["Line content"]).group(1).strip()
        all_referenced_images.append(line)
    elif re.match(r'[\s\t]*?show\s',line["Line content"]):
        line["Line content"] = re.search(r'[\s\t]*?show\s(.*?$)',line["Line content"]).group(1).strip()
        all_referenced_images.append(line)

def check_for_variable_reference(line):
    global all_referenced_variables
    if re.match(r'[\s\t]*?\$(.*?)=',line["Line content"]):
        line["Line content"] = re.search(r'[\s\t]*?\$(.*?)=',line["Line content"]).group(1).strip()
        all_referenced_variables.append(line)
    #Below: Checks for inline reference like '"Menu choice" if not variable_name:' etc.
    if re.match(r'"\s(if not|if)\s(\w*?)[\s$:]',line["Line content"]):
        line["Line content"] = re.search(r'"\s(if not|if)\s(\w*?)[\s$:]',line["Line content"]).group(2).strip()
        all_referenced_variables.append(line)
    #Below: Checks for inline reference but starting with and/or
    if re.match(r'\s(and not|and|or not|or)\s(\w*?)[\s$:]',line["Line content"]):
        line["Line content"] = re.search(r'\s(and not|and|or not|or)\s(\w*?)[\s$:]',line["Line content"]).group(2).strip()
        all_referenced_variables.append(line)

def check_for_character_reference(line):
    global all_referenced_characters
    if re.match(r'[\s\t]*?(\w*?)\s"',line["Line content"]):
        line["Line content"] = re.search(r'[\s\t]*?(\w*?)\s"',line["Line content"]).group(1).strip()
        all_referenced_characters.append(line)

def check_for_jump_reference(line):
    global all_referenced_jumps
    if re.match(r'[\s\t]*?jump\s(.*?)$',line["Line content"]):
        line["Line content"] = re.search(r'[\s\t]*?jump\s(.*?)$',line["Line content"]).group(1).strip()
        all_referenced_jumps.append(line)


def process_line(line):
    check_for_image_reference(line)
    check_for_variable_reference(line)
    check_for_character_reference(line)
    check_for_jump_reference(line)



if __name__ == '__main__':
    all_script_files = get_all_script_filepaths()
    all_errors = []
    all_warning = []

    for script in all_script_files:
        plaintext = get_plain_text_from_script_file(script)
        for idx, line in enumerate(plaintext):
            line_processed = {
                "Line number":idx+1,
                "Line content":line,
                "File name":script.split("/")[-1]
            }
            process_line(line_processed)
        #get all image declarations
        #get all image references
        #get all variable declarations
        #get all variable references
        #get all jump references
        #get all label declarations
        #get all named menu declarations
        #get all music declarations
        #get all music references
        #get all character declarations
        #get all character references

    test = "test"