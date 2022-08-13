
from Tableaux_Taille_Fixe import *
from os import path, system

FileExtension = '.t_of'


def recherche(file_name, cle):
    if path.isfile('Binary Data\\'+file_name):
        with open('Binary Data\\'+file_name, 'rb') as file:
            caracteristique_0 = entete(file, 0)
            for i in range(caracteristique_0):
                buf = lireBloc(file, i)
                buf_nb = buf[0]
                buf_tab = buf[1]
                for j in range(buf_nb):
                    if get_num(buf_tab[j]) == cle:
                        return [True, i, j]
    return [False]


def insertion(file_name, e):
    #search = recherche('Binary Data\\'+file_name+FileExtension, get_num(e))
    search = recherche(file_name, get_num(e))
    if not search[0]:
        if not path.isfile('Binary Data\\'+file_name):
            with open('Binary Data\\'+file_name, 'wb') as file:
                affecter_entete(file, 0, 0)
                affecter_entete(file, 1, 0)
        with open('Binary Data\\'+file_name, 'rb+') as file:
            car_0 = entete(file, 0)
            car_1 = entete(file, 1)
            if car_0 == 0:
                buf = [0, [Tnreg] * b]
                buf[0] = 1
                buf[1][0] = e
                ecrireBloc(file, 0, buf)
                affecter_entete(file, 0, 1)
                affecter_entete(file, 1, 1)

            else:
                buf = lireBloc(file, car_0 - 1)
                nb = buf[0]
                tab = buf[1]
                if nb < b:
                    tab[nb] = e
                    nb = nb + 1
                    buf = [nb, tab]
                    ecrireBloc(file, car_0 - 1, buf)
                else:
                    tab = [Tnreg] * b
                    tab[0] = e
                    nb = 1
                    buf = [nb, tab]
                    ecrireBloc(file, car_0 , buf)
                    affecter_entete(file, 0, car_0 + 1)
                affecter_entete(file, 1, car_1 + 1)


def supression(file_name, cle):
    search = recherche(file_name, cle)
    if search[0]:
        with open('Binary Data\\'+file_name, 'rb+') as file:
            car0 = entete(file, 0)
            lastBlock = lireBloc(file, car0 - 1)
            if search[1] == car0 - 1 and search[2] == lastBlock[0] - 1:
                lastBlock[1][search[2]] = Tnreg
                lastBlock[0] -= 1
                if lastBlock[0] == 0:
                    affecter_entete(file, 0, car0 - 1)
                else:
                    ecrireBloc(file, car0 - 1, lastBlock)
            
            else:
                e = lastBlock[1][lastBlock[0] - 1]
                lastBlock[1][lastBlock[0] - 1] = Tnreg
                lastBlock[0] -= 1
                if lastBlock[0] == 0:
                    affecter_entete(file, 0, car0 - 1)
                else:
                    ecrireBloc(file, car0 - 1, lastBlock)
                
                buf = lireBloc(file, search[1])
                buf[1][search[2]] = e
                ecrireBloc(file, search[1], buf)
            affecter_entete(file, 1, entete(file, 1) - 1)





#e = '20########5###################5###################5###################'
#
#system('cls')
#insertion('file_1', e)
#afficher_fichier('file_1')
