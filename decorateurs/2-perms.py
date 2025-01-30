def is_admin(func):
    def wrapper(role):
        if role == "admin":
            func()
        else:
            print("Vous n'avez pas la permission")
    return wrapper

@is_admin
def creer_fichier():
    print("Fichier créer !")

@is_admin
def modifier_fichier():
    print("Modifier supprimé !")

@is_admin
def supprimer_fichier():
    print("Fichier supprimé !")

creer_fichier("user")
modifier_fichier("user")
supprimer_fichier("admin")