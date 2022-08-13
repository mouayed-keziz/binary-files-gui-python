from pickle import dumps, loads
from sys import getsizeof
from os import path, remove, system


global nombre_de_caracteristique
nombre_de_caracteristique = 2




global Taille_Buf
Taille_Buf = 30

Chaine = '#' * Taille_Buf

global buf
Tbloc = [0, Chaine]

global blocsize
blocsize = getsizeof(dumps(Tbloc))



#Recuperer le num de l'enregistrement e
def get_num(e) : 
    if e[0] == '@':
        e = e[1:]
    return int(e[:e.find(':')])

def find_nth(haystack, needle, n):
    if n == 0:
        return 0
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def sizeRest(buf_content):
    if '#' in buf_content:
        return len(buf_content[buf_content.find('#'):])
    else:
        return 0

def get_enr(buf_content, index):
     return ( buf_content[find_nth(buf_content, '@', index):find_nth(buf_content, '@', index + 1)] )

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


def affichier_fichier(file_name, FileExtension):  # sourcery skip: aug-assign
    result = ''
    if path.isfile('Binary Data\\'+file_name+FileExtension):
        with open('Binary Data\\'+file_name+FileExtension, 'rb') as file:
            caracteristique_0 = entete(file, 0)
            result = result + file_name + FileExtension+'\n'
            result = result + f'car_0:{entete(file, 0)}  car_1:{entete(file, 1)}\n'
            for i in range(caracteristique_0):
                buf = lireBloc(file, i)
                buf_nb = buf[0]
                buf_content = buf[1]
                result = result + str(buf_content)+'\n'
                #for _ in range(buf_nb):
                #    result = result + str(buf_content[:buf_content.find('@')]) + '\n'
                #    buf_content = buf_content[buf_content.find('@')+1:]
            result = result + '\n\n\n'
            for i in range(caracteristique_0):
                buf = lireBloc(file, i)
                buf_nb = buf[0]
                buf_content = buf[1]
                for _ in range(buf_nb):
                    result = result + str(buf_content[:buf_content.find('@')]) + '\n'
                    result = result.replace(':', ' ')
                    result = result.replace('%', ' ')
                    buf_content = buf_content[buf_content.find('@')+1:]



    return result