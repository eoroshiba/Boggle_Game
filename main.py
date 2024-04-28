# Simple boggle game with built-in GUI

# Importing modules
from tkinter import *
import time
import random


# Defining boggle dice
DIE_1 = ['R', 'I', 'F', 'O', 'B', 'X']
DIE_2 = ['I', 'F', 'E', 'H', 'E', 'Y']
DIE_3 = ['D', 'E', 'N', 'O', 'W', 'S']
DIE_4 = ['U', 'T', 'O', 'K', 'N', 'D']
DIE_5 = ['H', 'M', 'S', 'R', 'A', 'O']
DIE_6 = ['A', 'C', 'I', 'T', 'O', 'A']
DIE_7 = ['L', 'U', 'P', 'E', 'T', 'S']
DIE_8 = ['Y', 'L', 'G', 'K', 'U', 'E']
DIE_9 = ['Qu', 'N', 'M', 'J', 'O', 'A']
DIE_10 = ['E', 'H', 'I', 'S', 'P', 'N']
DIE_11 = ['V', 'E', 'T', 'I', 'G', 'N']
DIE_12 = ['B', 'A', 'L', 'I', 'Y', 'T']
DIE_13 = ['E', 'Z', 'A', 'V', 'N', 'D']
DIE_14 = ['R', 'A', 'L', 'E', 'S', 'C']
DIE_15 = ['U', 'W', 'I', 'L', 'R', 'G']
DIE_16 = ['P', 'A', 'C', 'E', 'M', 'D']

# Creating array of boggle dice
die_array = [DIE_1, DIE_2, DIE_3, DIE_4, DIE_5, DIE_6, DIE_7, DIE_8, DIE_9, DIE_10, DIE_11, DIE_12, DIE_13, DIE_14, DIE_15, DIE_16]


# Defining function to return randomized boggle board
def getRandomBoard(die_array):
    
    die_array = die_array[:]
    
    board = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    
    for x in range(4):
        for y in range(4):
            cur_die = die_array[random.randint(0, len(die_array)-1)]
            die_array.remove(cur_die)
            cur_letter = cur_die[random.randint(0,5)]
            board[x][y] = cur_letter

    return board



### START OF SCRIPT ###

# Getting Boggle board array
board = getRandomBoard(die_array)

# Create window, define background based on local time
gui = Tk()
gui.title("Boggle Generator")
my_time = time.localtime()
if my_time.tm_hour < 6 or my_time.tm_hour > 18:
    gui["bg"] = "#7a7a7a"
else:
    gui["bg"] = "#e8e8e8"
gui.geometry('820x820')

# Create inner frame for extra padding
inside_frame = Frame(gui, height = "800", width = "800", padx = 20, pady = 20, bg = gui["bg"])
inside_frame.columnconfigure(0, weight = 1)
inside_frame.rowconfigure(0, weight = 1)

# Populate inner frame with series of frames to create board
for _row in range(4):
    for _col in range(4):
        temp_frame = Frame(inside_frame, height = 150, width = 150, borderwidth = 3, relief = "solid", bg = "white")
        temp_label = Label(temp_frame, text = board[_row][_col], font = ("TkDefaultFont", 72, "bold"), bg = "white")
        temp_frame.grid(column = _col, row = _row, padx = 10, pady = 10)
        temp_frame.columnconfigure(0, weight = 1)
        temp_frame.rowconfigure(0, weight = 1)
        temp_label.place(relx = 0.5, rely = 0.5, anchor = "center")
        
inside_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
gui.mainloop()