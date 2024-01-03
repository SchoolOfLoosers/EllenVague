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
        print("ID: "+ dialog_line[0] + ", Speaker: "+dialog_line[1]+ ", text: " + dialog_line[2])
        if not os.path.isfile(os.path.join(os.getcwd(), "audio", "voice",dialog_line[0]+".mp3")):
            speaker = dialog_line[1]
            if speaker == "mc" or speaker == "na":
                speaker = "Kimber"

            audio = generate(
                text=dialog_line[2],
                voice=speaker,
                model="eleven_multilingual_v2"
            )
            audio.hex
            savepath = os.path.join(os.getcwd(), "game","audio", "voice",dialog_line[0]+".mp3")
            save(audio, savepath)

if __name__ == '__main__':
    main()