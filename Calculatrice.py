#calculatrice simple(+,-,*,/)

#Fonction qui permet d'afficher le menu principal
def Afficher_menu_principal():
    print("Bienvenue dans la calculatrice")
    print("1.Calcul")
    print("2.Quitter")

#Fonction qui permet d'afficher le menu des opérations    
def Afficher_menu_opération():
    print("Opération possible")
    print("1.Addition")
    print("2.Soustraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quitter")

#Opération d'addition
#pré : a et b sont des int
#post : return a+b
def additionner(a,b):
    return a + b

#Opération de soustraction
#pré : a et b sont des int
#post : return a-b
def soustraction(a,b):
    return a - b

#Opération de multiplication
#pré : a et b sont des int
#post : return a*b
def multiplication(a,b):
    return a * b

#Opération de division
#pré : a et b sont des int
#post : return a/b
def division(a,b):
    if b == 0:
        print("Erreur, une division par 0 est impossible")
        return None
    else:
        return a / b
    
#Fonction demande nombre
def encodage_chiffre(message):
    while True:
        try:
            chiffre = int(input(message))
            return chiffre
        except ValueError:
            print("Erreur d'encodage. Veuillez écrire un nombre entier")


#main
def main():

    #boucle infini pour réafficher le menu
    while True:
        #afficher menu principal
        Afficher_menu_principal()

        #input choix du sous-menu
        choix = input("Entrez votre choix : ")

        #menu du calcul
        if choix == '1':

            #input des 2 nombres, a et b pour le calcul
            a = encodage_chiffre("Entrez votre premier nombre : ")
            b = encodage_chiffre("Entrez votre second nombre : ")



            #afficher menu des opérations
            Afficher_menu_opération()

            #input choix de l'opération
            choix = input("Entrez votre choix : ")

            if choix == '1':
                print("L'addition de %d et %d est : %d" % (a,b, additionner(a,b)))
            elif choix == '2':
                print("La soustraction de %d et %d est : %d" % (a,b, soustraction(a,b)))
            elif choix == '3':
                print("La multiplication de %d et %d est : %d" % (a,b,multiplication(a,b)))
            elif choix == '4':
                if division(a,b) is not None:
                    print("La division de %d et %d est : %d" % (a,b,division(a,b)))
            elif choix == '5':
                print("Fermeture calculatrice. Au revoir!")
                break
            else :
                print("Choix invalide")  

        #menu de sortie
        elif choix == '2':
            print("Fermeture calculatrice. Au revoir!")
            break
        else :
            print("Choix invalide")



if __name__ == "__main__":
     main()


