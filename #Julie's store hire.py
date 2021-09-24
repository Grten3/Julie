#Julie's store hire program f
#This program is used to store customer purchase data so that inventory of the store can be track


from tkinter import*
import random
import re



def quit(): #quit command
    main_window.destroy()


#print details of all the camps
def print_purchase_details ():
    global total_entries, name_count


    name_count = 0
    Label(main_window, font='bold',text="Row").grid(column=0,row=10, pady=(20,5))
    Label(main_window, font='bold',text="Full Name").grid(column=1,row=10, pady=(20,5))
    Label(main_window, font='bold',text="Receipt No.").grid(column=2,row=10, pady=(20,5))
    Label(main_window, font='bold',text="Item Hired").grid(column=3,row=10, pady=(20,5))
    Label(main_window, font='bold',text="Quantity").grid(column=4,row=10, padx=(35,0), pady=(20,5))




    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0,row=name_count+11)
        Label(main_window, text=(purchase_details[name_count][0])).grid(column=1,row=name_count+11)
        Label(main_window, text=(purchase_details[name_count][1])).grid(column=2,row=name_count+11)
        Label(main_window, text=(purchase_details[name_count][2])).grid(column=3,row=name_count+11)
        Label(main_window, text=(purchase_details[name_count][3])).grid(column=4,row=name_count+11)
        main_window.geometry("")
        name_count +=  1




#add the next camper to the list if all parameters are meet
def append_details ():
    global purchase_details, full_name, receipt_no, item_hired, quantity, total_entries, full_name_first, full_name_blank
  

  
    while len(re.findall(r'\w+', full_name.get())) == 0:
        full_name_blank = Label(main_window, text="    *This can't be blank. Enter the customer's Full Name     ", fg="red")
        full_name_blank.grid(row=1, column=3, columnspan=3)
        print("loop")
        full_name_blank.after(6000,lambda:full_name_blank.destroy())
        break
             
    while 0 < len(re.findall(r'\w+', full_name.get())) < 2:
        full_name_first = Label(main_window, text="*Only First name is entered. Enter the customer's Full Name", fg="red")
        full_name_first.grid(row=1, column=3, columnspan=3)
        print("loop1")
        full_name_first.after(6000,lambda:full_name_first.destroy())
        break
    

    if len(re.findall(r'\w+', full_name.get())) > 1:
         purchase_details.append([full_name.get().title(),receipt_no.get(),item_hired .get(),quantity.get()])
         full_name.delete(0,'end')
         receipt_no.delete(0,'end')
         item_hired.delete(0,'end')
         quantity.delete(0,'end')
         total_entries +=  1
         print("Loop3")
        

def clear():
    full_name_blank.destroy()
    full_name_first.destroy()




#delete a row from the list
def delete_row ():
    global purchase_details, delete_item, total_entries, name_count
    del purchase_details[int(delete_item.get())]
    total_entries -= 1
    delete_item.delete(0,'end')
    Label(main_window, text="       ").grid(column=0,row=name_count+10)
    Label(main_window, text="       ").grid(column=1,row=name_count+10)
    Label(main_window, text="       ").grid(column=2,row=name_count+10)
    Label(main_window, text="       ").grid(column=3,row=name_count+10)
    Label(main_window, text="       ").grid(column=4,row=name_count+10)
    print_purchase_details()






def GUI(): #Main GUI of the program
    global purchase_details, full_name, receipt_no, item_hired, quantity, total_entries, delete_item, full_name_blank

    Button(main_window, text="Quit", width= 8, command= quit) .grid(row=0, column=0, padx=(10,0), pady =(10, 40), sticky=E) #Button to execute the quit command
    Button(main_window, text="Store data", width= 8, command= append_details) .grid(row=0, column=4,  pady =(10, 40),  sticky=W) #Button to execute the append command
    Button(main_window, text="Print", width= 8, command= print_purchase_details) .grid(row=0, column=5, padx=7,  pady =(10, 40),  sticky=E) #Button to execute the print command

    Label(main_window, text="Full Name") .grid(row=1, column=1, sticky=E)
    full_name = Entry(main_window) #Text entry box for lengths
    full_name.grid(row=1, column=2, padx=10, pady=2, columnspan=2, sticky=W)
    
  

    Label(main_window, text="Receipt No.") .grid(row=2, column=1, sticky=E)
    receipt_no = Entry(main_window) #Text entry box for width
    receipt_no.grid(row=2, column=2, padx=10, pady=2,columnspan=2, sticky=W)

    Label(main_window, text="Item Hired") .grid(row=3, column=1, sticky=E)
    item_hired = Entry(main_window) #Text entry box for height
    item_hired.grid(row=3, column=2, padx=10, pady=2, columnspan=2, sticky=W)

    Label(main_window, text="Quantity") .grid(row=4, column=1, sticky=E)
    quantity = Entry(main_window) #Text entry box for height
    quantity.grid(row=4, column=2, padx=10, pady=2, columnspan=2, sticky=W)



    Label(main_window, text="") .grid(row=7, column= 1, columnspan=4, pady=2)

    Label(main_window, text="Row No.") .grid(column=1,row=8, padx=0, pady= 5, sticky=E)
    delete_item = Entry(main_window)
    delete_item .grid(column=2,row=8,padx=10, pady=1)
    Button(main_window, text="Delete", width= 8, command=delete_row) .grid(column=2,row=9, pady=4, sticky=E)







#start the program running
def main():
    global main_window
    global purchase_details, full_name, receipt_no, item_hired, quantity, total_entries, full_name_first, full_name_blank
    purchase_details = []
    total_entries = 0
    main_window =Tk()
    GUI()  
    main_window.title("Tracking Program")
    
    main_window.mainloop()


main()
