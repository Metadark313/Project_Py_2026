#calculatrice simple

#afficher un menu
def Afficher_menu_1():
    print("Bienvenue dans la calculatrice")
    print("1.Calcul")
    print("2.Quitter")
    
def Afficher_menu_2():
    print("Opération possible")
    print("1.Addition")
    print("2.Soustraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quitter")

#Opérations
def additionner(a,b):
    print("L'addition de %d et %d est : %d" % (a,b, a+b))

def soustraction(a,b):
    print("La soustraction de %d et %d est : %d" % (a,b, a-b))

def multiplication(a,b):
    print("La multiplication de %d et %d est : %d" % (a,b,a*b))

def division(a,b):
    print("La division de %d et %d est : %d" % (a,b,a/b))


#main
def main():
    while True:
        Afficher_menu_1()

        choix = input("Entrez votre choix : ")

        if choix == '1':
            a = int(input("Entrez votre premier nombre : "))
            b = int(input("Entrez votre second nombre : "))
            Afficher_menu_2()

            choix = input("Entrez votre choix : ")

            if choix == '1':
                additionner(a,b)
            elif choix == '2':
                soustraction(a,b)
            elif choix == '3':
                multiplication(a,b)
            elif choix == '4':
                division(a,b)
            elif choix == '5':
                print("Fermeture calculatrice. Au revoir!")
                break
            else :
                print("Choix invalide")  

        elif choix == '2':
            print("Fermeture calculatrice. Au revoir!")
            break
        else :
            print("Choix invalide")



if __name__ == "__main__":
     main()


