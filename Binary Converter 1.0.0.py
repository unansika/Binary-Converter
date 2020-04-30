#to - do
#space out ui
#fix delete for contents in e2 important close program between each version for now ////  done
#add ways to deal with getting 0 as the integer //// done
#add more stuff for the calcualations cause it looks cool

#imports

from tkinter import *
from tkinter import messagebox
from math import trunc

#i think this helps

binary = ''
integer = 0
x = '1'
y = '0'
z = '-'

#main thing

def binarycalc(event=None):
    processing = e1.get()  #get integer

    #try out exceptions

    try:
        integer = int(processing)
    except ValueError:
        print('Not an integer')
        messagebox.showerror("Error", "Please insert an integer")
    except integer == 0:
        binary = '0'
        e2.delete(first=0, last=END)
        e2.insert(END, binary)

    else:
        print(integer)
        binary = ''
        print("Calculations:")


        if integer < 0:
            z = '-'
        else:
            z = ''

        #binary thing

        while(integer > 0 or integer < 0):
            print(integer)
            if integer % 2 == 0:
                binary = (binary + y)
                integer = integer / 2
            else:
                binary = (binary + x)
                integer = integer / 2
                print(integer)
                integer = trunc(integer)

        print('Answer:')
        length = len(binary)
        final = binary[length::-1]
        final = z + final
        print(final)
        e2.delete(first=0,last=END)
        e2.insert(END,final)

#ui

window = Tk()
window.geometry('300x220')
window.title('Binary Converter')
window.configure(bg = 'black')

message = Message(window, text = 'Binary Converter', font = 'Arial', anchor = 'center', fg = 'yellow',bg = 'black')
message.grid(row = 0,column = 0)

instructions = Message(window, text = 'Insert the integer you would like to be in binary in the Integer entry box!',
                       fg = 'yellow', bg = 'black')

instructions.grid(row = 1,column = 0)

label1 = Label(window , text = 'Integer' ,bg = 'black' ,fg = 'yellow')
label1.grid(row = 4,column = 0)

e1 = Entry(window)
e1.grid(row = 4 ,column = 1)

label2 = Label(window, text = 'Binary', bg = 'black',fg = 'yellow')
label2.grid(row = 6,column = 0)

e2 = Entry(window)
e2.grid(row = 6, column = 1)

button = Button(window, text = 'Calculate',fg = 'yellow',bg = 'black',command = binarycalc)
button.grid(row = 8,column = 0)

window.bind('<Return>',binarycalc)

window.mainloop()

#reece(unansika)

