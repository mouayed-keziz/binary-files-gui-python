from Listes_Taille_Fixe import *
from os import path, system


FileExtension = '.l_of'

def recherche(file_name, cle):
    if path.isfile('Binary Data\\'+file_name):
        with open('Binary Data\\'+file_name, 'rb') as file:
            i = entete(file, 2)
            while i != -1:
                buf = lireBloc(file, i)
                for j in range(buf[0]):
                    if get_num(buf[1][j]) == cle:
                        return [True, i, j]
                i = buf[2]
            
    return [False]



def insertion(file_name, e):
    search = recherche(file_name, get_num(e))
    if not search[0]:
        if not path.isfile('Binary Data\\'+file_name):
            with open('Binary Data\\'+file_name, 'wb') as file:
                affecter_entete(file, 0, 0)
                affecter_entete(file, 1, 0)
                affecter_entete(file, 2, -1)
        with open('Binary Data\\'+file_name, 'rb+') as file:
            car_0 = entete(file, 0)
            car_1 = entete(file, 1)
            car_2 = entete(file, 2)
            if car_2 == -1:
                buf = [0, [Tnreg] * b, 0]
                buf[0] = 1
                buf[1][0] = e
                buf[2] = -1
                ecrireBloc(file, 0, buf)
                affecter_entete(file, 0, 1)
                affecter_entete(file, 1, 1)
                affecter_entete(file, 2, 0)

            else:
                i = car_2
                prec = i
                while i != -1:
                    buf = lireBloc(file, i)
                    prec = i
                    i = buf[2]
                nb = buf[0]
                tab = buf[1]
                if nb < b:
                    tab[nb] = e
                    nb = nb + 1
                    buf = [nb, tab, -1]
                    ecrireBloc(file, prec, buf)
                else:
                    tab = [Tnreg] * b
                    tab[0] = e
                    nb = 1
                    buf[2] = car_0
                    buf = [nb, tab, -1]
                    precbuf = lireBloc(file, prec)
                    precbuf[2] = car_0
                    ecrireBloc(file, prec, precbuf)
                    ecrireBloc(file, car_0 , buf)
                    affecter_entete(file, 0, car_0 + 1)
                affecter_entete(file, 1, car_1 + 1)
    else:
        print('element found xDDD jajajajajajajajazjajajaja')




def suppression(file_name, cle):
    search = recherche(file_name, cle)
    #if element found : delete it
    if search[0]:
        #delete that element
        with open('Binary Data\\'+file_name, 'rb+') as file:
            car_0 = entete(file, 0)
            car_1 = entete(file, 1)
            car_2 = entete(file, 2)
            
            last = index_of_last_block(file)
            lastBlock = lireBloc(file, last)

            #if the element we want to delete is the last element in the file
            if search[1] == last and search[2] == lastBlock[0] - 1:
                #delete it
                lastBlock[1][search[2]] = Tnreg
                lastBlock[0] -= 1
                #if the block is empty
                if lastBlock[0] == 0:
                    #delete the block
                    beforeLast = index_of_before_last_block(file)
                    if beforeLast == -1:
                        affecter_entete(file, 2, -1)
                    else:
                        beforeLastBlock = lireBloc(file, beforeLast)
                        beforeLastBlock[2] = -1
                        ecrireBloc(file, beforeLast, beforeLastBlock)
                    affecter_entete(file, 0, car_0 - 1)
                else:
                    #else: write it back
                    ecrireBloc(file, last, lastBlock)
            
            else:
                e = lastBlock[1][lastBlock[0] - 1]
                lastBlock[1][lastBlock[0] - 1] = Tnreg
                lastBlock[0] -= 1
                if lastBlock[0] == 0:
                    #delete the block
                    beforeLast = index_of_before_last_block(file)
                    if beforeLast == -1:
                        affecter_entete(file, 2, -1)
                    else:
                        beforeLastBlock = lireBloc(file, beforeLast)
                        beforeLastBlock[2] = -1
                        ecrireBloc(file, beforeLast, beforeLastBlock)
                    affecter_entete(file, 0, car_0 - 1)
                else:
                    #else: write it back
                    ecrireBloc(file, last, lastBlock)
                
                buf = lireBloc(file, search[1])
                buf[1][search[2]] = e
                ecrireBloc(file, search[1], buf)
            affecter_entete(file, 1, entete(file, 1) - 1)




#system('cls')
#e = '1#########1###################1###################1###################'.replace('1', '1')
#fileName = 'test'

#for i in range(1,9):
#    insertion(fileName, e.replace('1', str(i)))
#with open('Binary Data\\'+fileName, 'rb') as file:
#    a = get_index(file, -1)
#    print(a)
#
#for i in range(10):
#    suppression(fileName, i)
#suppression2(fileName, 3)
#affichier_fichier(fileName, FileExtension)
#
#
#
#suppression_fichier('Binary Data\\'+fileName)



