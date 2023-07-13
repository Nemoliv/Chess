# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:36:48 2023

@author: olivi
"""
import pieces
from pieces import is_piece
from pieces import is_colour
import pieces

def init_board():     
    board = [['□' for j in range (8)] for i in range(8)]
    for i in range(8):
        for j in [2,4,6]:
            board[i][i] = '◼'
            board[i-j][i]='◼' 
    return board
   
def init_position(board): 
    board[0][4]='♔'
    board[7][3]='♚'
    
    board[0][3]='♕'
    board[7][4]='♛'
    
    for b in [2,5]:
        board[0][b]='♗'
        
    for b in [2,5]:
        board[7][b]='♝'
    
    for n in [1,6]:
        board[0][n]='♘'
    
    for n in [1,6]:
        board[7][n]='♞'
        
    for r in [0, 7]:
        board[7][r]='♖'
    
    for r in [0, 7]:
        board[0][r]='♜'
        
    for p in range(8):
        board[1][p]='♙'
        
    for p in range(8):
        board[6][p]='♟︎'
        
def print_board(board):
    print(" ", end=" ")
    abc='abcdefgh'
    for i in abc:
        print(f"{i} ", end=" ")
    print()
    
    for row in range(len(board)):
        print(row+1, end=" ")
        for col in range(len(board)):
            print(board[row][col], end=" ")
        print()
        
def update_board(board, irow, icol, frow, fcol):
    board[frow][fcol] = board[irow][icol]
    board[irow][icol]=init_board()[irow][icol]
        
board = init_board()
init_position(board)
print_board(board)