from pickle import dumps,loads
from sys import getsizeof
from os import path, remove, system

global b
global tnom
global tprénom
global tnuminscpt 
global taffiliation
global nombre_de_caracteristique

b = 3                                                   #Taille max du bloc
tnum = 10                                               #Taille max du num
tnom = 40                                               #Taille max du nom
taffiliation = 20                                       #Taille max de l'affiliation
Tetud = tnum + tnom  + taffiliation            #Taille d'un enregistrements
Tnreg = '#' * Tetud                                     #enregistrement = chaine de caractaires de # repeté (Taille d'un enregistrements fois)
nombre_de_caracteristique = 3

global buf                                              #le buffer du programme (global)
Tbloc = [0, [Tnreg] * b, 0]                             #C'est le bloc ou Tbloc[0] est NB et Tbloc[1] est une list d'enregistrements(list de chaines de caractaires) et Tbloc[2] est l'indice du block suivant

global blocsize                                         #Taille d'un bloc (global)
blocsize=getsizeof(dumps(Tbloc))+len(Tnreg)*(b-1)+(b-1) #Calculer la taille d'un bloque en binaire


#Recuperer le num de l'enregistrement e
def get_num(e) : return int(e[:tnum].replace('#', ''))


#Complete le reste du chaine de caractaires avec '#' (jusqu'à la taille max)
def resize_chaine(chaine, maxtaille):
    for _ in range(len(chaine),maxtaille):
          chaine=chaine+'#' 
    return chaine


#Supprimer le fichier file_name
def suppression_fichier(file_name):
    remove(file_name)

#Supprimer le contenu du fichier file_name
def suppression_contenu(file_name):
    with open(file_name, 'wb') as file : pass

#Lire le bloc dans la position i dans le fichier file
def lireBloc(file, i):
    dp = nombre_de_caracteristique * getsizeof(dumps(0)) + i * blocsize
    file.seek(dp, 0)
    buf = file.read(blocsize)
    return (loads(buf))


#Ecrire le contenue du buffer dans le bloc dans la position i dans le fichier file
def ecrireBloc(file, i, bf):
    dp = nombre_de_caracteristique * getsizeof(dumps(0)) + i * blocsize
    file.seek(dp, 0)
    file.write(dumps(bf))


#Affecter la valeur c à la caracteristique numero 'of' de l'entete du fichier file
def affecter_entete(file, of, c):
    dp= of * getsizeof(dumps(0))
    file.seek(dp, 0)
    file.write(dumps(c))


#Lire la caracteristique numero 'offset' de l'entete du fichier file
def entete(file,offset):
    dp = offset * getsizeof(dumps(0))
    file.seek(dp, 0)
    c = file.read(getsizeof(dumps(0)))
    return loads(c)


def index_of_last_block(file_ptr):
    car_2 = entete(file_ptr, 2)
    i = car_2
    if i == -1:
        return (-1)
    while lireBloc(file_ptr, i)[2] != -1:
        i = lireBloc(file_ptr, i)[2]
    return i

def index_of_before_last_block(file_ptr):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    car_2 = entete(file_ptr, 2)
    i = car_2
    if i != -1 and lireBloc(file_ptr, i)[2] != -1:
        while lireBloc(file_ptr, lireBloc(file_ptr, i)[2])[2] != -1:
            i = lireBloc(file_ptr, i)[2]
        return i
    else:
        return (-1)



def get_index(file, num):
    num += 1
    car0 = entete(file, 0)
    car2 = entete(file, 2)
    if num > car0 or num <= 0:#condition my friend
        return -1

    k = 0
    i = car2
    while i != -1:
        k += 1
        if k == num:
            return i
        i = lireBloc(file, i)[2]




def addSpace(s, k):
    return s[:k] + ' ' + s[k:]


def affichier_fichier(file_name, FileExtension):
    result = ''
    if path.isfile('Binary Data\\'+file_name+FileExtension):
        with open('Binary Data\\'+file_name+FileExtension, 'rb') as file:
            i = entete(file, 2)
            result = result + file_name + FileExtension+'\n'
            result = result + f'car_0:{entete(file, 0)}  car_1:{entete(file, 1)}  car_2:{entete(file, 2)}\n'
            while i != -1:
                buf = lireBloc(file, i)
                for j in range(buf[0]):
                    s = addSpace(buf[1][j], tnum)
                    s = addSpace(s, tnum + 1 + tnom)
                    result = result + s.replace('#', '') + '\n'
                result = result + '\n'
                i = buf[2]
    return result

