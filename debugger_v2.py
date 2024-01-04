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

def check_for_character_definition(line):
    global all_defined_characters
    if re.match(r'[\s\t]*?define\s(.*?)=\sCharacter.*?"',line["Line content"]):
        line["Line content"] = re.search(r'define\s(.*?)=\sCharacter.*?"',line["Line content"]).group(1).strip()
        all_defined_characters.append(line)
    if re.match(r'[\s\t]*?define\s(.*?)=\sDynamicCharacter.*?"',line["Line content"]):
        line["Line content"] = re.search(r'define\s(.*?)=\sDynamicCharacter.*?"',line["Line content"]).group(1).strip()
        all_defined_characters.append(line)

def check_for_variable_definition(line):
    global all_defined_variables
    if re.match(r'[\s\t]*?default\s(.*?)=.*?$',line["Line content"]):
        line["Line content"] = re.search(r'[\s\t]*?default\s(.*?)=.*?$',line["Line content"]).group(1).strip()
        all_defined_variables.append(line)

def check_for_label_definition(line):
    global all_defined_labels
    if re.match(r'[\s\t]*?label\s(.*?)[:]',line["Line content"]):
        line["Line content"] = re.search(r'[\s\t]*?label\s(.*?)[:]',line["Line content"]).group(1).strip()
        all_defined_labels.append(line)

def check_for_menu_definition(line):
    global all_defined_menus
    if re.match(r'[\s\t]*?menu\s(.*?)[:]',line["Line content"]):
        line["Line content"] = re.search(r'[\s\t]*?menu\s(.*?)[:]',line["Line content"]).group(1).strip()
        all_defined_menus.append(line)

def check_for_existing_images(line):
    global all_existing_images
    for root, dirs, file in os.walk(os.path.join(os.getcwd(),"game","images")):
        for image in file:
            if image.split(".")[-1].lower() in {"png","jpg","jpeg","webp"}:
                all_existing_images.append({
                    "fullpath":os.path.join(root, image),
                    "extension":image.split(".")[-1].lower(),
                    "filename":image.split("/")[-1]
                })


def process_line(line):
    check_for_image_reference(line)
    check_for_variable_reference(line)
    check_for_character_reference(line)
    check_for_jump_reference(line)

    check_for_character_definition(line)
    check_for_variable_definition(line)
    check_for_label_definition(line)
    check_for_menu_definition(line)

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
    check_for_existing_images(line)

    test = "test"