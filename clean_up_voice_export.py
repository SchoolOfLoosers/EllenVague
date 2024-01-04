from elevenlabs import generate, play, set_api_key, save
import os

def main():
    elevenlabs_api_key = ""
    with open(os.path.join(os.getcwd(), "elevenlabs_api_key.txt"), "r") as f:
        set_api_key(f.readline().strip())
    all_input_lines = []
    all_dialog_lines = []
    with open(os.path.join(os.getcwd(), "dialogue.tab"), "r") as f:
        all_input_lines = f.readlines()
        all_input_lines.pop(0)

    for line in all_input_lines:
        dialog_line = line.split("\t")
        all_dialog_lines.append(dialog_line)
        savepath = os.path.join(os.getcwd(), "game","audio", "voice",dialog_line[0]+".mp3")
        if not os.path.exists(savepath):
            print("Generating file ID: "+ dialog_line[0] + ", Speaker: "+dialog_line[1]+ ", text: " + dialog_line[2])
            speaker = dialog_line[1]
            if speaker == "mc" or speaker == "na" or speaker == "":
                speaker = "Kimber"
            if speaker == "s":
                speaker = "Stacey"
            if speaker == "b":
                speaker = "Jessie"
            if speaker == "j":
                speaker = "Michael"
            if speaker == "p":
                speaker = "Stacey"

            audio = generate(
                text=dialog_line[2],
                voice=speaker,
                model="eleven_multilingual_v2"
            )
            audio.hex
            save(audio, savepath)

if __name__ == '__main__':
    main()