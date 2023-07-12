# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:08:29 2023

@author: olivi
"""
from board import init_position
from board import init_board
from board import print_board
import pieces

def main():
    board = init_board()
    init_position(board)
    print_board(board)
    player_turn ="w"
    pieces.king(board, 4, 4)
    print_board(board)
    
    
if __name__=="__main__":
    main()