__author__ = 'Pawel'

import sys
import getopt

class Puzzle():
    def __init__(self, N=3):
        self.N = N
        self.state = {}
        self.gap = (self.N - 1, self.N - 1)

        for i in range(self.N):
            for j in range(self.N):
                self.state[(i, j)] = (i * self.N + j + 1)%(self.N**2)

    def __str__(self):
        space = len(str(max(self.state.values())))
        board = '+' + ('-' + '-' * space + '-+') * self.N + '\n'
        for i in range(self.N):
            for j in range(self.N):
                number = ('{:' + str(space) + 'd}').format(self.state[i, j])
                board += '| ' + number + ' '
            board += '|\n'
            for j in range(self.N):
                board += '+-' + '-' * space + '-'
            board += '+\n'
        return board

    def is_finished(self):
        for i, j in self.state:
            if self.state[i, j] != (i * self.N + j + 1)%(self.N**2):
                return False
        return True

    def get_valid_moves(self):
        a,b = self.gap
        moves = {'left':(a,b-1),'right':(a,b+1),'down':(a+1,b),'up':(a-1,b)}
        if a<=0 :
            moves.pop('up')
        elif a>= self.N-1:
            moves.pop('down')
        if b<=0:
            moves.pop('left')
        elif b>=self.N-1:
            moves.pop('right')

        return moves

    def move_to(self, move):

        moves = self.get_valid_moves()

        for direction, goal in moves.iteritems():
            if direction == move:
                self.state[self.gap],self.state[goal] = self.state[goal],self.state[self.gap]
                self.gap = goal
                break

if __name__ == '__main__':
    puzzle = Puzzle(7)
    is_finished = False
    while not is_finished:
        print puzzle
        print puzzle.get_valid_moves()
        puzzle.move_to(raw_input('Your move: '))
        is_finished = puzzle.is_finished()

    print "Game over"

