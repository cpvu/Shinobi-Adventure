def printing_map(character):
    default_map = [" + + + + + + + + + C", " + + + + + + + + + +", " + + H + + + + H + +", " + + + + + + + + + +",
                   " + + + + + + + + + +", " + + + + + M + + + +", " + + + + + + + + + +", " + + H + + + + H + +",
                   " + + + + + + + + + +", " C + + + + + + + + B"]
    current_map = default_map[:]
    for line in current_map:
        target_row = current_map[character["X"]].split(' ')
        target_row[character["Y"]] = 'U'
        current_map[character["X"]] = " ".join(target_row)
        print(line)


# printing_map({"X": 2, "Y": 3})
