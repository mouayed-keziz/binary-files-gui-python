from tkinter import *
from GUI_SETTINGS import *




def about_program():
    window = Tk()
    window.geometry('1000x500')
    window.title("about this program")
    main_label = Label(master=window, text='ABOUT THIS PROGRAM', font=(Font_1,18), fg=TITLE_TEXT_COLOR)
    main_label.pack(padx=10, pady=10)
    text_label = Label(master=window, text=ABOUT_PROGRAM_TEXT, font=(Font_1, 12), fg=MAIN_TEXT_COLOR)
    text_label.pack()
    window.mainloop()


def about_developer():
    window = Tk()
    window.title("about the developer")
    main_label = Label(master=window, text='ABOUT THE DEVELOPER', font=(Font_1,18), fg=TITLE_TEXT_COLOR)
    main_label.pack(padx=10, pady=10)
    text_label = Label(master=window, text=ABOUT_DEVELOPER_TEXT, font=(Font_1, 12), fg=MAIN_TEXT_COLOR)
    text_label.pack()
    
    #c= Canvas(master=window, width=150, height=150)
    #image = PhotoImage(master=c, file=DEVELOPER_PIC)
    #c.create_image(0,0,  image=image)
    #c.pack()

    window.mainloop()


def MenuBar(root):
    menubar1 = Menu(root, tearoff=0)
    root.config(menu=menubar1)

    #Create a menu item
    file_menu = Menu(menubar1)
    menubar1.add_cascade(label='ABOUT', menu=file_menu)

    file_menu.add_command(label='about program', command=about_program)
    file_menu.add_command(label='about developer', command=about_developer)
    file_menu.add_separator()
    file_menu.add_command(label='EXIT', command=root.quit)