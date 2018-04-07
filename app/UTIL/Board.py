import random
class board:
    size = 0
    board = []


    def __init__(self, size):
        try:
            self.size = int(size)
        except ValueError as err:
            try:
                self.size= int(input("Enter size of board, press other key to exit.\n"))
            except ValueError as err:
                print("Exiting 2048")
                exit(0)
        self.board = [[0]* self.size for _ in range(self.size)]
        self.generate_number()

    def print_board(self):
        s = [[str(e) for e in row] for row in self.board]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))

    def performOperation(self,action):
        if action==1:self.move_upword()
        elif action==2:self.move_leftside()
        elif action==3:self.move_rightside()
        elif action==4:self.move_downword()
        self.generate_number()


    def move_downword(self):
        for j in range(self.size):
            for i in range(self.size-1):
                if self.board[i][j]== self.board[i+1][j] and self.board[i][j]!=0:
                    self.board[i + 1][j]*=2
                    self.board[i][j]=0
                    while i >0:
                        self.board[i][j] = self.board[i - 1][j]
                        i-=1
                    self.board[i][j] =0
                elif self.board[i][j]!=0 and self.board[i+1][j]==0:
                    self.board[i + 1][j] = self.board[i][j]
                    self.board[i][j] = 0
                    while i >0:
                        self.board[i][j] = self.board[i - 1][j]
                        i-=1
                    self.board[i][j] =0


    def move_upword(self):
        for j in range(0,self.size):
            for i in reversed(range(1,self.size)):
                if self.board[i][j]== self.board[i-1][j]and self.board[i][j]!=0:
                    self.board[i - 1][j]*=2
                    self.board[i][j]=0
                    while i <self.size-1:
                        self.board[i][j] = self.board[i + 1][j]
                        i+=1
                    self.board[i][j] =0
                elif self.board[i][j]!=0 and self.board[i-1][j]==0:
                    self.board[i - 1][j] = self.board[i][j]
                    self.board[i][j] = 0
                    while i <self.size-1:
                        self.board[i][j] = self.board[i + 1][j]
                        i+=1
                    self.board[i][j] =0

    def move_rightside(self):
        for i in range(self.size):
            for j in range(self.size-1):
                if self.board[i][j]== self.board[i][j+1]and self.board[i][j]!=0:
                    self.board[i][j+1]*=2
                    self.board[i][j]=0
                    while j >0:
                        self.board[i][j] = self.board[i][j-1]
                        j-=1
                    self.board[i][j] =0
                elif self.board[i][j]!=0 and self.board[i][j+1]==0:
                    self.board[i][j+1] = self.board[i][j]
                    self.board[i][j] = 0
                    while j >0:
                        self.board[i][j] = self.board[i][j-1]
                        j-=1
                    self.board[i][j] =0


    def move_leftside(self):
        for i in range(self.size):
            for j in range(self.size-1,0,-1):
                if self.board[i][j]== self.board[i][j-1]and self.board[i][j]!=0:
                    self.board[i][j-1]*=2
                    self.board[i][j]=0
                    while j <self.size-1:
                        self.board[i][j] = self.board[i ][j+1]
                        j+=1
                    self.board[i][j] =0
                elif self.board[i][j]!=0 and self.board[i][j-1]==0:
                    self.board[i][j-1] = self.board[i][j]
                    self.board[i][j] = 0
                    while j <self.size-1:
                        self.board[i][j] = self.board[i ][j+1]
                        j+=1
                    self.board[i][j] =0




    def generate_number(self):
        numbers=[2]*15
        numbers.extend([4]*4)
        numbers.extend([8]*1)

        i,j=random.randint(0,self.size-1),random.randint(0,self.size-1)
        if self.board[i][j]==0:
            self.board[i][j]=random.choice(numbers)
            self.print_board()
        elif any(0 in sublist for sublist in self.board):
            self.generate_number()
        else:
            print("You Lost")
            exit(0)