"""
Note:
2d arrays: 8 x 8 = [[0[3rd and 4th dims]]x8]x8
additional attribute: (3rd dimension)
rook : Have been moved?
Pawn: Just moved and move was a double up
King: Have been checked?
some bullshit Castle things

                                       
"""

from abc import abstractmethod


class Chess_square():
    seen_by_opponent = False
    piece = 'No'
    def __init__(self,*arg,**details):
        x = details.items()
        self.column = details['column']
        self.row = details['row']
        self.seen_by_opponent = details['in_view']
    def toString(self):
        return (str(self.king_in_check) + ' ' + str(self.seen_by_opponent) + ' ' + str(self.pinned) + ' ')

class Knight(Chess_square):
    piece = 'Knight'
    pinned = False
    def __init__(self,*arg,**details):
        x = details.items()
        super().__init__(self,*arg,**details)
        self.pinned = details['pinned']
        self.color = details['color']
        
    def viewing(self):
        viewing_squares = []
        if self.row + 1 <= 7 and self.column + 2 <= 7:
            viewing_squares.append([self.row + 1 ,self.column + 2])
        if self.row + 2 <= 7 and self.column + 1 <= 7:
            viewing_squares.append([self.row + 2 ,self.column + 1])
        if self.row - 2 >= 0 and self.column - 1 >= 0:
            viewing_squares.append([self.row - 2 ,self.column - 1])
        if self.row - 1 >= 0 and self.column -2 >= 0:
            viewing_squares.append([self.row - 1 ,self.column - 2])
        if self.row - 1 >= 0 and self.column + 2 <= 7:
            viewing_squares.append([self.row - 1 ,self.column + 2])
        if self.row - 2 >= 0 and self.column + 1 <= 7:
            viewing_squares.append([self.row - 2 ,self.column + 1])
        if self.row + 1 <= 7 and self.column - 2 >= 0:
            viewing_squares.append([self.row + 1 ,self.column - 2])
        if self.row + 2 <= 7 and self.column - 1 >= 0:
            viewing_squares.append([self.row + 2 ,self.column - 1])
        return viewing_squares


test_knight = Knight(column=5,row=3,piece=None,in_view=False,pinned=False,color="White")
test_knight['row'] = 5
print(test_knight.viewing())

