# -*- coding:UTF8 -*-
#145 429
#10.11 Écrivez une fonction chaineListe() qui convertisse une phrase en une liste de mots.



def chaineListe(chaine):
    ma_liste=[]
    mot = ""
    preced = '*'
    if chaine[0]==" ":
        preced = " "
    nb_mots = 0
    for car in chaine:
        if car == "\n" or car == "'":
            car = " "
        if car != ' ' and preced != ' ':
            # on est dans un mot
            mot = mot + car
        if car == ' ' and preced == ' ':
            # on est dans une suite de blancs
            instr = 1
        if car == ' ' and preced != ' ':
            # on termine un mot
            nb_mots += 1
            preced = ' '
            print(mot + "  " + str(nb_mots))
            ma_liste.append(mot)
            mot = ""
        if car != ' ' and preced == ' ':
            # on attaque un nouveau mot
            preced = '*'
            mot = car
    if preced != ' ':
        nb_mots+=1
        print(mot + "  " + str(nb_mots))
        ma_liste.append(mot)
    return ma_liste

        

if __name__ == "__main__":
    chainew='''LE LOUP ET L'AGNEAU (*)

La raison du plus fort est toujours la meilleure :
            Nous l'allons montrer tout à l'heure (1).
            Un Agneau se désaltérait
            Dans le courant d'une onde pure.
Un Loup survient à jeun, qui cherchait aventure,
       Et que la faim en ces lieux attirait.
Qui te rend si hardi (2) de troubler mon breuvage ?
            Dit cet animal plein de rage :
Tu seras châtié de ta témérité.
Sire, répond l'Agneau, que Votre Majesté
            Ne se mette pas en colère ;
            Mais plutôt qu'elle considère
            Que je me vas (3) désaltérant
                         Dans le courant,
            Plus de vingt pas au-dessous d'Elle ;
Et que par conséquent, en aucune façon,
            Je ne puis troubler sa boisson.
Tu la troubles, reprit cette bête cruelle,
Et je sais que de moi tu médis l'an passé.
Comment l'aurais-je fait si (4) je n'étais pas né ?
       Reprit l'Agneau ; je tette encor ma mère
            Si ce n'est toi, c'est donc ton frère.
       Je n'en ai point. C'est donc quelqu'un des tiens:
            Car vous ne m'épargnez guère,
            Vous, vos Bergers et vos Chiens.
On me l'a dit : il faut que je me venge."
           Là-dessus, au fond des forêts
            Le loup l'emporte et puis le mange,
            Sans autre forme de procès.'''


    chaine2='''    LE LOUP ET L'AGNEAU (*)

La raison du plus fort est toujours la meilleure :
            Nous l'allons montrer tout à l'heure (1).
            Un Agneau se désaltérait'''
    
##    ma_liste=[]
##    mot = ""
##    preced = '*'
##    if chaine[0]==" ":
##        preced = " "
##    nb_mots = 0
##    for car in chaine:
##        if car == "\n":
##            car = " "
##        if car != ' ' and preced != ' ':
##            # on est dans un mot
##            mot = mot + car
##        if car == ' ' and preced == ' ':
##            # on est dans une suite de blancs
##            instr = 1
##        if car == ' ' and preced != ' ':
##            # on termine un mot
##            nb_mots += 1
##            preced = ' '
##            print(mot + "  " + str(nb_mots))
##            ma_liste.append(mot)
##            mot = ""
##        if car != ' ' and preced == ' ':
##            # on attaque un nouveau mot
##            preced = '*'
##            mot = car
##
##    if preced != ' ':
##        nb_mots+=1
##        print(mot + "  " + str(nb_mots))
##        ma_liste.append(mot)
        
    ma_liste=chaineListe(chainew)
    print(ma_liste)
    nb_mots=len(ma_liste)
    print(str(nb_mots))
    




        

