# write your code here
def get_cell(text):
    cell = []
    for item in text:
        cell.append(item)
    return cell


def print_cells(cells):
    print("---------")
    for row in cells:
        temp = "| "
        for col in row:
            temp = temp + col + " "
        temp = temp + "|"
        print(temp)
    print("---------")


def validate(coordinates):
    numbers = []
    for item in coordinates:
        if not item.isdigit():
            print("You should enter numbers!")
            return []

        num = int(item)
        if num < 1 or num > 3:
            print("Coordinates should be from 1 to 3!")
            return []
        numbers.append(num)

    if len(numbers) == 2:
        cell = cells[numbers[0] - 1][numbers[1] - 1]
        if cell == "X" or cell == "O":
            print("This cell is occupied! Choose another one!")
            return []
    return numbers


def check_win(cells):
    if cells[0][0] == cells[0][1] and cells[0][1] == cells[0][2]:
        return True
    elif cells[1][0] == cells[1][1] and cells[1][1] == cells[1][2]:
        return True
    elif cells[2][0] == cells[2][1] and cells[2][1] == cells[2][2]:
        return True
    elif cells[0][0] == cells[1][1] and cells[1][1] == cells[2][2]:
        return True
    elif cells[0][2] == cells[1][1] and cells[1][1] == cells[2][0]:
        return True
    elif cells[0][0] == cells[1][0] and cells[1][0] == cells[2][0]:
        return True
    elif cells[0][1] == cells[1][1] and cells[1][1] == cells[2][1]:
        return True
    elif cells[0][2] == cells[1][2] and cells[1][2] == cells[2][2]:
        return True
    return False


def check_win_with(cells, player):
    if player == cells[0][0] and cells[0][0] == cells[0][1] and cells[0][1] == \
            cells[0][2]:
        return True
    elif player == cells[1][0] and cells[1][0] == cells[1][1] and cells[1][1] == \
            cells[1][2]:
        return True
    elif player == cells[2][0] and cells[2][0] == cells[2][1] and cells[2][1] == \
            cells[2][2]:
        return True
    elif player == cells[0][0] and cells[0][0] == cells[1][1] and cells[1][1] == \
            cells[2][2]:
        return True
    elif player == cells[0][2] and cells[0][2] == cells[1][1] and cells[1][1] == \
            cells[2][0]:
        return True
    elif player == cells[0][0] and cells[0][0] == cells[1][0] and cells[1][0] == \
            cells[2][0]:
        return True
    elif player == cells[0][1] and cells[0][1] == cells[1][1] and cells[1][1] == \
            cells[2][1]:
        return True
    elif player == cells[0][2] and cells[0][2] == cells[1][2] and cells[1][2] == \
            cells[2][2]:
        return True
    return False


def check_win_game(cells):
    if check_win_with(cells, "X") and check_win_with(cells, "O") or abs(
            count(cells, "X") - count(cells, "O")) > 1:
        print("Impossible")
        return -1
    elif check_win(cells) == False and check_empty(cells) == False:
        print("Draw")
        return 0
    elif check_win(cells) == False and check_empty(cells) == True:
        # print("Game not finished")
        return -1
    elif check_win(cells) == True and check_win_with(cells, "X"):
        print("X wins")
        return 1
    elif check_win(cells) == True and check_win_with(cells, "O"):
        print("O wins")
        return 1


def check_empty(cells):
    for row in cells:
        for col in row:
            if col != "X" and col != "O":
                return True
    return False


def count(cells, player):
    count = 0
    for row in cells:
        for col in row:
            if col == player:
                count += 1
    return count


# print("Enter cells:")
# text = str(input())
text = "_________"
length = len(text)
cells = []
cells.append(get_cell(text[0: 3]))
cells.append(get_cell(text[3: 6]))
cells.append(get_cell(text[6: 9]))
print_cells(cells)

playing = True
set_x = True

while playing:
    numbers = []
    while len(numbers) < 2:
        print("Enter the coordinates:")
        text = str(input()).strip()
        coordinates = text.split()
        numbers = validate(coordinates)
    if set_x:
        cells[numbers[0] - 1][numbers[1] - 1] = "X"
        set_x = False
    else:
        cells[numbers[0] - 1][numbers[1] - 1] = "O"
        set_x = True
    print_cells(cells)

    result = check_win_game(cells)
    if result == 1 or result == 0:
        playing = False
        break
