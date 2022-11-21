import random


def generate_room_type():
    random_number = random.randint(0, 100)
    if 0 <= random_number <= 50:
        return "Empty Room"
    elif 51 <= random_number <= 75:
        return "Treasure Room"


def make_board(row, column):
    board = {(k, v): generate_room_type() for k in range(row) for v in range(column)}
    # for k in range(row):
    #     for v in range(column):
    #         board.update({(k, v): generate_room_type()})
    return board


def main():
    # rows = input("Enter the amount of rows:")
    # columns = input("Enter the amount of columns:")
    print(make_board(10, 10))


if __name__ == '__main__':
    main()
