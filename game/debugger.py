import os
import re
from PIL import Image
import random
import subprocess

def get_all_script_filepaths(foldername):
    exclude_script_files = ['gui.rpy', 'options.rpy','screens.rpy']
    return_script_files = []
    if not foldername:
        foldername = os.getcwd()
    for root, dirs, file in os.walk(foldername):
        for script in file:
            if script.endswith('rpy'):
                if not script in exclude_script_files:
                    return_script_files.append(os.path.join(root, script))
    return return_script_files

def get_all_script_files_clean_text(filepaths):
    return_script_files = []
    for script_file in filepaths:
        return_script_files.append(get_text_from_script_file(script_file))
    return return_script_files

def get_text_from_script_file(script):
    with open(script, encoding="utf8") as f:
        scriptlines = f.readlines()
        scriptlines = clean_up_script_file(scriptlines)
        return scriptlines

def get_plain_text_from_script_file(script):
    with open(script, encoding="utf8") as f:
        scriptlines = f.readlines()
        scriptlines = clean_up_script_file(scriptlines)
        return '\n'.join(scriptlines)

def get_all_labels_from_script_files(script_files):
    labels = []
    for script_file in script_files:
        if 'label' in script_file:
            temp_labels = re.split('\Wlabel\s', script_file)

            for templabel in temp_labels:
                if templabel:
                    templabel = ('label '+ templabel ).replace('label label ','label ')#i know, i know...
                    name = re.search(r'label\s(.*?)[\s$:]',templabel).group(1)
                    referenced_images = get_referenced_images_in_label(templabel)
                    referenced_variables = get_referenced_variables_in_label(templabel)
                    referenced_music = get_referenced_music_in_label(templabel)
                    referenced_characters = get_referenced_characters_in_label(templabel)
                    referenced_jumps = get_referenced_jumps_in_label(templabel)
                    menus = get_menus_from_label(templabel)

                    labels.append({"name": name,"referenced_images":referenced_images,"referenced_variables":referenced_variables,"labels_referenced":referenced_jumps,"referenced_music":referenced_music,"referenced_characters":referenced_characters, "referenced_jumps":referenced_jumps,"menus":menus,"full_text":templabel})

    return labels

def get_referenced_images_in_label(label_text):
    result = []
    for line in label_text.split('\n'):
        if re.match(r'[\s\t]*?scene\s',line):
            result.append(re.search(r'[\s\t]*?scene\s(.*?)(\s|\n|$)',line).group(1).strip())
        if re.match(r'[\s\t]*?show\s',line):
            result.append(re.search(r'[\s\t]*?show\s(.*?$)',line).group(1).strip())
    return result

def get_referenced_music_in_label(label_text):
    result = []
    for line in label_text.split('\n'):
        if re.match(r'[\s\t]*?play\s(.*?)$',line):
            result.append(re.search(r'[\s\t]*?play(\smusic\s|\s)"(.*?)"$',line).group(2).strip()) #todo only return music name
        if re.match(r'[\s\t]*?voice\s(.*?)$',line):
            result.append(re.search(r'[\s\t]*?voice\s"(.*?)"$',line).group(1).strip())
    return result

def get_referenced_variables_in_label(label_text):
    result = []
    for line in label_text.split('\n'):
        if '$' in line: #todo also check for inline ifs and report any variables that have no =  (so missing variable assignment)
            try:
                result.append(re.search(r'.*?\$(\w*?)[\s=]',line).group(1).strip()) #todo only return image name
            except Exception as e:
                pass
    return result

def get_referenced_characters_in_label(label_text):
    result = []
    for line in label_text.split('\n'):
        if re.match(r'[\s\t]*?(\w*?)\s"',line): #todo check for dialog
            match = re.search(r'[\s\t]*?(\w*?)\s"',line).group(1)
            if match != '':
                result.append(match) #this takes care of narrator that is always "defined"
    return result

def get_referenced_jumps_in_label(label_text):
    result = []
    for line in label_text.split('\n'):
        if re.match(r'[\s\t]*?jump\s(.*?)$',line): #todo check for dialog
            result.append(re.search(r'[\s\t]*?jump\s(.*?)$',line.rstrip()).group(1).strip())
    return result

def get_menus_from_label(label_text):
    result = []
    for temp_menu in re.split('[\s{4}|\t{1}]menu',label_text)[1::1]:#the last part ignores the first split element that is everything before the first split happens
        temp_menu = 'menu '+temp_menu
        temp_menu = temp_menu.replace('menu :','menu:')

        name = ''
        options = []
        temp_options = re.split(r'([\s{8}\t{2}]".*?":)',temp_menu)[1::1]
        #workaround because split puts the delimiters as an own item into the list
        for i in range(1, len(temp_options)+1):
            if i % 2 == 0:
                options.append({"option_name":temp_options[i-2],"option_text":temp_options[i-1]})

        #     #todo figure out recursive structure for menus inside menus
        menu = {"name":name,"options":options,"full_text":temp_menu}
        result.append(menu)
    return result

def clean_up_script_file(text):
    result = []
    line_number = 0

    for line in text:
        # line = line.lstrip()
        line = re.sub(r'#.*?$','',line) #strip comments
        line = re.sub(r'\swith (hpunch|vpunch|fade).*?$','',line) #strip with / transition statements
        line = line.rstrip()
        #line = re.sub(r'".*?"$','""',line) #delete all text inside double quotes to prevent false positives.
        result.append(line)
    return result

def get_all_defined_variables(script_files):
    result = []
    for file in script_files:
        for line in file:
            if re.match(r'.*?default\s(.*?)=.*?$',line):
                result.append(re.search(r'.*?default\s(.*?)=.*?$',line).group(1).strip())
    return result

def get_all_empty_voice_files(path_to_game_directory):
    result = []

    for fIndex, file in enumerate(get_all_script_files_clean_text(all_script_filepaths)):
        for index, line in enumerate(file):
            if re.match(r'.*?voice\s"".*?$',line):
                result.append("Empty voice file declaration detected in file: "+all_script_filepaths[fIndex].split('\\')[-1]+" in line: "+str(index+1))
    return result

def get_all_text_without_voice_files(path_to_game_directory):
    result = []

    # for fIndex, file in enumerate(get_all_script_files_clean_text(all_script_filepaths)):
    #     for index, line in enumerate(file):
    #         if not 'voice "' in line and not 'play music' in line:
    #             if re.match(r'.*?\w+?\s".*?".*?$',line):
    #                 if not '"..."' in line and not '"(chuckles)"' in line and not '"(laughs)"' in line:
    #                     if not re.match(r'.*?voice\s".*?"$',file[index-1]):
    #                         result.append("Character text without associated voice in file: "+all_script_filepaths[fIndex].split('\\')[-1]+" in line: "+str(index+1))
    return result


def get_all_defined_image_names(script_files):
    result = []
    for file in script_files:
        for line in file:
            if re.match(r'image\s(.*?)=\s".*?"',line):
                result.append(re.search(r'image\s(.*?)=\s".*?"',line).group(1).strip())
    return result

def get_all_referenced_image_names(folder_path):
    result = []
    text = get_all_script_files_clean_text(folder_path)
    for file in text:
        for line in file:
            if re.match(r'image\s(.*?)=\s".*?"',line):
                result.append(re.search(r'image\s(.*?)=\s".*?"',line).group(1).strip())
    #todo
    return result

def get_all_defined_characters(script_files):
    result = []

    for file in script_files:
        for line in file:
            if re.match(r'define\s(.*?)=\sCharacter.*?"',line):
                result.append(re.search(r'define\s(.*?)=\sCharacter.*?"',line).group(1).strip())
            if re.match(r'define\s(.*?)=\sDynamicCharacter.*?"',line):
                result.append(re.search(r'define\s(.*?)=\sDynamicCharacter.*?"',line).group(1).strip())
    return result

def get_all_defined_music(script_files):
    result = []

    for file in script_files:
        for line in file:
            if not 'Character(' in line:
                if re.match(r'define\s(.*?)=.*?"',line):
                    result.append(re.search(r'define\s(.*?)=.*?"',line).group(1).strip())
    return result

def get_all_defined_labels(folder_path):
    result = []
    text = get_all_script_files_clean_text(folder_path)

    for file in text:
        for line in file:
            if re.match(r'.*?label\s(.*?)[:]',line):
                result.append(re.search(r'.*?label\s(.*?)[:]',line).group(1).strip())
    return result

def get_all_defined_menus(script_files):
    result = []

    for file in script_files:
        for line in file:
            if re.match(r'.*?menu\s(.*?):',line):
                result.append(re.search(r'.*?menu\s(.*?):',line).group(1).strip())
    return result
def find_image_by_full_name(referenced_image,existing_images_in_folder):
    for existing_image in existing_images_in_folder:
        if re.match(r'\..*?$',referenced_image):
            if referenced_image == existing_image:
                return existing_image
        if referenced_image == re.sub(r'\..*?$','',existing_image):
            return existing_image
    return None
def find_image_by_full_name_without_extension(referenced_image,existing_images_in_folder):
    for existing_image in existing_images_in_folder:
        if re.sub(r'\..*?$','',referenced_image) == re.sub(r'\..*?$','',existing_image) :
            return existing_image
    return None

def find_image_by_full_name_without_underscores_or_dashes(referenced_image,existing_images_in_folder):
    for existing_image in existing_images_in_folder:
        if re.sub(r'[-_]','',referenced_image) in re.sub(r'[-_]','',existing_image):
            return existing_image
    return None
def find_image_by_full_name_with_different_capitalization(referenced_image,existing_images_in_folder):
    for existing_image in existing_images_in_folder:
        if referenced_image.lower() in existing_image.lower():
            return existing_image
    return None

def get_referenced_images_that_dont_exist(label,existing_images_in_folder):
    result = []
    name = label['name']
    referenced_images = label['referenced_images']
    image_files = existing_images_in_folder
    image_files = [re.sub(r'\..*?$','',x) for x in image_files]

    for referenced_image in referenced_images:
        found_image_by_full_name = find_image_by_full_name(referenced_image,existing_images_in_folder)
        found_image_by_full_name_without_extension = find_image_by_full_name_without_extension(referenced_image,existing_images_in_folder)
        found_image_by_full_name_without_underscores_or_dashes = find_image_by_full_name_without_underscores_or_dashes(referenced_image,existing_images_in_folder)
        found_image_by_full_name_with_different_capitalization = find_image_by_full_name_with_different_capitalization(referenced_image,existing_images_in_folder)

        if not found_image_by_full_name and not found_image_by_full_name_without_extension and not "expression" in referenced_image:
            if found_image_by_full_name_without_underscores_or_dashes:
                result.append("Image " + referenced_image + " that was called in label '" + label['name'] + "' does not exist but was found using alternate spelling: " + found_image_by_full_name_without_underscores_or_dashes)
            elif found_image_by_full_name_with_different_capitalization:
                result.append("Image " + referenced_image + " that was called  in label '" + label['name'] + "' does not exist but was found using alternate capitalization: " + found_image_by_full_name_with_different_capitalization)
            else:
                result.append("Image " + referenced_image + " that was called  in label '" + label['name'] + "' does not exist")
    return result

def get_referenced_images_that_dont_match_game_resolution(label,path_to_game_directory):
    result = []

    name = label['name']
    referenced_images = label['referenced_images']

    game_resolution_width = 1920 #todo get info from file
    game_resolution_height = 1080 #todo get info from file

    with open(os.path.join(path_to_game_directory,'gui.rpy')) as f:
        scriptlines = f.readlines()
        for line in scriptlines:
            if 'gui.init(' in line:
                resolution = line.replace('gui.init(','').replace(')','').replace('\n','').split(',')
                game_resolution_width = int(resolution[0].strip())
                game_resolution_height = int(resolution[1].strip())

    for referenced_image in referenced_images:
        for file in os.listdir(os.path.join(path_to_game_directory, 'images')):
            if not ".ps1" in file:
                if referenced_image in file:
                    image = Image.open(os.path.join(path_to_game_directory,'images',file))
                    width, height = image.size
                    if width != game_resolution_width or height != game_resolution_height:
                        result.append("Image " + referenced_image + " that was called in label '" + label['name'] + "' has a different resolution("+str(width)+"x"+str(height)+") from the game ("+ str(game_resolution_width)+"x"+str(game_resolution_height)+") and will not display correctly.")
    return remove_duplicates_from_list(result)

def get_referenced_sounds_that_dont_exist(path_to_game_directory,label,defined_sounds):
    result = []
    if os.path.exists(os.path.join(path_to_game_directory, 'audio', 'voice')):
        sound_files = [f for f in os.listdir(os.path.join(path_to_game_directory, 'audio')) if os.path.isfile(os.path.join(path_to_game_directory, 'audio', f))] + [f for f in os.listdir(os.path.join(path_to_game_directory, 'audio','voice')) if os.path.isfile(os.path.join(path_to_game_directory, 'audio','voice', f))]

        #todo two possible cases here: sound file doesnt exist or sound file is called by name and has not been initialized with Define
        name = label['name']
        referenced_sounds = label['referenced_music']
        for referenced_sound in referenced_sounds:
            if referenced_sound and not referenced_sound+".mp3" in sound_files:
                #todo check for images of different capitalization.
                #todo check for images that are split by either dashes or underscores
                #todo figure something out for those stupid multi-word file names. (fuck you renpy, whyyyyy?!)
                result.append("Sound " + referenced_sound + ".mp3 that was referenced in label '" + label['name'] + "' could not be found in audio folder.")
        #todo
    else:
        name = label['name']
        referenced_sounds = label['referenced_music']
        for referenced_sound in referenced_sounds:
            result.append("Sound " + referenced_sound + ".mp3 that was referenced in label '" + label['name'] + "' could not be found in audio folder.")

    return result

def get_referenced_characters_that_dont_exist(label,defined_characters):
    result = []
    name = label['name']
    referenced_characters = label['referenced_characters']
    for referenced_character in referenced_characters:
        if not referenced_character in defined_characters and not 'voice' in referenced_character:
            result.append("The character of the name " + referenced_character + " was referenced in label '" + label['name'] + "' but the character has never been defined using 'define x = Character()'.")
    #todo check for capitalization issues
    return result

def get_referenced_variables_that_dont_exist(label,defined_variables):
    result = []
    name = label['name']
    referenced_variables = label['referenced_variables']
    for referenced_variable in referenced_variables:
        defined_variables = [re.sub(r'=.*?$','',x).strip() for x in defined_variables]
        just_the_variable_name = re.sub(r'=.*?$','',referenced_variable).strip()
        if not just_the_variable_name in defined_variables:
            result.append("A variable of the name " + referenced_variable + " was referenced in label '" + label['name'] + "', but the variable has never been defined using 'default'.")
    #todo
    return result

def get_all_scenes_without_background_images(file,defined_images):
    result = []
    for label in get_all_labels_from_script_files(file):
        name = label['name']
        referenced_variables = label['referenced_variables']
        for referenced_variable in referenced_variables:
            if not referenced_variable in defined_variables:
                result.append("A variable of the name " + referenced_variable + " was referenced in " + file + "\\" + label['name'] + " but the variable has never been defined using 'default'.")
    #todo
    return result

def get_all_short_scenes(file):
    result = []
    for label in get_all_labels_from_script_files(file):
        name = label['name']
        referenced_variables = label['referenced_variables']
        for referenced_variable in referenced_variables:
            if not referenced_variable in defined_variables:
                result.append("A variable of the name " + referenced_variable + " was referenced in " + file + "\\" + label['name'] + " but the variable has never been defined using 'default'.")
    #todo
    return result

def get_all_menus_with_just_one_option(file,defined_sounds):
    result = []
    for label in get_all_labels_from_script_files(file):
        name = label['name']
        referenced_variables = label['referenced_variables']
        for referenced_variable in referenced_variables:
            if not referenced_variable in defined_variables:
                result.append("A variable of the name " + referenced_variable + " was referenced in " + file + "\\" + label['name'] + " but the variable has never been defined using 'default'.")
    #todo
    return result

def get_all_empty_say_statements(file,defined_characters):
    result = []
    for label in get_all_labels_from_script_files(file):
        name = label['name']
        referenced_variables = label['referenced_variables']
        for referenced_variable in referenced_variables:
            if not referenced_variable in defined_variables:
                result.append("A variable of the name " + referenced_variable + " was referenced in " + file + "\\" + label['name'] + " but the variable has never been defined using 'default'.")
    #todo
    return result

def get_all_unused_music(path_to_game_directory,defined_music):
    result = []
    if os.path.exists(os.path.join(path_to_game_directory,'audio')) and os.path.exists(os.path.join(path_to_game_directory,'audio', 'voice')):
        sound_files = os.listdir(os.path.join(path_to_game_directory,'audio'))
        voice_files = os.listdir(os.path.join(path_to_game_directory,'audio','voice'))
        for sound_file in sound_files:
            if os.path.isfile(sound_file):
                if not sound_file in defined_music:
                    result.append("An audio file with the name " + sound_file + " exists in audio directory but is not used anywhere in the game files. If this is intended you can safe disk space by cleaning this up, or reference the file in the code if you want to use it.")
        for voice_file in voice_files:
            if os.path.isfile(voice_file):
                if not voice_file in defined_music:
                    result.append("A voice file with the name " + voice_file + " exists in audio/voice directory but is not used anywhere in the game files. If this is intended you can safe disk space by cleaning this up, or reference the file in the code if you want to use it.")
    return result

def get_all_unused_variables(defined_variables,referenced_variables):
    result = []
    export = []
    for variable in defined_variables:
        if not variable in referenced_variables:
            result.append("A variable with the name " + variable + " was defined but is not used anywhere in the game files.")
    return list(dict.fromkeys(result))


def get_all_unused_images(path_to_game_directory,referenced_images):
    result = []
    export = []
    ignore_these_files = [
        'black.webp',
        'load_hover.webp',
        'load_idle.webp',
        'start_hover.webp',
        'start_idle.webp',
        'options_hover.webp',
        'options_idle.webp',
        'patreon_idle.webp',
        'patreon_idle.webp',
        'main_menu.webp',
        'game_menu.webp',
    ]

    for image_file in os.listdir(os.path.join(path_to_game_directory,'images')):
        image_file = re.sub(r'\..*?$','',image_file)
        if not image_file in referenced_images and not "main_menu" in image_file and not image_file in ignore_these_files and not ".mp4" in image_file:
            export.append(image_file)
            #result.append("An image file with the name " + image_file + " exists in image directory but is not used anywhere in the game files. If this is intended you can safe disk space by cleaning this up, or reference the file in the code if you want to use it.")

    export_file_path = os.path.join(path_to_game_directory,'images',"remove_unused_images.ps1")
    with open(export_file_path,'w+') as f:
        for item in export:
            f.writelines("if (Test-Path \".\\"+item+".png\") {Remove-Item \".\\"+item+".png\"}\n")
            f.writelines("if (Test-Path \".\\"+item+".jpg\") {Remove-Item \".\\"+item+".jpg\"}\n")
            f.writelines("if (Test-Path \".\\"+item+".webp\") {Remove-Item \".\\"+item+".jpg\"}\n")
    return list(dict.fromkeys(result))

def remove_duplicates_from_list(list_to_dedupe):
    if len(list_to_dedupe) == 0:
        return list_to_dedupe
    return list(dict.fromkeys(list_to_dedupe))

def get_all_unused_characters(referenced_characters):
    result = []
    #todo get sound files from folder and report all that are not defined

            # if not referenced_variable in defined_variables:
            #     result.append("A variable of the name " + referenced_variable + " was referenced in " + file + "\\" + label['name'] + " but the variable has never been defined using 'default'.")
    #todo
    return result

def get_all_images_davailable_in_multiple_formats(folder_path):
    result = []
    #todo check image names and return those defined twice
    #todo
    return result

def remove_trailing_lines_with_less_indentation(option_lines):
    result = []
    first_line = option_lines[0]
    first_line_indentation = len(first_line) - len(first_line.lstrip())
    for line in reversed(option_lines):
        current_line_indentation = len(line) - len(line.lstrip())
        if not current_line_indentation < first_line_indentation:
            result.append(line)
    return list(reversed(result))

def get_all_menus_without_variable_content_or_jumps(label):
    result = []
    name = label['name']
    menus = label['menus']
    # for menu in menus:
    #     for option in menu['options']:
    #         option_lines = option['option_text'].split('\n')
    #         option_lines = [line for line in option_lines if line.strip() != ""]
    #         option_lines = remove_trailing_lines_with_less_indentation(option_lines)
    #         if not 'jump ' in option_lines[len(option_lines)-1] and not not 'call ' in option_lines[len(option_lines)-1]:
    #             if not re.match(r'.*?\$\w*?=',option):
    #                 if not re.match(r'.*?scene\s.*?',option) and not re.match(r'.*?show\s.*?',option):
    #                     result.append("A menu choice with the name " + option["option_name"] + " has been declared in label '" + label['name'] + "' but the choice does not have any jumps, variable declaration or image changes. This can be a valid choice but is usually an error'.")
    #todo
    return result

def get_all_variables_not_following_pattern(defined_variables):
    result = []
    found_pattern = False
    pattern = ''
    try:
        random_variable = random.choice(defined_variables)
        possible_patterns = [
            {"rule_description":"Variables contain underscores","pattern":r'^.*?_'},
        ]
        for possible_pattern in possible_patterns:
            pattern = possible_pattern["pattern"]
            if re.match(pattern,random_variable):
                matched_count = 0
                non_matched_count = 0
                for variable in defined_variables:
                    if re.match(pattern,variable):
                        matched_count +=1
                    else:
                        non_matched_count += 1
                if matched_count > len(defined_variables)/2:
                    found_pattern = True
            for variable in defined_variables:
                if not re.match(pattern,variable):
                    result.append("A pattern for variable naming has been detected for over half of all variables: (" + possible_pattern["rule_description"] + ") but the variable '" + variable + "' does not follow that pattern. Feel free to ignore this warning if this is intended")

    except Exception as e:
        pass
    return list(dict.fromkeys(result))

def get_all_characters_not_following_pattern(defined_characters):
    result = []
    #todo
    return result


def get_referenced_jump_statements_that_dont_exist(label,defined_scenes,defined_menus):
    result = []
    name = label['name']
    referenced_jumps = label['referenced_jumps']
    jump_found = False
    for referenced_jump in referenced_jumps:
        for defined_menu in defined_menus:
            if defined_menu == referenced_jump:
                jump_found = True
        for defined_scene in defined_scenes:
            if defined_scene['name'] == referenced_jump:
                jump_found = True

        if not jump_found:
            result.append("Jump statement leading to " + referenced_jump + " was referenced in label '" + label['name'] + "' but the label (or named menu) doesn't exist.")

    return result

def get_all_existing_images_in_folder(path):
    result = []
    for file in os.listdir(os.path.join(path, 'images')):
        if '.png' in file or '.jpg' in file or '.webp' in file:
            result.append(file)
    return result

def get_all_existing_music_in_folder(path):
    result = []
    if os.path.exists(os.path.join(path, 'audio')):
        for file in os.listdir(os.path.join(path, 'audio')):
            if '.wav' in file or '.mp3' in file or '.ogg' in file:
                result.append(file)
    return result




def check_for_errors(all_defined_labels, path_to_game_directory,all_defined_characters,all_defined_variables,all_defined_menus,all_defined_music,all_defined_images):
    result = []
    existing_images_in_folder = get_all_existing_images_in_folder(path_to_game_directory)
    for label in all_defined_labels:
        result.extend(get_referenced_images_that_dont_exist(label,existing_images_in_folder))
        result.extend(get_referenced_images_that_dont_match_game_resolution(label,path_to_game_directory))
        result.extend(get_referenced_characters_that_dont_exist(label,all_defined_characters))

        result.extend(get_referenced_sounds_that_dont_exist(path_to_game_directory,label,all_defined_music))
        result.extend(get_referenced_variables_that_dont_exist(label,all_defined_variables))
        result.extend(get_referenced_jump_statements_that_dont_exist(label,all_defined_labels,all_defined_menus))
        result.extend(get_all_empty_voice_files(all_script_files))
        result.extend(get_all_text_without_voice_files(all_script_files))
    #todo
    return remove_duplicates_from_list([x for x in result if x])


def check_for_warnings(all_defined_labels, path_to_game_directory,all_defined_characters,all_defined_variables,all_defined_menus,all_defined_music,all_defined_images,all_referenced_images):
    result = []

    for label in all_defined_labels:
        #todo result.extend(get_all_scenes_without_background_images(file,defined_images))
        #todo result.extend(get_all_short_scenes(file))
        #todo result.extend(get_all_menus_with_just_one_option(file,defined_sounds))
        #todo result.extend(get_all_empty_say_statements(file,defined_characters))
        #todo result.extend(get_all_unused_variables(file,defined_variables))
        #result.extend(get_all_unused_characters(file,defined_labels,defined_menus))
        #todo: add check for disallowed file types

        #todo result.extend(get_all_images_davailable_in_multiple_formats(path))
        result.extend(get_all_menus_without_variable_content_or_jumps(label))
        result.extend(get_all_variables_not_following_pattern(all_defined_variables))
        result.extend(get_all_characters_not_following_pattern(all_defined_characters))
        #todo report all labels that have todo comments in them
    result.extend(get_all_unused_music(path_to_game_directory,all_defined_music))
    result.extend(get_all_unused_images(path_to_game_directory,all_referenced_images))
    result.extend(get_all_unused_variables(all_defined_variables,all_referenced_variables))
    result = [x for x in result if x]
    return  remove_duplicates_from_list(result)

def check_for_stats(all_defined_labels, path_to_game_directory,all_defined_characters,all_defined_variables,all_defined_menus,all_defined_music,all_defined_images,all_referenced_images, all_referenced_variables, all_referenced_jumps, all_referenced_music,all_referenced_characters,all_existing_images_in_folder,all_existing_music_in_folder,errors,warnings):
    result = []
    result.append("Number of errors: "+str(len(remove_duplicates_from_list(errors))))
    result.append("Number of warnings: "+str(len(remove_duplicates_from_list(warnings))))
    result.append("Number of image definitions using 'image x = ' notation: "+str(len(all_defined_images)))
    result.append("Number of images inside image folder: "+str(len(remove_duplicates_from_list(all_existing_images_in_folder))))
    result.append("Number of (unique) images referenced: "+str(len(remove_duplicates_from_list(all_referenced_images))))
    result.append("Number of (unique) variables referenced: "+str(len(remove_duplicates_from_list(all_referenced_variables))))
    result.append("Number of (unique) characters referenced: "+str(len(remove_duplicates_from_list(all_referenced_characters))))
    result.append("Number of (unique) audio files referenced: "+str(len(remove_duplicates_from_list(all_referenced_music))))
    result.append("Number of labels: "+str(len(all_defined_labels)))
    result.append("Number of menus: "+str(len(remove_duplicates_from_list(all_defined_menus))))
    result.append("Number of menus: "+str(len(remove_duplicates_from_list(all_defined_menus))))

    result = [x for x in result if x]
    return  remove_duplicates_from_list(result)

def get_all_referenced_images(all_defined_labels,all_script_files):
    result = []
    for label in all_defined_labels:
        result.extend(label["referenced_images"])
    print('images before extended search: ' + str(len(result)))
    for script_file in all_script_files:
        if '.webp"' in script_file:
            for line in script_file.split('\n'):
                try:
                    image_name = re.search(r'.*?"(.*?)\.webp"',line).group(1)
                    result.append(image_name)
                except Exception as e:
                    pass
    print('images after extended search: ' + str(len(result)))

    return list(dict.fromkeys([x for x in result if x]))

def get_all_referenced_variables(all_defined_labels):
    result = []
    for label in all_defined_labels:
        result.extend(label["referenced_variables"])
    return list(dict.fromkeys([x for x in result if x]))

def get_all_referenced_jumps(all_defined_labels):
    result = []
    for label in all_defined_labels:
        result.extend(label["referenced_jumps"])
    return list(dict.fromkeys([x for x in result if x]))

def get_all_referenced_music(all_defined_labels):
    result = []
    for label in all_defined_labels:
        result.extend(label["referenced_music"])
    return list(dict.fromkeys([x for x in result if x]))

def get_all_referenced_characters(all_defined_labels):
    result = []
    for label in all_defined_labels:
        result.extend(label["referenced_characters"])
    return list(dict.fromkeys([x for x in result if x]))




def export_results(stats,errors,warnings):
    export_file_path = os.path.join(os.getcwd(),"python_debugger_export.txt")
    with open(export_file_path,'w+') as f:
        f.writelines('\n\n'+'Stats: ')
        f.writelines('\n'.join(stats))
        f.writelines('\n\n'+'Errors: ')
        f.writelines('\n'.join(errors))
        f.writelines('\n\n'+'warnings: ')
        f.writelines('\n'.join(warnings))
    # os.startfile(export_file_path)
    #subprocess.call(['cmd.exe', '/c', export_file_path])
if __name__ == "__main__":
    errors = []
    warnings = []
    stats = []
    path_to_game_directory = os.path.join(os.getcwd(),'game')

    all_script_filepaths = get_all_script_filepaths(path_to_game_directory)
    all_script_files = get_all_script_files_clean_text(all_script_filepaths)
    all_script_files_plain_text = [get_plain_text_from_script_file(x) for x in all_script_filepaths]
    all_defined_labels = get_all_labels_from_script_files(all_script_files_plain_text)
    all_defined_images = get_all_defined_image_names(all_script_files)
    all_defined_music = get_all_defined_music(all_script_files)
    all_defined_characters = get_all_defined_characters(all_script_files)
    all_defined_variables = get_all_defined_variables(all_script_files)
    all_defined_menus = get_all_defined_menus(all_script_files)
    all_existing_images_in_folder = get_all_existing_images_in_folder(path_to_game_directory)
    all_existing_music_in_folder = get_all_existing_music_in_folder(path_to_game_directory)
    all_referenced_images = get_all_referenced_images(all_defined_labels,all_script_files_plain_text)
    all_referenced_variables = get_all_referenced_variables(all_defined_labels)
    all_referenced_jumps = get_all_referenced_jumps(all_defined_labels)
    all_referenced_music = get_all_referenced_music(all_defined_labels)
    all_referenced_characters = get_all_referenced_characters(all_defined_labels)


    errors = check_for_errors(all_defined_labels, path_to_game_directory,all_defined_characters,all_defined_variables,all_defined_menus,all_defined_music,all_defined_images)

    warnings = check_for_warnings(all_defined_labels, path_to_game_directory,all_defined_characters,all_defined_variables,all_defined_menus,all_defined_music,all_defined_images,all_referenced_images)

    stats = check_for_stats(all_defined_labels, path_to_game_directory,all_defined_characters,all_defined_variables,all_defined_menus,all_defined_music,all_defined_images,all_referenced_images, all_referenced_variables, all_referenced_jumps, all_referenced_music,all_referenced_characters,all_existing_images_in_folder,all_existing_music_in_folder,errors,warnings)
    export_results(stats,errors,warnings)
