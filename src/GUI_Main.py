from tkinter import *
from tkinter import font
from GUI_menu_bar import *
from GUI_SETTINGS import *
from os import system, path, remove
import Tableau_Taille_Variable
import Tableaux_Taille_Fixe
import Listes_Taille_Fixe
import TOF
import T_OF
import LOF
import L_OF
import T_OV_C


def OpenFile():
    file_name = file_name_entry.get()
    if file_name == '':
        display_label.config(text='')
        log_label.config(text='Enter File Name')
        return [False]
    else:
        if not path.isfile('Binary Data\\'+file_name):
            display_label.config(text='')
            log_label.config(text='File Not Found, Go and create it')
            return [False]
        else:
            fileExtension = file_name[file_name.find('.'):]
            if   fileExtension.find('v') != -1 and fileExtension.find('t') != -1:
                log_label.config(text='')
                display_label.config(text=Tableau_Taille_Variable.affichier_fichier(file_name[:file_name.find('.')],  fileExtension))
            elif fileExtension.find('v') != -1 and fileExtension.find('l') != -1:
                log_label.config(text='')
                display_label.config(text='')
            elif fileExtension.find('f') != -1 and fileExtension.find('t') != -1:
                log_label.config(text='')
                display_label.config(text=Tableaux_Taille_Fixe.afficher_fichier(file_name[:file_name.find('.')],  fileExtension))
            elif fileExtension.find('f') != -1 and fileExtension.find('l') != -1:
                log_label.config(text='')
                display_label.config(text=Listes_Taille_Fixe.affichier_fichier(file_name[:file_name.find('.')],   fileExtension))
            return [True, file_name]

def CreateFile():
    file_name = file_name_entry.get()
    if file_name == '':
        display_label.config(text='')
        log_label.config(text='Enter File Name')
    else:
        if not path.isfile('Binary Data\\'+file_name):
            if file_name.find('.') == -1:
                display_label.config(text='')
                log_label.config(text='enter the extension of the file')
            else:
                fileExtension = file_name[file_name.find('.'):]
                if fileExtension == '.tof' or fileExtension == '.t_of' or fileExtension == '.t_ov_c':
                    with open('Binary Data\\'+file_name, 'wb') as file:
                        Tableaux_Taille_Fixe.affecter_entete(file, 0, 0)
                        Tableaux_Taille_Fixe.affecter_entete(file, 1, 0)
                        log_label.config(text='File Created succesfully')
                elif fileExtension == '.lof' or fileExtension == '.l_of':
                    with open('Binary Data\\'+file_name, 'wb') as file:
                        Listes_Taille_Fixe.affecter_entete(file, 0, 0)
                        Listes_Taille_Fixe.affecter_entete(file, 1, 0)
                        Listes_Taille_Fixe.affecter_entete(file, 2, -1)
                        log_label.config(text='File Created succesfully')
                else:
                    log_label.config(text='File Extension doesnt exist')
                display_label.config(text='')

        else:
            display_label.config(text='')
            log_label.config(text='file alredy exists')



def InsertEnr():
    for widgets in informations_frame.winfo_children():
        widgets.destroy()
    
    a = OpenFile()
    if a[0]:
        num_label         = Label(bg=LABELS_COLOR,master=informations_frame, text='        Number:', font=(Font_1, 16))
        name_label        = Label(bg=LABELS_COLOR,master=informations_frame, text='          Name:', font=(Font_1, 16))
        affiliation_label = Label(bg=LABELS_COLOR,master=informations_frame, text='   Affiliation:', font=(Font_1, 16))

        num_entry         = Entry(bg=ENTRY_COLOR,master=informations_frame, font=(Font_1, 16))
        name_entry        = Entry(bg=ENTRY_COLOR,master=informations_frame, font=(Font_1, 16))
        affiliation_entry = Entry(bg=ENTRY_COLOR,master=informations_frame, font=(Font_1, 16))

        num_label.grid(row=0, column=0)
        name_label.grid(row=1, column=0)
        affiliation_label.grid(row=2, column=0)
        num_entry.grid(row=0, column=2)
        name_entry.grid(row=1, column=2)
        affiliation_entry.grid(row=2, column=2)

        submit_button = Button(bg=BUTTONS_COLORS,master=informations_frame, text=' OK ', font=(Font_1, 18), command=lambda * args: Insert(a[1], num_entry.get(), name_entry.get(), affiliation_entry.get()))
        cancel_button = Button(bg=BUTTONS_COLORS,master=informations_frame, text='Cancel', font=(Font_1, 18), command=Cancel_information)

        submit_button.grid(row=3, column=0)
        cancel_button.grid(row=3, column=2)


def Insert(file_name, key, name, affiliation):
    if key == '' or name == '' or affiliation == '':
        log_label.config(text='you have to fill the informations')
    else:
        if not bool(key[0] == '-' and key[1:].isdecimal() or key[0] != '-' and key.isdecimal()):
            log_label.config(text='key has to be a decimal value')
        else:
            fileExtension = file_name[file_name.find('.'):]
            if fileExtension.find('f') != -1:
                enr = Tableaux_Taille_Fixe.resize_chaine(key, 10)+Tableaux_Taille_Fixe.resize_chaine(name, 40)+Tableaux_Taille_Fixe.resize_chaine(affiliation, 20)
                if fileExtension == '.tof':
                    TOF.insertion(file_name, enr)
                if fileExtension == '.t_of':
                    T_OF.insertion(file_name, enr)
                if fileExtension == '.lof':
                    LOF.insertion(file_name, enr)
                if fileExtension == '.l_of':
                    L_OF.insertion(file_name, enr)
                
            else:
                enr = key +':'+ name +'%'+ affiliation
                if fileExtension == '.t_ov_c':
                    T_OV_C.insertion(file_name, enr)
            OpenFile()
def DeleteEnr():
    for widgets in informations_frame.winfo_children():
        widgets.destroy()

    a = OpenFile()
    if a[0]:
        key_label = Label(bg='white',master=informations_frame, text='Key:', font=(Font_1, 18))
        key_entry = Entry(bg=ENTRY_COLOR,master=informations_frame, font=(Font_1, 18))
        submit_button = Button(bg=BUTTONS_COLORS,master=informations_frame, text='  OK  ', command=lambda * args: Delete(a[1], key_entry.get()), font=(Font_1, 18))
        cancel_button = Button(bg=BUTTONS_COLORS,master=informations_frame, text='Cancel', command=Cancel_information, font=(Font_1, 18))
        key_label.grid(row=0, column=1)
        key_entry.grid(row=1, column=1)
        submit_button.grid(row=2, column=0)
        cancel_button.grid(row=2, column=3)
    else:
        log_label.config(text='file not found')
        display_label.config(text='')



def Delete(filename, key):
    if key == '':
        log_label.config(text='enter a key')
    else:
        if not bool(key[0] == '-' and key[1:].isdecimal() or key[0] != '-' and key.isdecimal()):
            log_label.config(text='enter a decimal value')
        else:
            fileExtension = filename[filename.find('.'):]
            if fileExtension == '.tof':
                TOF.supression(filename, int(key))
            if fileExtension == '.t_of':
                T_OF.supression(filename, int(key))
            if fileExtension == '.lof':
                LOF.suppression(filename, int(key))
            if fileExtension == '.l_of':
                L_OF.suppression(filename, int(key))
            if fileExtension == '.t_ov_c':
                T_OV_C.suppression(filename, int(key))
            
            for widgets in informations_frame.winfo_children():
                widgets.destroy()
            
            log_label.config(text='')
            OpenFile()
            #display_label.config(text=)

def Cancel_information():
    for widgets in informations_frame.winfo_children():
        widgets.destroy()

    log_label.config(text='')
    display_label.config(text='')


def SearchEnr():
    for widgets in informations_frame.winfo_children():
        widgets.destroy()
    
    a = OpenFile()
    if a[0]:
        key_label = Label(bg='white',master=informations_frame, text='Key:', font=(Font_1, 18))
        key_entry = Entry(bg=ENTRY_COLOR,master=informations_frame, font=(Font_1, 18))
        submit_button = Button(bg=BUTTONS_COLORS,master=informations_frame, text='  OK  ', command=lambda * args: Search(a[1], key_entry.get()), font=(Font_1, 18))
        cancel_button = Button(bg=BUTTONS_COLORS,master=informations_frame, text='Cancel', command=Cancel_information, font=(Font_1, 18))
        key_label.grid(row=0, column=1)
        key_entry.grid(row=1, column=1)
        submit_button.grid(row=2, column=0)
        cancel_button.grid(row=2, column=3)
    else:
        log_label.config(text='file not found')
        display_label.config(text='')


def Search(filename, key):
    if key == '':
        log_label.config(text='enter a key')
    else:
        if not bool(key[0] == '-' and key[1:].isdecimal() or key[0] != '-' and key.isdecimal()):
            log_label.config(text='enter a decimal value')
        else:
            s = None
            fileExtension = filename[filename.find('.'):]
            if fileExtension == '.tof':
                s = TOF.recherche(filename, int(key))
            if fileExtension == '.t_of':
                s = T_OF.recherche(filename, int(key))
            if fileExtension == '.lof':
                s = LOF.recherche(filename, int(key))
            if fileExtension == '.l_of':
                s = L_OF.recherche(filename,int(key))
            if fileExtension == '.t_ov_c':
                s = T_OV_C.recherche(filename, int(key))
            
            for widgets in informations_frame.winfo_children():
                widgets.destroy()
            
            log_label.config(text=str(s))
            #display_label.config(text='')


def DeleteFile():
    o = OpenFile()
    file_name = file_name_entry.get()
    display_label.config(text='')
    if o[0]:
        remove('Binary Data\\'+file_name)
        log_label.config(text='file deleted succesfully')
    else:
        log_label.config(text='File Not Found')




system('cls')
mainwindow = Tk()
mainwindow.title('Binary Files By KEZIZ Mouayed')
mainwindow.geometry(str(windowWidth)+'x'+str(windowHeight))

mainLabel = Label(master=mainwindow, bg='#15224F')
mainLabel.place(x=0, y=0, width=windowWidth, height=windowHeight)

MenuBar(mainwindow)

global left_frame, right_frame
left_frame = Frame(master=mainwindow, background=LEFT_FRAME_COLOR)
right_frame = Frame(master=mainwindow, background=RIGHT_FRAME_COLOR)

left_frame.place(x=0, y=0, width=windowWidth/2, height= windowHeight - 60)
right_frame.place(x=windowWidth/2, y=0, width=windowWidth/2, height=windowHeight - 60)

global log_label
log_label = Label(fg='#17445D', bg=LABELS_COLOR,master=mainwindow, font=(Font_1, 14), text='Log Label Text')
log_label.place(x=(-FILE_NAME_ENTRY_WIDTH*2+(windowWidth))/2, y=windowHeight - 60, width=FILE_NAME_ENTRY_WIDTH*2, height=FILE_NAME_ENTRY_HEIGHT)

global file_name_label
file_name_label = Label(bg=LEFT_FRAME_COLOR ,fg='white' ,master=left_frame, text='File Name:', font=(Font_1, 16))
file_name_label.place(x=35, y=20, width=FILE_NAME_ENTRY_WIDTH/2, height=FILE_NAME_ENTRY_HEIGHT)

global file_name_entry
file_name_entry = Entry(bg=ENTRY_COLOR,master=left_frame, font=(Font_1, 18))
file_name_entry.place(x=(-FILE_NAME_ENTRY_WIDTH+(windowWidth/2))/2 + 70, y=20, width=FILE_NAME_ENTRY_WIDTH, height=FILE_NAME_ENTRY_HEIGHT)

global open_file_button, create_file_button, insert_button, delete_button, search_button, delete_file_button
open_file_button   = Button(bg=BUTTONS_COLORS,master=left_frame, text='DELETE FILE', font=(Font_1,18), command=DeleteFile)
create_button      = Button(bg=BUTTONS_COLORS,master=left_frame, text=' OPEN ', font=(Font_1,18), command=OpenFile)
insert_button      = Button(bg=BUTTONS_COLORS,master=left_frame, text='CREATE', font=(Font_1,18), command=CreateFile)
delete_button      = Button(bg=BUTTONS_COLORS,master=left_frame, text='INSERT', font=(Font_1,18), command=InsertEnr)
search_button      = Button(bg=BUTTONS_COLORS,master=left_frame, text='SEARCH', font=(Font_1,18), command=SearchEnr)
delete_file_button = Button(bg=BUTTONS_COLORS,master=left_frame, text='DELETE', font=(Font_1,18), command=DeleteEnr)

create_button.place(x=30, y=FILE_NAME_ENTRY_HEIGHT + 50, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
delete_button.place(x=30, y=FILE_NAME_ENTRY_HEIGHT + 50 + BUTTON_HEIGHT+ 30, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
search_button.place(x=300, y=FILE_NAME_ENTRY_HEIGHT + 50 + BUTTON_HEIGHT+ 30, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
delete_file_button.place(x=30, y=FILE_NAME_ENTRY_HEIGHT + 50 + (BUTTON_HEIGHT + 30)*2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
insert_button.place(x=300, y=FILE_NAME_ENTRY_HEIGHT + 50, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
open_file_button.place(x=300, y=FILE_NAME_ENTRY_HEIGHT + 50 + (BUTTON_HEIGHT  + 30)*2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

global informations_frame
informations_frame = Frame(master=mainwindow, background=LABELS_COLOR)
informations_frame.place(x=30, y=FILE_NAME_ENTRY_HEIGHT + 50 + (BUTTON_HEIGHT  + 30)*2 + 80, width=INFORMATION_FRAME_WIDTH ,height=INFORMATION_FRAME_HEIGHT)

global display_label
display_label = Label(master=right_frame, text='', bg=LABELS_COLOR, font=(Font_1, 18))
display_label.place(x= 30, y=50, width=DISPLAY_LABEL_WIDTH, height=windowHeight - 150)




mainwindow.mainloop()