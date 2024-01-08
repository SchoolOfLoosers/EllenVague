from pathlib import Path

file = Path("./game/declarations/choices.rpy")
uniqlines = set(open(file).readlines())
file.write_text(
    "".join(
        sorted(
            uniqlines
        )
    ).replace("Falsedefault","False\ndefault")
)
file = Path("./game/declarations/characters.rpy")
uniqlines = set(open(file).readlines())
file.write_text(
    "".join(
        sorted(
            uniqlines
        )
    ).replace("Falsedefault","False\ndefault")
)