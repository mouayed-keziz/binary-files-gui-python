from Tableau_Taille_Variable import *
from os import path, system

FileExtension = '.tov_c'


def recherche(file_name, cle):
    if not path.isfile('Binary Data\\' + file_name + FileExtension):
        return [False, 0, 0]
    trouv = False
    stop = False
    with open('Binary Data\\'+file_name,'rb') as file:
        bs = entete(file, 0) - 1
        bi = 0
        while bi <= bs and not trouv and not stop:
            i = (bi + bs) // 2
            buf = lireBloc(file, i)
            buf_nb = buf[0]
            buf_content = buf[1]
            if cle >= get_num(get_enr(buf_content, 0)) and cle <= get_num(get_enr(buf_content, buf_nb - 1)):
                inf = 0
                sup = buf_nb - 1
                while inf <= sup and not trouv:
                    j = (inf + sup) // 2
                    if cle == get_num(get_enr(buf_content, j)):
                        trouv = True
                    elif cle < get_num(get_enr(buf_content, j)):
                        sup = j - 1
                    else:
                        inf = j + 1
                if (inf > sup):
                    j = inf
                    stop = True
            elif cle < get_num(get_enr(buf_content, 0)):
                bs = i - 1
            else:
                bi = i + 1
        if bi > bs:
            i = bi
            j = 0
    return [trouv, i, j]



def insertion(file_name, e):  # sourcery no-metrics
    e = e + '@'
    l = []
    search = recherche(file_name, get_num(e))
    trouv = search[0]
    i = search[1]
    j = search[2]
    if not trouv:
        if not path.isfile('Binary Data\\'+file_name):
            with open('Binary Data\\'+file_name, 'wb') as file:
                affecter_entete(file, 0, 0)
                affecter_entete(file, 1, 0)
        with open('Binary Data\\'+file_name, 'rb+') as file:
            car_0 = entete(file, 0)
            car_1 = entete(file, 1)

            if car_0 == 0:
                buf_nb = 1
                buf_content = Chaine
                buf_content = e + buf_content[len(e):]
                buf = [buf_nb, buf_content]
                ecrireBloc(file, 0, buf)
                affecter_entete(file, 0, 1)
                affecter_entete(file, 1, 1)
                return
            
            if i == car_0:
                buf_nb = 1
                buf_content = Chaine
                buf_content = e + buf_content[len(e):]
                buf = [buf_nb, buf_content]
                ecrireBloc(file, i, buf)
                affecter_entete(file, 0, car_0 + 1)
                affecter_entete(file, 1, car_1 + 1)
                return

            buf = lireBloc(file, i)
            buf_nb = buf[0]
            buf_content = buf[1]
            
            
            if j == buf_nb:
                if sizeRest(buf_content) >= len(e):
                    buf_nb += 1
                    buf_content = buf_content[:buf_content.rfind('@')+1] + e + buf_content[buf_content.rfind('@') + 1 + len(e):]
                    buf = [buf_nb, buf_content]
                    ecrireBloc(file, i, buf)
                    affecter_entete(file, 1, car_1 + 1)
                else:
                    if i == car_0 - 1:
                        pass
                    else:
                        buf = lireBloc(file, i+1)
                        buf_nb = buf[0]
                        buf_content = buf[1]
                        for k in range(0, buf_nb):
                            enr = get_enr(buf_content, k)
                            if enr[0] == '@':
                                enr = enr[1:]
                            l.append(enr)
                        buf_nb = 1
                        buf_content = e + Chaine[len(e):]
                        buf = [buf_nb, buf_content]
                        ecrireBloc(file, i+1, buf)
                        affecter_entete(file, 1, car_1 + 1 - len(l))
                        for e in l:
                            insertion(file_name, e)
                        
            else:
                for k in range(j, buf_nb):
                    enr = get_enr(buf_content, k)
                    if enr[0] == '@':
                        enr = enr[1:]
                    l.append(enr)
                buf_nb = j+1
                buf_content = buf_content[:find_nth(buf_content, '@', j)]
                buf_content = buf_content + Chaine[len(buf_content):]
                buf_content = buf_content[:buf_content.rfind('@')+1] + e + buf_content[buf_content.rfind('@') + 1 + len(e):]
                buf = [buf_nb, buf_content]
                ecrireBloc(file, i, buf)
                affecter_entete(file, 1, car_1 + 1 - len(l))
                for e in l:
                    insertion(file_name, e)




def suppression(file_name, cle):
    pass



#FileName = 'test'
#system('cls')
#e = '1:111'
#
#
#
#
#
#
#for i in range(-3, 14, 2):
#    #break
#    #print(i,' : ',recherche(FileName, i))
#    insertion(FileName, e.replace('1', str(i)))
#affichier_fichier(FileName, FileExtension)