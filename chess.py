# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:08:29 2023

@author: olivi
"""
from board import init_position
from board import init_board
from board import update_board
from board import print_board
import pieces
from pieces import is_colour
from pieces import is_piece
from pieces import vertical_intersect
from pieces import horizontal_intersect
from pieces import diagonal_intersect

def valid_move(board, irow, icol, frow, fcol):    
    if irow==frow and icol==fcol:
        return False
    
    if is_piece(board, irow, icol)=='king':
        return pieces.king(board,irow,icol,frow,fcol)
    
    if is_piece(board, irow, icol)=='queen':
        if pieces.bishop(board,irow,icol,frow,fcol)==True:
            return True
        elif pieces.rook(board,irow,icol,frow,fcol)==True:
            return True
        else:
            return False
    
    if is_piece(board, irow, icol)=='bishop':
        return pieces.bishop(board,irow,icol,frow,fcol)
        
    if is_piece(board, irow, icol)=='knight':
        return pieces.knight(irow,icol,frow,fcol)
        
    if is_piece(board, irow, icol)=='rook':
        return pieces.rook(board,irow,icol,frow,fcol)

    if is_piece(board, irow, icol)=='pawn':
        return pieces.pawn(board,irow,icol,frow,fcol)

def valid_selection(board, irow, icol, player_turn):
    if is_colour(board, irow, icol)!=player_turn:
        return False
    elif board[irow][icol]=="◼" or board[irow][icol]=='□':
        return False
    else:
        return True
    
def column_number(col):
    if col=='a':
        return 1
    if col=='b':
        return 2
    if col=='c':
        return 3
    if col=='d':
        return 4
    if col=='e':
        return 5
    if col=='f':
        return 6
    if col=='g':
        return 7
    if col=='h':
        return 8

def main():
    board = init_board()
    init_position(board)
    player_turn ="white"
    while True:
        print(f"It is now {player_turn}'s turn to play")
        old_row = int(input("input row piece you wish to move is in: "))
        old_col = input("input column piece you wish to move is in: ")
        old_col=column_number(old_col)
        selection = valid_selection(board, old_row-1, old_col-1, player_turn)
        while selection ==False:
            print(f"you must select from the {player_turn} pieces")
            old_row = int(input("input row piece you wish to move is in: "))
            old_col = input("input column piece you wish to move is in: ")
            old_col=column_number(old_col)
            selection = valid_selection(board, old_row-1, old_col-1, player_turn)
        
        new_row = int(input("input row piece you wish to move it to: "))
        new_col = input("input column you wish to move piece to: ")
        new_col=column_number(new_col)
        
        move = valid_move(board, old_row-1, old_col-1, new_row-1, new_col-1)
        
        while move==False:
            print("invalid move, please reselect.")
            old_row = int(input("input row piece you wish to move is in: "))
            old_col = input("input column piece you wish to move is in: ")
            old_col=column_number(old_col)
            
            new_row = int(input("input row piece you wish to move it to: "))
            new_col = input("input column you wish to move piece to: ")
            new_col=column_number(new_col)
            move = valid_move(board, old_row-1, old_col-1, new_row-1, new_col-1)
        
        update_board(board, old_row-1, old_col-1, new_row-1, new_col-1)
        print_board(board)
        if player_turn=="white":
            player_turn='black'
        else:
            player_turn="white"
        
    
if __name__=="__main__":
    main()