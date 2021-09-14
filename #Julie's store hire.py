#Julie's store hire program 
#This program is used to store customer purchase data so that inventory of the store can be track


from tkinter import *
import random
main_window =Tk()

main_window.title("Tracking Program")

def quit(): #quit command
    main_window.destroy()


def print(): #Print the details of the purchase 

def append(): #Store the details of the purchase to be printed later on 
    
  




def main(): #Main GUI of the program 
    Button(main_window, text="Quit", command=quit) .grid(row=6, column=0, padx=7, pady =5) #Button to execute the quit command
    Button(main_window, text="Print", command=calculate) .grid(row=6, column=1) #Button to execute the random command 
    Label(main_window, text="Full Name:") .grid(row=1, column=0) 
    Label(main_window, text="Receipt No.:") .grid(row=2, column=0)
    Label(main_window, text="Item Hired:") .grid(row=3, column=0)
    Label(main_window, text="Quantity:") .grid(row=4, column=0)
    


    main_window.mainloop()

length = Entry(main_window) #Text entry box for lengths
length.grid(row=1, column=1, padx=10, pady=2) 

width = Entry(main_window) #Text entry box for width 
width.grid(row=2, column=1, padx=10, pady=2)

height = Entry(main_window) #Text entry box for height 
height.grid(row=3, column=1, padx=10, pady=2)



main()

