from Tableau_Taille_Variable import *
from os import path, system

FileExtension = '.t_ov_c'


def recherche(file_name, cle):
    if path.isfile('Binary Data\\'+file_name):
        with open('Binary Data\\'+file_name, 'rb') as file:
            caracteristique_0 = entete(file, 0)
            for i in range(caracteristique_0):
                buf = lireBloc(file, i)
                buf_nb = buf[0]
                buf_content = buf[1]
                for j in range(buf_nb):
                    e = buf_content[:buf_content.find('@')]
                    if get_num(e) == cle:
                        return [True, i, j]
                    buf_content = buf_content[buf_content.find('@')+1:]
    return [False]


def insertion(file_name, e):  # sourcery no-metrics
    search = recherche(file_name, get_num(e))
    e = e + '@'
    if not search[0]:
        if not path.isfile('Binary Data\\'+file_name):
            with open('Binary Data\\'+file_name, 'wb') as file:
                affecter_entete(file, 0, 0)
                affecter_entete(file, 1, 0)
        with open('Binary Data\\'+file_name, 'rb+') as file:
            car_0 = entete(file, 0)
            car_1 = entete(file, 1)
            if car_0 == 0:
                if len(e) > Taille_Buf:
                    print('Taille kbira bzf')
                else:
                    buf_nb = 1
                    buf_content = Chaine
                    buf_content = e + buf_content[len(e):]
                    buf = [buf_nb, buf_content]
                    ecrireBloc(file, 0, buf)
                    affecter_entete(file, 0, 1)
            else:
                isInsert = False
                for i in range(car_0):
                    buf = lireBloc(file, i)
                    buf_nb = buf[0]
                    buf_content = buf[1]
                    if '#' in buf_content:
                        sizeRest = len(buf_content[buf_content.find('#'):])
                    else:
                        sizeRest = 0
                    if sizeRest >= len(e):
                        buf_content = buf_content[:buf_content.rfind('@')+1] + e + buf_content[buf_content.rfind('@') + 1 + len(e):]
                        buf_nb += 1
                        buf = [buf_nb, buf_content]
                        ecrireBloc(file, i, buf)
                        isInsert = True
                        break
                if not isInsert:
                    buf_nb = 1
                    buf_content = Chaine
                    buf_content = e + buf_content[len(e):]
                    buf = [buf_nb, buf_content]
                    ecrireBloc(file, car_0, buf)
                    affecter_entete(file, 0, car_0 + 1)
            affecter_entete(file, 1, car_1 + 1)
    else:
        print('element found')

def suppression(file_name, cle):
    search = recherche(file_name, cle)
    if search[0]:
        with open('Binary Data\\'+file_name, 'rb+') as file:
            car_0 = entete(file, 0)
            i = search[1]
            j = search[2]
            buf = lireBloc(file, i)
            buf_nb = buf[0]
            buf_content = buf[1]
            firstAT = find_nth(buf_content, '@', j)
            secondAT = find_nth(buf_content, '@', j+1)
            if j == 0:
                secondAT += 1
            buf_content = buf_content[:firstAT] + buf_content[secondAT:] + ((secondAT - firstAT) * '#')
            buf_nb -= 1
            buf = [buf_nb, buf_content]
            if buf_nb != 0:
                ecrireBloc(file, i, buf)
            else:
                if i != car_0:
                    lastBloc = lireBloc(file, car_0 - 1)
                    ecrireBloc(file, i, lastBloc)
                affecter_entete(file, 0, car_0 - 1)
            affecter_entete(file, 1, entete(file, 1) - 1)
    else:
        print('element not found')


#FileName = 'test'
#system('cls')
#s = [0,0,0,0,0,0,0,0,0,0]
#s[0] = '0:00000000'
#s[1] = '1:11111'
#s[2] = '2:2'
#s[3] = '3:33'
#s[4] = '4:4444444444'
#s[5] = '5:555555555555555555'
#s[6] = '6:666'
#s[7] = '7:77777'
#s[8] = '8:88'
#s[9] = '9:9'
#
#
#for i in s:
#    pass
#    #insertion(FileName, i)
##
##for i in range(-3, 15):
#    pass
#    #print(i,recherche(FileName, i))
#    #insertion(FileName, s[i])
#    #suppression(FileName, i)
#
#
#affichier_fichier(FileName, FileExtension)
#
#suppression(FileName, 7)
#insertion(FileName, s[4])
#
#affichier_fichier(FileName, FileExtension)
#
#suppression_fichier('Binary Data\\'+FileName+FileExtension)
#