
from Tableaux_Taille_Fixe import *
from os import path, system

FileExtension = '.tof'


def recherche(file_name,cle):
    if not path.isfile('Binary Data\\' + file_name):
        return [False, 0, 0]
    trouv = False
    stop = False
    j = 0
    with open('Binary Data\\'+file_name,'rb') as file:
        if entete(file, 0) == 0:
            return [False, 0, 0]
        bs = entete(file,0) - 1
        bi = 0
        while bi <= bs and not trouv and not stop:
            i=(bs+bi)//2
            buf=lireBloc(file, i)
            buf_nb = buf[0]
            buf_tab = buf[1]
            if cle >= get_num(buf_tab[0]) and cle <= get_num(buf_tab[buf_nb-1]):
                inf= 0
                sup= buf_nb - 1
                while inf <= sup and not trouv:
                    j=(inf+sup)//2
                    if cle == get_num(buf_tab[j]):
                        trouv=True
                    elif cle < get_num(buf_tab[j]):
                        sup=j-1
                    else:
                        inf=j+1
                if(inf>sup):
                    j=inf
                    stop = True
            elif cle < get_num(buf_tab[0]):
                bs=i-1
            else:
                bi=i+1
        if bi > bs :
            if buf_nb == b:
                i = bi 
                j = 0
            elif cle > get_num(buf_tab[0]): 
                j = buf_nb
    return [trouv,i,j]



def insertion(file_name, e):
    search = recherche(file_name, get_num(e))
    trouv = search[0]
    i = search[1]
    j = search[2]
    if not trouv:
        with open('Binary Data\\'+file_name, 'rb+') as file: 
            continu = True
            while continu and i < entete(file, 0):
                buf = lireBloc(file, i)
                buf_nb = buf[0]
                buf_tab = buf[1]
                x = buf_tab[buf_nb-1]
                k = buf_nb-1
                if j == buf_nb:
                    buf_tab[j] = e
                    buf_nb += 1
                    buf = [buf_nb, buf_tab]
                    ecrireBloc(file, i, buf)
                    continu = False
                else:
                    while k > j:
                        buf_tab[k] = buf_tab[k-1]
                        k -= 1
                    buf_tab[j] = e
                    if buf_nb < b:
                        buf_tab[buf_nb] = x
                        buf_nb += 1
                        buf = [buf_nb, buf_tab]
                        ecrireBloc(file, i, buf)
                        continu = False
                    else:
                        buf = [buf_nb, buf_tab]
                        ecrireBloc(file, i, buf)
                        i += 1
                        j = 0
                        e = x
            if i >= entete(file, 0):
                buf_tab = [Tnreg] * b
                buf_tab[0] = e
                buf_nb = 1
                buf = [buf_nb, buf_tab]
                ecrireBloc(file, i, buf)
                affecter_entete(file, 0, i+1)
            affecter_entete(file, 1, entete(file, 1) + 1)
    else:
        print('element found, so we can not insert it')


def supression(file_name, cle):
    search = recherche(file_name, cle)
    trouv = search[0]
    if trouv:
        i = search[1]
        j = search[2]
        with open('Binary Data\\'+file_name, 'rb+') as file:
            buf = lireBloc(file, i)
            buf_nb = buf[0]
            buf_tab = buf[1]
            if j == buf_nb - 1:
                buf_tab[j] = Tnreg
            else:
                k = j
                while k < buf_nb-1:
                    buf_tab[k] = buf_tab[k+1]
                    k += 1
                buf_tab[k] = Tnreg
            buf_nb -= 1
            buf = [buf_nb, buf_tab]
            if buf_nb == 0:
                if i != entete(file, 0) - 1:
                    for k in range(i, entete(file, 0) - 1):
                        ecrireBloc(file, k, lireBloc(file, k+1))
                affecter_entete(file, 0, entete(file, 0) - 1)
            else:
                ecrireBloc(file, i, buf)
            affecter_entete(file, 1, entete(file, 1) - 1)



#fileName = 'tof_recherche_test'
#e = '9#########5###################5###################5###################'
#system('cls')
#
#
##créer_fichier('tof_recherche_test')
#
##insertion(fileName, e)
#supression(fileName, 7)
#afficher_fichier(fileName)
##print(recherche(fileName, 14))