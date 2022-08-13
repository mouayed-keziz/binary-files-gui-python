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
Tetud = tnum + tnom + taffiliation            #Taille d'un enregistrements
Tnreg = '#' * Tetud                                     #enregistrement = chaine de caractaires de # repeté (Taille d'un enregistrements fois)
nombre_de_caracteristique = 2

global buf                                              #le buffer du programme (global)
Tbloc = [0, [Tnreg] * b]                                #C'est le bloc ou Tbloc[0] est NB et Tbloc[1] est une list d'enregistrements(list de chaines de caractaires)

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
#filename , file
def entete(file,offset):
    dp = offset * getsizeof(dumps(0))
    file.seek(dp, 0)
    c = file.read(getsizeof(dumps(0)))
    return loads(c)


def addSpace(s, k):
    return s[:k] + ' ' + s[k:]

def afficher_fichier(file_name, FileExtension):
    result = ''
    #system('cls')
    with open('Binary Data\\'+file_name+FileExtension,'rb') as file:
        caracteristique1 = entete(file,0)
        caracteristique2 = entete(file,1)
        result = result + file_name + FileExtension + '\n'
        result += f'car_0:{entete(file, 0)}  car_1:{entete(file, 1)}\n'
        for i in range(caracteristique1):
            buf = lireBloc(file, i)
            buf_nb = buf[0]
            buf_tab = buf[1]
            for j in range(buf_nb):
                s = addSpace(buf[1][j], tnum)
                s = addSpace(s, tnum + 1 + tnom)
                result = result + s.replace('#', '') + '\n'
            result += '\n'
    return result












'''
def créer_fichier(file_name):
    j = 0
    i = 0
    n = 0
    buf_tab = [Tnreg] * b
    buf_nb = 0
    try:
        f = open('Binary Data\\'+file_name+FileExtension, 'wb')
    except:
        print('impossible d\'ouvrir le fichier en mode d\'écriture ')
    rep = 'O'
    while (rep == 'O'):
        system('cls')
        print('Entrer les information de l\'étudiant: ')
        num = int(input('Enter le numéro d\'inscription : '))
        #nom = input('Enter le nom: ')
        #prénom = input('Entrer le prénom: ')
        #affiliation = input('Entrer l\'affiliation: ')
        nom= str(num)
        prénom = str(num)
        affiliation = str(num)
        num = resize_chaine(str(num), tnum)
        nom = resize_chaine(nom, tnom)
        prénom = resize_chaine(prénom, tprénom)
        affiliation = resize_chaine(affiliation, taffiliation)
        etud = str(num) + nom + prénom + affiliation
        n += 1
        if (j < b):
            buf_tab[j] = etud
            buf_nb += 1
            j += 1
        else:
            buf = [buf_nb, buf_tab]
            ecrireBloc(f,i,buf)
            buf_tab = [Tnreg] * b
            buf_nb = 1
            buf_tab[0] = etud
            j = 1
            i += 1
        rep = input('Avez vous un autre élement à entrer O/N: ').upper()

    buf = [j,buf_tab]
    ecrireBloc(f,i,buf)
    affecter_entete(f,0,i+1)
    affecter_entete(f,1,n)
    f.close()
'''