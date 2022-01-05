from pick import pick


def fonction_shop(inventaire, argent, liste_item, liste_prix):
    global result

    title = f"\n Bienvenue dans le magasin, que souhaitez vous faire ? \n Vous avez {argent}€"
    print("Inventaire:", inventaire)
    print("Argent:", argent, "\n")
    options = ["Acheter", "Vendre", "Quitter"]

    choice_action, index = pick(
        options, title, indicator='=>', default_index=0)
    while choice_action != "quitter" or index == 2:
        if choice_action == "acheter" or index == 0:
            result = fonction_achat(inventaire, argent, liste_item, liste_prix)
            title = f"\n Bienvenue dans le magasin, que souhaitez vous faire ? \n Vous avez {result[1]}€"
            argent = result[1]
        elif choice_action == "vendre" or index == 1:
            result = fonction_vente(inventaire, argent, result[2])
            title = f"\n Bienvenue dans le magasin, que souhaitez vous faire ? \n Vous avez {result[1]}€"
            argent = result[1]

        if choice_action == "quitter" or index == 2:
            break
        choice_action, index = pick(
            options, title, indicator='=>', default_index=0)

    return inventaire, argent


def verif_item(choice, liste):
    i = 0
    while i < len(liste):
        if choice == liste[i]:
            return i
        else:
            i += 1
    return "non"


def fonction_achat(inventaire, argent, liste_item, liste_prix):
    credit = []
    title = f"Choisissez l'objet que vous souhaitez acheter ou quittez le mode achat en choisissant 'quitter' : \n Vous avez {argent}€"
    options = []
    for i in range(len(liste_item)):
        options.append(liste_item[i])
    options.append("quitter")
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    while choice != "quitter":
        i = verif_item(choice, liste_item)
        if i != "non":
            if argent >= liste_prix[i]:
                title2 = f"Vous avez {argent} €. \n L'objet {liste_item[i]} coûte {liste_prix[i]} € \n voulez-vous l'acheter ?"
                options2 = ["oui", "non"]
                choice2, index = pick(
                    options2, title2, indicator='=>', default_index=0)
                if choice2 == "oui":
                    inventaire.append(liste_item[i])
                    argent -= liste_prix[i]
                    credit.append(liste_prix[i])
                    title = f"Choisissez l'objet que vous souhaitez acheter ou quittez le mode achat en choisissant 'quitter' :\n --> paiement effectué, merci de votre achat ! \n Vous avez {argent}€"
                if choice2 == "non":
                    pass
            else:
                title = f"Choisissez l'objet que vous souhaitez acheter ou quittez le mode achat en choisissant 'quitter' :\n Vous avez {argent}€ \n L'objet {liste_item[i]} coûte {liste_prix[i]} € \n Vous n'avez pas assez d'argent pour acheter cet objet."
        choice, index = pick(
            options, title, indicator='=>', default_index=0)

    return inventaire, argent, credit


def fonction_vente(inventaire, argent, credit):
    title = f"Quel objet souhaitez-vous vendre ? Choisissez 'quitter' pour quitter le mode vente: \n Vous avez {argent}€"
    options = []
    for i in range(len(inventaire)):
        options.append(inventaire[i])
    options.append("quitter")
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    while choice != "quitter":
        i = verif_item(choice, inventaire)
        if i != "non":
            title2 = "Êtes-vous sûr de vouloir vendre cet objet, oui ou non ?"
            options2 = ["oui", "non"]
            choice_answer, index = pick(
                options2, title2, indicator='=>', default_index=0)
            if choice_answer == "oui":
                argent += credit[i]
                credit.remove(credit[i])
                inventaire.remove(inventaire[i])
                options.remove(options[i])
                title = f"Quel objet souhaitez-vous vendre ? Choisissez 'quitter' pour quitter le mode vente: \n Vous avez {argent}€"
            if choice_answer == "non":
                pass
        choice, index = pick(
            options, title, indicator='=>', default_index=0)

    return inventaire, argent
