import os
import re
from PIL import Image


#section global variables
all_defined_labels = []
all_defined_menus = []
all_defined_characters = []
all_defined_variables = []
all_existing_images = []

all_referenced_jumps = []
all_referenced_calls = []
all_referenced_variables = []
all_referenced_characters = []
all_referenced_images = []

all_referenced_images_that_dont_exist = []
all_referenced_characters_that_dont_exist = []
all_referenced_variables_that_dont_exist = []
all_referenced_jumps_that_dont_exist = []
all_unreachable_labels = []
all_unused_variables = []

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
    if re.match(r'[\s\t]*?scene\s',line["content"]):
        line["content"] = re.search(r'[\s\t]*?scene\s(.*?)(\s|\n|$)',line["content"]).group(1).strip()
        all_referenced_images.append(line)
    elif re.match(r'[\s\t]*?show\s',line["content"]):
        line["content"] = re.search(r'[\s\t]*?show\s(.*?$)',line["content"]).group(1).strip()
        all_referenced_images.append(line)

def check_for_variable_reference(line):
    global all_referenced_variables
    if not "renpy." in line["content"]:
        if re.match(r'[\s\t]*?\$(.*?)[\s\+\-=]',line["content"]):
            templine = line
            templine["content"] = re.search(r'[\s\t]*?\$(.*?)[\s\+\-=]',line["content"]).group(1).strip()
            all_referenced_variables.append(templine)
        #Below: Checks for inline reference like '"Menu choice" if not variable_name:' etc.
        if re.match(r'"\s(if not|if)\s(\w*?)[\s$:]',line["content"]):
            templine = line
            templine["content"] = re.search(r'"\s(if not|if)\s(\w*?)[\s$:]',line["content"]).group(2).strip()
            all_referenced_variables.append(templine)
        #Below: Checks for inline reference but starting with and/or
        if re.match(r'[\s\t]*?".*?".*?\s(and not|and|or not|or)\s(\w*?)[\s$:]',line["content"]):
            templine = line
            templine["content"] = re.search(r'[\s\t]*?".*?".*?\s(and not|and|or not|or)\s(\w*?)[\s$:]',line["content"]).group(2).strip()
            all_referenced_variables.append(templine)

def check_for_character_reference(line):
    global all_referenced_characters
    if re.match(r'[\s\t]*?(\w*?)\s"',line["content"]):
        line["content"] = re.search(r'[\s\t]*?(\w*?)\s"',line["content"]).group(1).strip()
        all_referenced_characters.append(line)

def check_for_jump_reference(line):
    global all_referenced_jumps
    if re.match(r'[\s\t]*?jump\s(.*?)$',line["content"]):
        line["content"] = re.search(r'[\s\t]*?jump\s(.*?)$',line["content"]).group(1).strip()
        all_referenced_jumps.append(line)

def check_for_call_reference(line):
    global all_referenced_calls
    if re.match(r'[\s\t]*?call\s(.*?)$',line["content"]):
        line["content"] = re.search(r'[\s\t]*?call\s(.*?)$',line["content"]).group(1).strip()
        all_referenced_calls.append(line)

def check_for_character_definition(line):
    global all_defined_characters
    if re.match(r'[\s\t]*?define\s(.*?)=\sCharacter.*?"',line["content"]):
        line["content"] = re.search(r'define\s(.*?)=\sCharacter.*?"',line["content"]).group(1).strip()
        all_defined_characters.append(line)
    if re.match(r'[\s\t]*?define\s(.*?)=\sDynamicCharacter.*?"',line["content"]):
        line["content"] = re.search(r'define\s(.*?)=\sDynamicCharacter.*?"',line["content"]).group(1).strip()
        all_defined_characters.append(line)

def check_for_variable_definition(line):
    global all_defined_variables
    if re.match(r'[\s\t]*?default\s(.*?)=.*?$',line["content"]):
        line["content"] = re.search(r'[\s\t]*?default\s(.*?)=.*?$',line["content"]).group(1).strip()
        all_defined_variables.append(line)

def check_for_label_definition(line):
    global all_defined_labels
    if re.match(r'[\s\t]*?label\s(.*?)[:]',line["content"]):
        line["content"] = re.search(r'[\s\t]*?label\s(.*?)[:]',line["content"]).group(1).strip()
        all_defined_labels.append(line)

def check_for_menu_definition(line):
    global all_defined_menus
    if re.match(r'[\s\t]*?menu\s(.*?)[:]',line["content"]):
        line["content"] = re.search(r'[\s\t]*?menu\s(.*?)[:]',line["content"]).group(1).strip()
        all_defined_menus.append(line)

def check_for_existing_images(line):
    global all_existing_images
    for root, dirs, file in os.walk(os.path.join(os.getcwd(),"game","images")):
        for image in file:
            if image.split(".")[-1].lower() in {"png","jpg","jpeg","webp"}:
                all_existing_images.append({
                    "fullpath":os.path.join(root, image),
                    "extension":image.split(".")[-1].lower(),
                    "filename":image.split("/")[-1].split(".")[0]
                })


def process_line(line):
    check_for_image_reference(line)
    check_for_variable_reference(line)
    check_for_character_reference(line)
    check_for_jump_reference(line)
    check_for_call_reference(line)

    check_for_character_definition(line)
    check_for_variable_definition(line)
    check_for_label_definition(line)
    check_for_menu_definition(line)

def check_images_that_dont_exist():
    global all_existing_images
    global all_referenced_images
    global all_referenced_images_that_dont_exist
    for image in all_referenced_images:
        for existing_image in all_existing_images:
            if image["content"] == existing_image["filename"]:
                break
        else:
            if not image["content"]=="black":
                all_referenced_images_that_dont_exist.append(image)
                append_messages_to_log(f'Image {image["content"]} that was referenced in {image["filename"]} (Line: {image["number"]}) does not exist in game/images folder')

def check_wrong_image_resolution():
    game_resolution = (1, 2)
    with open(os.path.join(os.getcwd(),"game","gui.rpy"), "r") as config:
        text = config.read()
        res = re.search(r"gui.init\((\d*?, \d*?)\)",text).group(1)
        res = res.split(",")
        game_resolution = (int(res[0]), int(res[1]))

    for root, dirs, file in os.walk(os.path.join(os.getcwd(),"game","images")):
        for image in file:
            if image.split(".")[-1].lower() in {"png","jpg","jpeg","webp"}:

                # get image
                filepath = os.path.join(root, image)
                img = Image.open(filepath)

                # get width and height
                width = img.width
                height = img.height
                if width!= game_resolution[0] or height!= game_resolution[1]:
                    append_messages_to_log(f'Image {image} has resolution {width}x{height}, which differs from the game resolution defined in gui.rpy ({game_resolution[0]}x{game_resolution[1]})')

def check_images_that_exist_multiple_times():
    global all_existing_images
    global all_referenced_images
    global images_that_exist_multiple_times
    for image1 in all_existing_images:
        for image2 in all_existing_images:
            if image1["filename"] == image2["filename"] and image1["extension"] != image2["extension"]:
                images_that_exist_multiple_times.append({"image1":image1, "image2":image2})
                append_messages_to_log(f'Image {image1["content"]} exist twice in game/images folder with differen file extensions: {image1["extension"]} and {image2["extension"]}')

def check_characters_that_dont_exist():
    global all_defined_characters
    global all_referenced_characters
    global all_referenced_characters_that_dont_exist
    for referenced_character in all_referenced_characters:
        for existing_character in all_defined_characters:
            if existing_character["content"] == referenced_character["content"] or referenced_character["content"] == "":
                break
        else:
            all_referenced_characters_that_dont_exist.append(referenced_character)
            append_messages_to_log(f'Character {referenced_character["content"]} that was referenced in {referenced_character["filename"]} (Line: {referenced_character["number"]}) has not been defined anywhere in your game files')

def check_variables_that_dont_exist():
    global all_defined_variables
    global all_referenced_variables
    global all_referenced_variables_that_dont_exist
    for referenced_variable in all_referenced_variables:
        for existing_variable in all_defined_variables:
            if existing_variable["content"] == referenced_variable["content"] or referenced_variable["content"] == "":
                break
        else:
            all_referenced_variables_that_dont_exist.append(referenced_variable)
            append_messages_to_log(f'Variable {referenced_variable["content"]} that was referenced in {referenced_variable["filename"]} (Line: {referenced_variable["number"]}) has not been defined anywhere in your game files')
            with open(os.path.join(os.getcwd(),"game","declarations","choices.rpy"), "a") as f:
                f.write(f"\ndefault {referenced_variable['content']} = False")

def check_variables_with_different_capitalization():
    global all_defined_variables
    global all_referenced_variables
    global all_referenced_variables_that_dont_exist
    for ref1 in all_referenced_variables:
        for ref2 in all_referenced_variables:
            if ref1["content"] != ref2["content"] and ref1["content"].lower() == ref2["content"].lower():
                append_messages_to_log(f'Variable {ref1["content"]} (File: {ref1["filename"]} (Line: {ref1["number"]})) and variable {ref1["content"]}(File: {ref2["filename"]} (Line: {ref2["number"]})) have the same name with different capitalization.')
    for def1 in all_defined_variables:
        for def2 in all_defined_variables:
            if def1["content"] != def2["content"] and def1["content"].lower() == def2["content"].lower():
                append_messages_to_log(f'Variable {def1["content"]}(File: {def1["filename"]} (Line: {def1["number"]})) and variable {def1["content"]}(File: {def2["filename"]} (Line: {def2["number"]})) have the same name with different capitalization.')

def check_characters_with_different_capitalization():
    global all_defined_characters
    global all_referenced_characters
    for ref1 in all_referenced_characters:
        for ref2 in all_referenced_characters:
            if ref1["content"] != ref2["content"] and ref1["content"].lower() == ref2["content"].lower():
                append_messages_to_log(f'character {ref1["content"]} (File: {ref1["filename"]} (Line: {ref1["number"]})) and character {ref1["content"]}(File: {ref2["filename"]} (Line: {ref2["number"]})) have the same name with different capitalization.')
    for def1 in all_defined_characters:
        for def2 in all_defined_characters:
            if def1["content"] != def2["content"] and def1["content"].lower() == def2["content"].lower():
                append_messages_to_log(f'character {def1["content"]}(File: {def1["filename"]} (Line: {def1["number"]})) and character {def1["content"]}(File: {def2["filename"]} (Line: {def2["number"]})) have the same name with different capitalization.')

def check_labels_with_different_capitalization():
    global all_defined_labels
    for ref1 in all_defined_labels:
        for ref2 in all_defined_labels:
            if ref1["content"] != ref2["content"] and ref1["content"].lower() == ref2["content"].lower():
                append_messages_to_log(f'label {ref1["content"]} (File: {ref1["filename"]} (Line: {ref1["number"]})) and label {ref1["content"]}(File: {ref2["filename"]} (Line: {ref2["number"]})) have the same name with different capitalization.')

def check_menus_with_different_capitalization():
    global all_defined_menus
    for ref1 in all_defined_menus:
        for ref2 in all_defined_menus:
            if ref1["content"] != ref2["content"] and ref1["content"].lower() == ref2["content"].lower():
                append_messages_to_log(f'menu {ref1["content"]} (File: {ref1["filename"]} (Line: {ref1["number"]})) and menu {ref1["content"]}(File: {ref2["filename"]} (Line: {ref2["number"]})) have the same name with different capitalization.')


def check_jumps_that_dont_exist():
    global all_defined_labels
    global all_defined_menus
    global all_referenced_jumps
    global all_referenced_jumps_that_dont_exist
    for referenced_jump in all_referenced_jumps:
        for existing_label in all_defined_labels + all_defined_menus:
            if existing_label["content"] == referenced_jump["content"]:
                break
        else:
            all_referenced_jumps_that_dont_exist.append(referenced_jump)
            append_messages_to_log(f'Jump statement {referenced_jump["content"]} that was referenced in {referenced_jump["filename"]} (Line: {referenced_jump["number"]}) has no matching label or named menu')

def check_unreachable_labels():
    global all_defined_labels
    global all_referenced_jumps
    global all_referenced_calls
    global all_unreachable_labels
    for defined_label in all_defined_labels:
        for referenced_jump in all_referenced_jumps + all_referenced_calls:
            if defined_label["content"] == referenced_jump["content"]:
                break
        else:
            if not defined_label["content"] == "start":
                all_unreachable_labels.append(defined_label)
                append_messages_to_log(f'label  {defined_label["content"]} that was referenced in {defined_label["filename"]} (Line: {defined_label["number"]}) exists, but no jump statements are leading to it (unreachable code)')

def check_unused_variables():
    global all_defined_variables
    global all_referenced_variables
    global all_unused_variables
    for defined_variable in all_defined_variables:
        for referenced_variable in all_referenced_variables:
            if defined_variable["content"] == referenced_variable["content"]:
                break
        else:
            all_unused_variables.append(defined_variable)
            append_messages_to_log(f'variable  {defined_variable["content"]} that was defined in {defined_variable["filename"]} (Line: {defined_variable["number"]}) is not used anywhere in the scanned script files')

def process_errors():
    check_images_that_dont_exist()
    check_images_that_exist_multiple_times()
    check_characters_that_dont_exist()
    check_variables_that_dont_exist()
    check_jumps_that_dont_exist()
    check_unreachable_labels()

def process_warnings():
    check_unused_variables()
    check_wrong_image_resolution()
    check_variables_with_different_capitalization()
    check_characters_with_different_capitalization()
    check_labels_with_different_capitalization()
    check_menus_with_different_capitalization()

def append_messages_to_log(message):
    with open(os.path.join(os.getcwd(),"debugger_report.txt"),"a+") as log:
        log.write(message)
        log.write("\n")



if __name__ == '__main__':
    all_script_files = get_all_script_filepaths()
    all_errors = []
    all_warning = []
    log_file_path = os.path.join(os.getcwd(),"debugger_report.txt")
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
    for script in all_script_files:
        plaintext = get_plain_text_from_script_file(script)
        for idx, line in enumerate(plaintext):
            line_processed = {
                "number":idx+1,
                "content":line,
                "filename":script.split("game")[-1]
            }
            process_line(line_processed)
    check_for_existing_images(line)
    append_messages_to_log("--------\nErrors:\n--------")
    process_errors()
    append_messages_to_log("--------\nWarnings:\n--------")
    process_warnings()
    test = "test"