
from UTIL.Board import board
board=board(input("Welcome to 2048!\nEnter size of board\n"))
while True:
    try:
      action=int(input("Press 1 for ↑\tPress 2 for  ←\tPress 3 for  →\tPress 4 for  ↓\t"))
      if action not in [1,2,3,4]:raise ValueError
      else:board.performOperation(action)
    except ValueError as err:
        try:
            action=int(input("You have entered wrong value.\nPress 1 for ↑\tPress 2 for  ←\tPress 3 for  →\tPress 4 for  ↓,press other key to exit.\t"))
            if action not in [1, 2, 3, 4]:
                raise ValueError
            else:
                board.performOperation(action)
        except ValueError as err:
            print("Exiting 2048")
            exit(0)