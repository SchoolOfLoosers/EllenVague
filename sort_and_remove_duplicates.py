from pathlib import Path

file = Path("./game/declarations/choices.rpy")
uniqlines = set(open(file).readlines())
file.write_text(
    "".join(
        sorted(
            uniqlines
        )
    )
)
file = Path("./game/declarations/characters.rpy")
uniqlines = set(open(file).readlines())
file.write_text(
    "".join(
        sorted(
            uniqlines
        )
    )
)