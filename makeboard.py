import random


def generate_room_type():
    random_number = random.randint(0, 100)
    if 0 <= random_number <= 45:
        return "Empty Room"
    elif 45 <= random_number <= 59:
        return "Treasure Room"
    elif 60 <= random_number <= 100:
        return "Monster Room"



def make_board(row, column):
    board = {(k, v): generate_room_type() for k in range(row) for v in range(column)}
    board[(0, 0)] = "Empty Room"
    board[(0, 9)] = "Chest room"
    board[(9, 0)] = "Chest room"
    board[(9, 9)] = "Boss room"
    board[(2, 2)] = "Health room"
    board[(2, 7)] = "Health room"
    board[(7, 2)] = "Health room"
    board[(7, 7)] = "Health room"
    board[(5, 5)] = "Elite room"

    return board


def main():
    # rows = input("Enter the amount of rows:")
    # columns = input("Enter the amount of columns:")
    print(make_board(10, 10))


if __name__ == '__main__':
    main()
