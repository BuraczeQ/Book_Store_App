"""
Programm was created to make a personal database to store books
"""
from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)



def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),title_author.get(),title_year.get(),title_ISBN.get()):
        list1.insert(END,row)


def add_command():
    backend.insert(title_text.get(),title_author.get(),title_year.get(),title_ISBN.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),title_author.get(),title_year.get(),title_ISBN.get()))
    view_command()

def get_seleted_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0],title_text.get(),title_author.get(),title_year.get(),title_ISBN.get())
    view_command()

window = Tk()

window.wm_title("Personal book store for your deskopt!")

l1=Label(window,text="Title")
l1.grid(row=0, column=0)

l2=Label(window,text="Author")
l2.grid(row=0, column=2)

l3=Label(window,text="Year")
l3.grid(row=1, column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1, column=2)


title_text = StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

title_author = StringVar()
e2=Entry(window, textvariable=title_author)
e2.grid(row=0,column=3)

title_year = StringVar()
e3=Entry(window, textvariable=title_year)
e3.grid(row=1,column=1)

title_ISBN = StringVar()
e4=Entry(window, textvariable=title_ISBN)
e4.grid(row=1,column=3)




list1=Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_seleted_row)




b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2,column=3)

b1=Button(window, text="Search Entry", width=12, command=search_command)
b1.grid(row=3,column=3)

b1=Button(window, text="Add Entry", width=12, command=add_command)
b1.grid(row=4,column=3)

b1=Button(window, text="Update", width=12, command=update_command)
b1.grid(row=5,column=3)

b1=Button(window, text="Delete", width=12, command=delete_command)
b1.grid(row=6,column=3)

b1=Button(window, text="Close", width=12, command=window.destroy)
b1.grid(row=7,column=3)







window.mainloop()