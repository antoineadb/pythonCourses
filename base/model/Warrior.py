from base.model.Player import Player


class Warrior(Player):

    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo,health, attack)
        self.armor = 3
        print("Bienvenu au Guerrier",pseudo,"/ Points de vie:",health, "/Attaque:", attack)

    def damage(self,damage):
        if self.armor > 0:
            self.armor -=1
            damage = 0
        super().damage(damage)    

    def attack_player(self,target_player):
        target_player.damage(self.attack)

    def blade(self):
        self.armor = 3
        print("Les points d'armure ont été rechagés")

    def get_armore_point(self):
        return self.armor

warrior = Warrior("DarkWarrior", 30,4)
warrior.damage(4)
print("vie", warrior.get_health(),"armure:",warrior.get_armore_point())
warrior.damage(4)
print("vie", warrior.get_health(),"armure:",warrior.get_armore_point())
warrior.damage(4)
print("vie", warrior.get_health(),"armure:",warrior.get_armore_point())

if issubclass(Warrior,Player):
    print("Le guerrier est bien une spécialisation de player")