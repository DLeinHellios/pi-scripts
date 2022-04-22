colors = {
        "blank": [0,0,0],
        "red1": [220,0,0],
        "orange1": [160,25,0],
        "yellow1": [180,40,0],
        "green1": [40,150,0],
        "blue1": [0,25,180],
        "indigo1": [30,0,170],
        "violet1": [150,0,60],
        }

sequences = {
        "rainbow1": [
            colors["red1"],
            colors["orange1"],
            colors["yellow1"],
            colors["green1"],
            colors["blue1"],
            colors["indigo1"],
            colors["violet1"],
            ],
        "oranges": [
            colors["orange1"],
            [170,35,0],
            colors["yellow1"],
            [170,35,0],
            ]
        }


if __name__ == "__main__":
    print("----------------------------")
    print("fx/colors.py\n")
    print (f"colors:\n{' | '.join(colors.keys())}\n")
    print (f"sequences:\n{' | '.join(sequences.keys())}\n")
    print("----------------------------")