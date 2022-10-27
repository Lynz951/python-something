
# create character class

class Character():
    modifiers = [-5,-4,-4,-3,-3,-2,-2,-1,-1,0,0,1,1,2,2,3,3,4,4,5]
    alignment = ['Good', 'Neutral', 'Evil']

    def __init__ (self, name_in, alignment_in, armor_in, hit_points_in, damage_points_in, is_alive_in, strength_in, dexterity_in, constitution_in, wisdom_in, intelligence_in, charisma_in, experience_points_in, level_in):
        self.name = name_in
        self.alignment = alignment_in
        self.armor = armor_in
        self.hit_points = hit_points_in
        self.damage_points = damage_points_in
        self.is_alive= is_alive_in
        self.strength = strength_in
        self.dexterity = dexterity_in
        self.constitution = constitution_in
        self.wisdom = wisdom_in
        self.intelligence = intelligence_in
        self.charisma = charisma_in
        self.experience_points = experience_points_in
        self.level = level_in
        self.level_roll_modifier = self.level // 2

    def modify_roll(self, roll, modifier):
        if roll == 20:
            modified_roll = 20
        else:
            modified_roll = roll + modifier + self.level_roll_modifier
        return modified_roll

    def attack(self, roll, armor, opponent):
        modified_roll = self.modify_roll(roll, Character.modifiers[self.strength+1])
        if self.hit_points <= 0:
            self.is_alive = False
        if modified_roll >= 20:
            if isinstance(self, Rogue):
                opponent.damage_points = opponent.damage_points * 3
            else:
                opponent.damage_points = opponent.damage_points * 2
            self.armor = self.armor + Character.modifiers[self.dexterity+1]
            self.hit_points = self.hit_points + Character.modifiers[self.constitution+1]
            self.experience_points = self.experience_points +10
            if self.experience_points//1000+1 > self.level:
                self.level_up()
            return "hit"
        if modified_roll > armor:
            if isinstance(self, Monk):
                opponent.damage_points = opponent.damage_points + 3
            else:
                opponent.damage_points = opponent.damage_points + 1
            self.armor = self.armor + Character.modifiers[self.dexterity+1]
            self.hit_points = self.hit_points + Character.modifiers[self.constitution+1]
            self.experience_points = self.experience_points +10
            if self.experience_points//1000+1 > self.level:
                self.level_up()
            return "hit"
   
    def level_up(self):
        self.level += 1
        if isinstance(self, Fighter):
            self.hit_points = self.hit_points + 10 + self.modifiers[self.constitution+1]
        elif isinstance(self, Monk):
            self.hit_points = self.hit_points + 6 + self.modifiers[self.constitution+1]
        elif isinstance(self, Paladin):
            self.hit_points = self.hit_points + 8 + self.modifiers[self.constitution+1]
        
        self.hit_points = self.hit_points + 5 + self.modifiers[self.constitution+1]


class Fighter(Character):
    def __init__(self, name_in, alignment_in, armor_in, hit_points_in, damage_points_in, is_alive_in, strength_in, dexterity_in, constitution_in, wisdom_in, intelligence_in, charisma_in, experience_points_in, level_in):
        super().__init__(name_in, alignment_in, armor_in, hit_points_in, damage_points_in, is_alive_in, strength_in, dexterity_in, constitution_in, wisdom_in, intelligence_in, charisma_in, experience_points_in, level_in)
        self.level_roll_modifier = self.level

class Rogue(Character):
    
    def __init__(self, name_in, alignment_in, armor_in, hit_points_in, damage_points_in, is_alive_in, strength_in, dexterity_in, constitution_in, wisdom_in, intelligence_in, charisma_in, experience_points_in, level_in):
        super().__init__(name_in, alignment_in, armor_in, hit_points_in, damage_points_in, is_alive_in, strength_in, dexterity_in, constitution_in, wisdom_in, intelligence_in, charisma_in, experience_points_in, level_in)
        self.alignment = ['Neutral', 'Evil']

class Monk(Character):
    def __init__(self, name_in, alignment_in, armor_in, hit_points_in, damage_points_in, is_alive_in, strength_in, dexterity_in, constitution_in, wisdom_in, intelligence_in, charisma_in, experience_points_in, level_in):
        super().__init__(name_in, alignment_in, armor_in, hit_points_in, damage_points_in, is_alive_in, strength_in, dexterity_in, constitution_in, wisdom_in, intelligence_in, charisma_in, experience_points_in, level_in)

class Paladin(Character):
    def __init__(self, name_in, alignment_in, armor_in, hit_points_in, damage_points_in, is_alive_in, strength_in, dexterity_in, constitution_in, wisdom_in, intelligence_in, charisma_in, experience_points_in, level_in):
        super().__init__(name_in, alignment_in, armor_in, hit_points_in, damage_points_in, is_alive_in, strength_in, dexterity_in, constitution_in, wisdom_in, intelligence_in, charisma_in, experience_points_in, level_in)
        self.alignment = ['Good']
   
char1 = Character('George', 'Neutral', 3, 5, 10, True, 10, 12, 10, 10, 10, 10, 0, 1)
char2 = Character('Fred', 'Good', 10, 5, 10, True, 10, 10, 10, 10, 10, 10, 0, 1)




            
    