def printing_map(character):
    default_map = [" + + + + + + + + + C", " + + + + + + + + + +", " + + H + + + + H + +", " + + + + + + + + + +",
                   " + + + + + + + + + +", " + + + + + M + + + +", " + + + + + + + + + +", " + + H + + + + H + +",
                   " + + + + + + + + + +", " C + + + + + + + + B"]
    current_map = default_map[:]
    for line in current_map:
        target_row = current_map[character[0]["X"]].split(' ')
        target_row[character[0]["Y"]] = 'U'
        current_map[character[0]["X"]] = " ".join(target_row)
        print(line)


# printing_map({"X": 2, "Y": 3})
