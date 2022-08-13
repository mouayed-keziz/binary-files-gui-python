from Listes_Taille_Fixe import *
from os import path, system


FileExtension = '.lof'


def recherche(file_name, cle):
    if not path.isfile('Binary Data\\' + file_name):
        return [False, 0, 0]
    trouv = False
    stop = False
    j = 0
    with open('Binary Data\\'+file_name,'rb') as file:
        try:
            if entete(file, 0) == 0 : return [False, 0, 0]
        except:
            return [False, 0, 0]
        bs = entete(file,0) - 1
        bi = 0
        while bi <= bs and not trouv and not stop:
            i=(bs+bi)//2
            buf=lireBloc(file, get_index(file, i))
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
        return [trouv,get_index(file, i),j]



def insertion(file_name, e):  # sourcery no-metrics
    search = recherche(file_name, get_num(e))
    if not search[0]:
        if not path.isfile('Binary Data\\'+file_name):
            with open('Binary Data\\'+file_name, 'wb') as file:
                affecter_entete(file, 0,  0)
                affecter_entete(file, 1,  0)
                affecter_entete(file, 2, -1)
        with open('Binary Data\\'+file_name, 'rb+') as file: 
            i = search[1]
            j = search[2]
            continu = True
            if entete(file, 2) == -1:
                buf = [1, [Tnreg] * b, -1]
                buf[1][0] = e
                ecrireBloc(file, 0, buf)
                affecter_entete(file, 0, 1)
                affecter_entete(file, 1, 1)
                affecter_entete(file, 2, 0)
                return
            while continu and i != -1:
                buf = lireBloc(file, i)
                buf_nb = buf[0]
                buf_tab = buf[1]
                buf_suiv = buf[2]
                x = buf_tab[buf_nb-1]
                k = buf_nb-1
                if j == buf_nb:
                    buf_tab[j] = e
                    buf_nb += 1
                    buf = [buf_nb, buf_tab, buf_suiv]
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
                        buf = [buf_nb, buf_tab, buf_suiv]
                        ecrireBloc(file, i, buf)
                        continu = False
                    else:
                        buf = [buf_nb, buf_tab, buf_suiv]
                        ecrireBloc(file, i, buf)
                        i = lireBloc(file, i)[2]
                        j = 0
                        e = x
            if i == -1:
                buf_tab = [Tnreg] * b
                buf_tab[0] = e
                buf_nb = 1
                buf = [buf_nb, buf_tab, -1]
                lastBloc = lireBloc(file, get_index(file, entete(file, 0) - 1))
                lastBloc[2] = entete(file, 0)
                ecrireBloc(file, get_index(file, entete(file, 0) - 1), lastBloc)
                ecrireBloc(file, entete(file, 0), buf)
                affecter_entete(file, 0, entete(file, 0) + 1)
            affecter_entete(file, 1, entete(file, 1) + 1)
    else:
        print('element found, so we can not insert it')


def suppression(file_name, cle):
    search = recherche(file_name, cle)
    trouv = search[0]
    if trouv:
        i = search[1]
        j = search[2]
        with open('Binary Data\\'+file_name, 'rb+') as file:
            buf = lireBloc(file, i)
            buf_nb = buf[0]
            buf_tab = buf[1]
            buf_suiv = buf[2]
            if j == buf_nb - 1:
                buf_tab[j] = Tnreg
            else:
                k = j
                while k < buf_nb-1:
                    buf_tab[k] = buf_tab[k+1]
                    k += 1
                buf_tab[k] = Tnreg
            buf_nb -= 1
            buf = [buf_nb, buf_tab, buf_suiv]
            if buf_nb == 0:
                #delete this block
                if i == entete(file, 2):
                    affecter_entete(file, 2, lireBloc(file, i)[2])
                elif i == get_index(file, entete(file, 0) - 1):
                    h = entete(file, 2)
                    while lireBloc(file, h)[2] != i:
                        h = lireBloc(file, h)[2]
                    buf = lireBloc(file, h)
                    buf[2] = -1
                    ecrireBloc(file, h, buf)
                else:
                    beforeLast = entete(file, 2)
                    while lireBloc(file, beforeLast)[2] != get_index(file, entete(file, 0) - 1):
                        beforeLast = lireBloc(file, beforeLast)[2]

                    beforeI = entete(file, 2)
                    while lireBloc(file, beforeI)[2] != get_index(file, i):
                        beforeI = lireBloc(file, beforeI)[2]

                    beforeIbuf = lireBloc(file, beforeI)
                    beforeIbuf[2] = lireBloc(file, beforeIbuf[2])[2]
                    ecrireBloc(file, beforeI, beforeIbuf)
                    lastBuf = lireBloc(file, lireBloc(file, beforeLast)[2])
                    beforeLastBuf = lireBloc(file, beforeLast)
                    beforeLastBuf[2] = i
                    ecrireBloc(file, i, lastBuf)
                    ecrireBloc(file, beforeLast, beforeLastBuf)

                    
                    
                    

                affecter_entete(file, 0, entete(file, 0) - 1)
            else:
                ecrireBloc(file, i, buf)
            affecter_entete(file, 1, entete(file, 1) - 1)



def test(FileName):
    e = '1#########1###################1###################1###################'
    l0 = [0 ,[Tnreg] * b, -1]
    l1 = [0 ,[Tnreg] * b, -1]
    l2 = [0 ,[Tnreg] * b, -1]

    l0[0] = 3
    l1[0] = 1
    l2[0] = 2

    l0[1][0] = e.replace('1', '1')
    l0[1][1] = e.replace('1', '3')
    l0[1][2] = e.replace('1', '4')
    l1[1][0] = e.replace('1', '7')
    l2[1][0] = e.replace('1', '10')
    l2[1][1] = e.replace('1', '13')
    l2[1][2] = e.replace('1', '15')

    l0[2] = 0
    l1[2] = 2
    l2[2] = -1

    with open('Binary Data\\'+FileName, 'wb') as file:
        affecter_entete(file, 1, 3)
        affecter_entete(file, 0, 3)
        affecter_entete(file, 2, 1)
        ecrireBloc(file, 1, l0)
        ecrireBloc(file, 0, l1)
        ecrireBloc(file, 2, l2)


#system('cls')
#e = '1#########1###################1###################1###################'
#FileName = 'test'
#
#
#for i in range(-2, 18, 2):
#    pass
#    #suppression(FileName, i)
#    #insertion(FileName, e.replace('1', str(i)))
#    #print(i, ' : ', recherche(FileName, i))
#
#
#suppression(FileName, 17)
#insertion(FileName, e.replace('1', '-1'))
#test(FileName)
#
#
#affichier_fichier(FileName, FileExtension)
#
#test(FileName)
#
#affichier_fichier(FileName, FileExtension)
#
#for i in range(-3, 20):
#    print(i, ' : ', recherche(FileName, i))