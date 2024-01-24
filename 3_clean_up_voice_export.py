from elevenlabs import generate, play, set_api_key, save
import os
import shutil
import re

def main():
    elevenlabs_api_key = ""
    with open(os.path.join(os.getcwd(), "elevenlabs_api_key.txt"), "r") as f:
        set_api_key(f.readline().strip())
    all_input_lines = []
    all_dialog_lines = []
    all_dialog_ids = []
    with open(os.path.join(os.getcwd(), "dialogue.tab"), "r") as f:
        all_input_lines = f.readlines()
        all_input_lines.pop(0)


    for line in all_input_lines:
        dialog_line = line.split("\t")
        all_dialog_lines.append(dialog_line)
        all_dialog_ids.append(dialog_line[0])
        savepath = os.path.join(os.getcwd(), "game","audio", "voice",dialog_line[0]+".mp3")

        #this portion first checks if a file ending with _1 / _2 etc already exists without the suffix --> duplicate voice lines aren't generated twice but rather copied to save API calls.
        if (not os.path.exists(savepath)):
            digit = None
            if re.search(r"(_\d).mp3$", savepath):
                digit = re.search(r"(_\d).mp3$", savepath).group(1)
            if digit:
                if os.path.exists(savepath.replace(digit+".mp3", ".mp3")):
                    shutil.copy(savepath.replace(digit+".mp3", ".mp3"),savepath)
            else:
                print("Generating file ID: "+ dialog_line[0] + ", Speaker: "+dialog_line[1]+ ", text: " + dialog_line[2])
                speaker = dialog_line[1]
                if speaker == "mc" or speaker == "na" or speaker == "":
                    speaker = "Kimber"
                elif speaker == "s":
                    speaker = "Stacey"
                elif speaker == "b":
                    speaker = "Jessie"
                elif speaker == "j":
                    speaker = "Michael"
                elif speaker == "p":
                    speaker = "Stacey"
                elif speaker == "y":
                    speaker = "Bill"
                elif speaker == "r":
                    speaker = "Fin"
                elif speaker == "m":
                    speaker = "Rachel"
                elif speaker == "man":
                    speaker = "Clyde"
                elif speaker == "k":
                    speaker = "Grace"
                elif speaker == "shadow":
                    speaker = "DaveGruff"
                elif speaker == "e":
                    speaker = "Brian"
                elif speaker == "c":
                    speaker = "Nora"
                elif speaker == "v":
                    speaker = "Roshni"
                elif speaker == "ba":
                    speaker = "Adam"
                elif speaker == "w":
                    speaker = "Ava"

                audio = generate(
                    text=dialog_line[2],
                    voice=speaker,
                    model="eleven_multilingual_v2"
                )
                audio.hex
                save(audio, savepath)
    #remove old voice files that are superseded by new IDs
    # for soundfile in os.listdir(os.path.join(os.getcwd(), "game","audio","voice")):
    #     if soundfile.split('.')[0] not in all_dialog_ids:
    #         os.remove(os.path.join(os.getcwd(), "game","audio","voice",soundfile))

if __name__ == '__main__':
    main()