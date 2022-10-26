
# create character class

class Character():
    modifiers = [-5,-4,-4,-3,-3,-2,-2,-1,-1,0,0,1,1,2,2,3,3,4,4,5]

    def __init__ (self, name_in, alignment_in):
        self.name = name_in
        self.alignment = alignment_in
        self.armor = 10
        self.hit_points = 5
        self.damage_points = 0
        self.is_alive= True
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.wisdom = 10
        self.intelligence = 10
        self.charisma = 10

    def modify_roll(self, roll, modifier):
        return roll + modifier

    def attack(self, roll, armor, opponent):
        modified_roll = self.modify_roll(roll, Character.modifiers[self.strength+1])
        if self.hit_points <= 0:
            self.is_alive = False
        if modified_roll >= 20:
            opponent.damage_points = opponent.damage_points * 2
            return "hit"
        if modified_roll > armor or modified_roll >= 20:
            opponent.damage_points = opponent.damage_points + 1
            return "hit"
       


            
    