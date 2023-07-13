# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:48:51 2023

@author: olivi
"""

def is_piece(board, row, col):
    if board[row][col]=='□' or board[row][col]=='◼':
        return False
    elif board[row][col]=='♔' or board[row][col]=='♚':
        return 'king'
    elif board[row][col]=='♕' or board[row][col]=='♛':
        return 'queen'
    elif board[row][col]=='♗' or board[row][col]=='♝':
        return 'bishop'
    elif board[row][col]=='♘' or board[row][col]=='♞':
        return 'knight'
    elif board[row][col]=='♖' or board[row][col]=='♜':
        return 'rook'
    else:
        return 'pawn'
    
def is_colour(board, row, col):
    if board[row][col]=='□' or board[row][col]=='◼':
        return False
    elif board[row][col]=='♔':
        return 'black'
    
    elif board[row][col]=='♚':
        return 'white'
    
    elif board[row][col]=='♕':
        return 'black'
    
    elif board[row][col]=='♛':
        return 'white'
    
    elif board[row][col]=='♗':
        return 'black'
    
    elif board[row][col]=='♝':
        return 'white'
    
    elif board[row][col]=='♘':
        return 'black'
    
    elif board[row][col]=='♞':
        return 'white'
    
    elif board[row][col]=='♖':
        return 'white'
    elif board[row][col]=='♜':
        return 'black'
    
    elif board[row][col]=='♙':
        return 'black'
    
    else:
        return 'white'
    
def horizontal_intersect(board,irow,icol,frow,fcol):
    #right is negative
    coldiff=icol-fcol
    if coldiff<0:
        for i in range(1, -1*coldiff): 
            #all the spaces between initial and final position
            if board[irow][icol+i]!="◼" or board[irow][icol+i]!='□':
                #for this case the columns are increasing, moving right
                #if the space isn't blank, there's a piece there
                print(icol+i)
                print("there is a piece in the way")
                return True
    elif coldiff>0:
        for i in range(1, coldiff):
            if board[irow][icol-i]!="◼" or board[irow][icol-i]!='□':
                #For this case, columns are decreasing, moving left so -i
                print(icol-i)
                print("there is a piece in the way")
                return True
    else:
        return False

def vertical_intersect(board,irow,icol,frow,fcol):
    #down is negative
    rowdiff=irow-frow
    if rowdiff<0:
        for i in range(1, -1*rowdiff): 
            #every space between initial position and final position
            if board[irow+i][icol]!="◼" or board[irow+i][icol]!='□':
                #+i because moving down, rows increasing
                #if there is a piece on any point, it is an intersect
                print("There is a piece in the way")
                return True
    elif rowdiff>0:
        for i in range(1, rowdiff):
            if board[irow-i][icol]!="◼" or board[irow-i][icol]!='□':
                #-i because moving up the rows, rows decreasing
                print('there is a piece in the way')
                return True
            
def diagonal_intersect(board,irow,icol,frow,fcol):
    rowdiff=irow-frow
    coldiff=icol-fcol
    #moves to bottom right, row should increase, col should increase
    if rowdiff<0 and coldiff<0:
        for i in range(1,-1*rowdiff):
            if board[irow+i][icol+i]!="◼" or board[irow+i][icol+i]!='□':
                print("there is a piece in the way")
                return True
    #moves to bottom left, row should increase, column should decrease
    elif rowdiff<0 and coldiff>0:
        for i in range(1,-1*rowdiff):
            if board[irow+i][icol-i]!="◼" or board[irow+i][icol-i]!='□':
                print("there is a piece in the way")
                return True
    #moves to top right, row decrease, col increase
    elif rowdiff>0 and coldiff<0:
        for i in range(1,rowdiff):
            if board[irow-i][icol+i]!="◼" or board[irow-i][icol+i]!='□':
                print("there is a piece in the way")
                return True
    #moves to top left, row should decrease, col should decrease
    elif rowdiff>0 and coldiff>0:
        for i in range(1,rowdiff):
            if board[irow-i][icol-i]!="◼" or board[irow-i][icol-i]!='□':
                print("there is a piece in the way")
                return True
    else:
        return False
    
def king(board,irow,icol,frow,fcol):
    if frow==irow+1 and icol==fcol:
        if vertical_intersect(board,irow,icol,frow,fcol):
            return True
    elif fcol==icol+1 and irow==frow:
        if horizontal_intersect(board,irow,icol,frow,fcol)!=True:
            return True
    elif frow==irow-1 and icol==fcol:
        if vertical_intersect(board,irow,icol,frow,fcol):
            return True
    elif fcol==icol-1 and irow==frow:
        if horizontal_intersect(board,irow,icol,frow,fcol)!=True:
            return True
    elif frow==irow-1 and fcol==icol+1:
        if diagonal_intersect(board,irow,icol,frow,fcol)!=True:
            return True
    elif frow==irow+1 and fcol==icol-1:
        if diagonal_intersect(board,irow,icol,frow,fcol)!=True:
            return True
    elif frow==irow-1 and fcol==icol-1:
        if diagonal_intersect(board,irow,icol,frow,fcol)!=True:
            return True
    elif frow==irow+1 and fcol==icol+1:
        if diagonal_intersect(board,irow,icol,frow,fcol)!=True:
            return True
    else:
        return False

def bishop(board,irow,icol,frow,fcol):
    for j in [0,1,2,3,4,5,6,7]:
        if diagonal_intersect(board,irow,icol,frow,fcol)!=True:
            if frow==irow-j and fcol==icol+j:
                return True
            elif frow==irow+j and fcol==icol-j:
                return True
            elif frow==irow-j and fcol==icol-j:
                return True
            elif frow==irow+j and fcol==icol+j:
                return True
    else:
        return False

def knight(irow,icol,frow,fcol):
    if frow==irow+2 and fcol==icol+1:
            return True
    elif frow==irow+1 and fcol==icol+2:
        return True
    elif frow==irow-1 and fcol==icol+2:
        return True
    elif frow==irow-2 and fcol==icol+1:
        return True
    elif frow==irow-2 and fcol==icol-1:
        return True
    elif frow==irow-1 and fcol==icol-2:
        return True
    elif frow==irow+1 and fcol==icol-2:
        return True
    elif frow==irow+2 and fcol==icol-1:
        return True
    else:
        return False
        
def rook(board,irow,icol,frow,fcol):
    if irow==frow:
        if horizontal_intersect(board,irow,icol,frow,fcol)!=True:
            return True
        
    elif icol==fcol:
        if vertical_intersect(board,irow,icol,frow,fcol):
            return True
    else:
        return False
    

def pawn_take_white(board, irow, icol,frow,fcol):
    if frow==irow-1 and fcol==icol+1:
        if board[frow][fcol]!="◼":
            return True
        elif board[frow][fcol]!='□':
            return True
        else:
            return False

    elif frow==irow-1 and fcol==icol-1:
        if board[frow][fcol]!="◼":
            return True
        elif board[frow][fcol]!='□':
            return True
        else:
            return False

def pawn_take_black(board, irow, icol,frow,fcol):
    if frow==irow+1 and fcol==icol+1:
        if board[frow][fcol]!="◼":
            return True
        elif board[frow][fcol]!='□':
            return True
        else:
            return False

    elif frow==irow+1 and fcol==icol-1:
        if board[frow][fcol]!="◼":
            return True
        elif board[frow][fcol]!='□':
            return True
        else:
            return False

def pawn(board,irow,icol,frow,fcol):
    #if it is the pawn's first move it can move one...
    #space up or 2 spaces up
    if is_colour(board, irow,icol)=='white':
        if irow==6 or irow==1:
            if frow==irow-1:
                if vertical_intersect(board,irow,icol,frow,fcol)!=True:
                    return True
            elif frow==irow-2:
                if vertical_intersect(board,irow,icol,frow,fcol)!=True:
                    return True
            elif pawn_take_white(board, irow, icol,frow,fcol)==True:
                return True
            else:
                return False
        elif irow==irow-1:
            if vertical_intersect(board,irow,icol,frow,fcol)!=True:
                return True
        elif pawn_take_white(board, irow, icol,frow,fcol)==True:
            return True
        else:
            return False
        
    else:
        if irow==6 or irow==1:
            if frow==irow+1:
                if vertical_intersect(board,irow,icol,frow,fcol)!=True:
                    return True
            elif frow==irow+2:
                if vertical_intersect(board,irow,icol,frow,fcol)!=True:
                    return True
            elif pawn_take_black(board, irow, icol,frow,fcol)==True:
                return True
            else:
                return False
        elif irow==irow+1:
            if vertical_intersect(board,irow,icol,frow,fcol)!=True:
                return True
        elif pawn_take_black(board, irow, icol,frow,fcol):
            return True
        else:
            return False