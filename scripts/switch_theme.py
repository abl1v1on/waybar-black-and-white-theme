from pathlib import Path


def main() -> None:
    path_to_style = Path(__file__).parent.parent / "style.css"

    with open(path_to_style, mode="r") as file:
        lines = file.readlines()

    for idx, line in enumerate(lines):
        if line.startswith("@define-color main-text-color"):
            text_idx = idx
            text_color = line.split(" ")[-1][:-2]
        elif line.startswith("@define-color main-bg-color"):
            bg_idx = idx
            bg_color = line.split(" ")[-1][:-2]

    lines[text_idx] = f"@define-color main-text-color {bg_color};\n"
    lines[bg_idx] = f"@define-color main-bg-color {text_color};\n"

    with open(path_to_style, mode="w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    main()
