# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:36:48 2023

@author: olivi
"""

def init_board():     
    board = [['.' for j in range (8)] for i in range(8)]
    for i in range(8):
        for j in [2,4,6]:
            board[i][i] = '_'
            board[i-j][i]='_' 
    return board
    
def print_board(board):
    print(" ", end=" ")
    for i in range(len(board)):
        print(i+1, end=" ")
    print()
    
    for row in range(len(board)):
        print(row+1, end=" ")
        for col in range(len(board)):
            print(board[row][col], end=" ")
        print()
        
b = init_board()
print_board(b)