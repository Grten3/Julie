#Julie's store hire program 
#This program is used to store customer purchase data so that inventory of the store can be track


from tkinter import *
import random




def quit(): #quit command
    main_window.destroy()


#print details of all the camps
def print_purchase_details ():
    global j_names, total_entries, name_count
    name_count = 0
    Label(main_window, font='bold',text="Row").grid(column=0,row=7)
    Label(main_window, font='bold',text="Full Name").grid(column=1,row=7)
    Label(main_window, font='bold',text="Receipt No.").grid(column=2,row=7)
    Label(main_window, font='bold',text="Item Hired").grid(column=3,row=7)
    Label(main_window, font='bold',text="Quantity").grid(column=4,row=7)

    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(purchase_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(purchase_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(purchase_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=(purchase_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1


#add the next camper to the list
def append_details ():
    global purchase_details, full_name, receipt_no, item_hired, quantity, total_entries
    if len(full_name.get()) != 0 :
        purchase_details.append([full_name.get(),receipt_no.get(),item_hired .get(),quantity.get()])
        full_name.delete(0,'end')
        receipt_no.delete(0,'end')
        item_hired.delete(0,'end')
        quantity.delete(0,'end')
        total_entries +=  1
  


#delete a row from the list
def delete_row ():
    global purchase_details, delete_item, total_entries, name_count
    del purchase_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')
    Label(main_window, text="       ").grid(column=0,row=name_count+7) 
    Label(main_window, text="       ").grid(column=1,row=name_count+7)
    Label(main_window, text="       ").grid(column=2,row=name_count+7)
    Label(main_window, text="       ").grid(column=3,row=name_count+7)
    Label(main_window, text="       ").grid(column=4,row=name_count+7)
    print_purchase_details()



def GUI(): #Main GUI of the program 
    global purchase_details, full_name, receipt_no, item_hired, quantity, total_entries, delete_item

    Button(main_window, text="Quit", command=quit) .grid(row=0, column=6, padx=7, pady =5) #Button to execute the quit command
    Button(main_window, text="Print", command=print_purchase_details) .grid(row=0, column=8) #Button to execute the random command 
    Button(main_window, text="Store data", command=append_details) .grid(row=0, column=7) #Button to execute the random command 
    
    Label(main_window, text="Full Name:") .grid(row=1, column=0) 
    full_name = Entry(main_window) #Text entry box for lengths
    full_name.grid(row=1, column=1, padx=10, pady=2) 
    
    Label(main_window, text="Receipt No.:") .grid(row=2, column=0)
    receipt_no = Entry(main_window) #Text entry box for width 
    receipt_no.grid(row=2, column=1, padx=10, pady=2)
    
    Label(main_window, text="Item Hired:") .grid(row=3, column=0)
    item_hired = Entry(main_window) #Text entry box for height 
    item_hired.grid(row=3, column=1, padx=10, pady=2)
    
    Label(main_window, text="Quantity:") .grid(row=4, column=0)
    quantity = Entry(main_window) #Text entry box for height 
    quantity.grid(row=4, column=1, padx=10, pady=2)

    Label(main_window, text="Row #") .grid(column=0,row=6)
    delete_item = Entry(main_window)
    delete_item .grid(column=1,row=6)
    Button(main_window, text="Delete",command=delete_row) .grid(column=2,row=6)


    




#start the program running
def main():
    global main_window
    global purchase_details, total_entries
    purchase_details = []
    total_entries = 0
    main_window =Tk()
    GUI()
    main_window.title("Tracking Program")
    main_window.mainloop()

    

main()

