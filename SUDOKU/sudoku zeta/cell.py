# IF YOU THINK ABOUT IT,
# FOR HUMAN TO SOLVE THE PUZZLE, HE WOULD MARK CANDIDATE NUMBERS IN EACH BOX
# SO IT WOULD BE BEST TO CREATE A CLASS CELL WITH DEFAULT ATTRIBUTE CANDIDATES [1 TO 9]
from collections import Counter


class Cell:
    puz=[range(9) for i in range(9)]

    @staticmethod
    def getpuzzle(p):
        Cell.puz=p

    def __init__(self, x, y):  # X,Y WILL BE NEEDED TO IDENTIFY THE BOX'S LOCATION TO FIGURE OUT ITS ROW, COLUMN, SQR
        if Cell.puz[x][y] == 0:  # SINCE EVERY ELEMENT OF PUZZLE GETS ASSOCIATED WITH A BOX, WE HAVE TO SEPARATE EMPTY BOXES
            self.x = x
            self.y = y
            self.empty = True
            self.candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9} - {0}
            self.row = set(Cell.puz[x]) - {0}
            self.col = set([Cell.puz[i][y] for i in range(9)]) - {0}

            # GROUPS CANNOT BE IDENTIFIED EASILY AS THERE IS NO GENERAL PATTERN, SO I DID IT MANUALLY
            grp1 = set([Cell.puz[i][j] for i in range(3) for j in range(3)]) - {0}
            grp2 = set([Cell.puz[i][j] for i in range(3) for j in range(3, 6)]) - {0}
            grp3 = set([Cell.puz[i][j] for i in range(3) for j in range(6, 9)]) - {0}
            grp4 = set([Cell.puz[i][j] for i in range(3, 6) for j in range(3)]) - {0}
            grp5 = set([Cell.puz[i][j] for i in range(3, 6) for j in range(3, 6)]) - {0}
            grp6 = set([Cell.puz[i][j] for i in range(3, 6) for j in range(6, 9)]) - {0}
            grp7 = set([Cell.puz[i][j] for i in range(6, 9) for j in range(3)]) - {0}
            grp8 = set([Cell.puz[i][j] for i in range(6, 9) for j in range(3, 6)]) - {0}
            grp9 = set([Cell.puz[i][j] for i in range(6, 9) for j in range(6, 9)]) - {0}

            groups = [grp1, grp2, grp3, grp4, grp5, grp6, grp7, grp8, grp9]

            if x <= 2 and y <= 2:
                self.grp = groups[0]
            elif x <= 2 < y <= 5:
                self.grp = groups[1]
            elif x <= 2 and 5 < y <= 8:
                self.grp = groups[2]
            elif 5 >= x > 2 >= y:
                self.grp = groups[3]
            elif 5 >= x > 2 < y <= 5:
                self.grp = groups[4]
            elif 2 < x <= 5 < y <= 8:
                self.grp = groups[5]
            elif 5 < x <= 8 and 2 >= y:
                self.grp = groups[6]
            elif 8 >= x > 5 >= y > 2:
                self.grp = groups[7]
            elif 5 < x <= 8 and 5 < y <= 8:
                self.grp = groups[8]
        else:
            self.empty = False

    # THE CANDIDATES ARE CALCULATED BY ROW,SQR,COLUMN
    def eval_candidates(self):
        self.candidates -= self.row
        self.candidates -= self.col
        self.candidates -= self.grp

    # THE ROW,COL,SQR OF EACH BOX INSTANCE DOES NOT CHANGE ON ITS OWN WHEN P CHANGES [NO IDEA WHY]
    # SO IT NEEDS UPDATING BY REASSIGNING ROW,COL,SQR TO EACH BOX
    # NOTE HOW I DIDN'T RE ASSIGN CANDIDATES
    def update(self):
        x = self.x
        y = self.y
        if Cell.puz[x][y] == 0:
            self.x = x
            self.y = y
            self.empty = True
            self.row = set(Cell.puz[x]) - {0}
            self.col = set([Cell.puz[i][y] for i in range(9)]) - {0}

            grp1 = set([Cell.puz[i][j] for i in range(3) for j in range(3)]) - {0}
            grp2 = set([Cell.puz[i][j] for i in range(3) for j in range(3, 6)]) - {0}
            grp3 = set([Cell.puz[i][j] for i in range(3) for j in range(6, 9)]) - {0}
            grp4 = set([Cell.puz[i][j] for i in range(3, 6) for j in range(3)]) - {0}
            grp5 = set([Cell.puz[i][j] for i in range(3, 6) for j in range(3, 6)]) - {0}
            grp6 = set([Cell.puz[i][j] for i in range(3, 6) for j in range(6, 9)]) - {0}
            grp7 = set([Cell.puz[i][j] for i in range(6, 9) for j in range(3)]) - {0}
            grp8 = set([Cell.puz[i][j] for i in range(6, 9) for j in range(3, 6)]) - {0}
            grp9 = set([Cell.puz[i][j] for i in range(6, 9) for j in range(6, 9)]) - {0}

            groups = [grp1, grp2, grp3, grp4, grp5, grp6, grp7, grp8, grp9]

            if x <= 2 and y <= 2:
                self.grp = groups[0]
            elif x <= 2 < y <= 5:
                self.grp = groups[1]
            elif x <= 2 and 5 < y <= 8:
                self.grp = groups[2]
            elif 5 >= x > 2 >= y:
                self.grp = groups[3]
            elif 5 >= x > 2 < y <= 5:
                self.grp = groups[4]
            elif 2 < x <= 5 < y <= 8:
                self.grp = groups[5]
            elif 5 < x <= 8 and 2 >= y:
                self.grp = groups[6]
            elif 8 >= x > 5 >= y > 2:
                self.grp = groups[7]
            elif 5 < x <= 8 and 5 < y <= 8:
                self.grp = groups[8]
        else:
            self.empty = False


# PRE-DEFINED FUNCTION TO CHECK IF ALL BOXES ARE FILLED
def all_filled(p):
    for i in p:
        for j in i:
            if j == 0:
                return False
    return True

'''
p = [[0, 1, 0, 0, 0, 5, 0, 0, 0],
     [0, 0, 0, 8, 0, 6, 0, 9, 0],
     [0, 7, 0, 0, 1, 0, 8, 0, 0],
     [3, 0, 8, 0, 2, 7, 0, 0, 5],
     [0, 0, 0, 3, 0, 4, 0, 0, 0],
     [5, 0, 0, 6, 9, 0, 3, 0, 4],
     [0, 0, 1, 1, 6, 0, 0, 5, 0],
     [0, 5, 0, 2, 2, 3, 0, 0, 0],
     [0, 0, 0, 5, 0, 0, 0, 8, 0]]
'''

def solved(p):
    Cell.getpuzzle(p)
    cells = [[Cell(i, j) for j in range(9)] for i in range(9)]

    # HERE IS THE HEART OF THE PROGRAM
    # THE SOLUTION LOGIC
    while not all_filled(p):  # as long as all the boxes are'nt filled keep repeating the following
        Cell.getpuzzle(p)
        for row in cells:
            for box in row:
                if box.empty:
                    box.update()  # update all empty boxes

        q = [i.copy() for i in p]  # q will be a copy of puzzle to keep track of any change in p

        for row in cells:
            for box in row:
                if box.empty:
                    box.eval_candidates()  # evaluate all empty boxes
                    if len(box.candidates) == 1:  # if you find any box with a single candidate
                        p[box.x][box.y] = list(box.candidates)[0]  # change element of p to that candidate...the element's
                        # address given by the box's attributes
        Cell.getpuzzle(p)
        for r in cells:
            for b in r:
                if b.empty:
                    b.update()  # update all empty boxes

        if q == p:  # if the puzzle has not changed....the above effort failed to even corner down a single box then we
            # need to try other methods
            for row in cells:
                r_freq = Counter()
                for box in row:
                    if box.empty:
                        r_freq.update(box.candidates)

                for g in r_freq:
                    if r_freq[g] == 1:
                        for box in row:
                            if box.empty and g in box.candidates:
                                p[box.x][box.y] = g  # evaluate each row of boxes, if any number appears only in a
                                #  particular box...fix it in
                                Cell.getpuzzle(p)
                                for r in cells:
                                    for b in r:
                                        if b.empty:
                                            box.update()  # update all empty boxes

            if q == p:  # if still puzzle isn't changed

                box_cols = [[cells[i][j] for i in range(9)] for j in range(9)]  # same evaluation for column of boxes
                for col in box_cols:
                    c_freq = Counter()
                    for box in col:
                        if box.empty:
                            c_freq.update(box.candidates)

                    for g in c_freq:
                        if c_freq[g] == 1:
                            for box in col:
                                if box.empty and g in box.candidates:
                                    p[box.x][box.y] = g
                                    Cell.getpuzzle(p)
                                    for r in cells:
                                        for b in r:
                                            if b.empty:
                                                b.update()
                if q == p:  # if yet still puzzle has not changed, evaluate square-wise
                    box_grp1 = [cells[i][j] for i in range(3) for j in range(3)]
                    box_grp2 = [cells[i][j] for i in range(3) for j in range(3, 6)]
                    box_grp3 = [cells[i][j] for i in range(3) for j in range(6, 9)]
                    box_grp4 = [cells[i][j] for i in range(3, 6) for j in range(3)]
                    box_grp5 = [cells[i][j] for i in range(3, 6) for j in range(3, 6)]
                    box_grp6 = [cells[i][j] for i in range(3, 6) for j in range(6, 9)]
                    box_grp7 = [cells[i][j] for i in range(6, 9) for j in range(3)]
                    box_grp8 = [cells[i][j] for i in range(6, 9) for j in range(3, 6)]
                    box_grp9 = [cells[i][j] for i in range(6, 9) for j in range(6, 9)]

                    box_groups = [box_grp1, box_grp2, box_grp3, box_grp4, box_grp5, box_grp6, box_grp7, box_grp8,
                                  box_grp9]

                    for sqr in box_groups:
                        s_freq = Counter()
                        for box in sqr:
                            if box.empty:
                                s_freq.update(box.candidates)
                        for g in s_freq:
                            if s_freq[g] == 1:
                                for box in sqr:
                                    if box.empty and g in box.candidates:
                                        p[box.x][box.y] = g
                                        Cell.getpuzzle(p)
                                        for r in cells:
                                            for b in r:
                                                if b.empty:
                                                    b.update()
                    if q == p:  # IF STILL THE PUZZLE REMAINS UNCHANGED. NO HUMAN CAN SOLVE IT...PLS ADD BRUTE FORCE
                        # ALGORITHM HERE
                        break
    return(p)
