from evercraft import *

# def test_passing():
#     assert 42 == 42

def test_character_class():
    assert Character("Fred", "Good") != None

def test_character_name_set():
    new_char = Character("Larry", "Evil")
    assert new_char.name == "Larry"

def test_character_alignment():
    char1 = Character("Larry", "Neutral")
    assert char1.alignment != None

def test_character_alignment_set():
    char1 = Character("Larry", "Good")
    assert char1.alignment == "Good"

def test_character_alignment_values():
    char1 = Character("Larry", "Good")
    assert char1.alignment == "Good" or "Evil" or "Neutral"

def test_character_has_armor():
    char1 = Character("Fred", "Neutral")
    assert char1.armor != None

def test_character_has_armor_value():
    char1 = Character("Fred", "Neutral")
    assert char1.armor == 10

def test_character_has_hit_points():
    char1 = Character("Fred", "Neutral")
    assert char1.hit_points != None

def test_character_hit_points_value():
    char1 = Character("Fred", "Neutral")
    assert char1.hit_points == 5 

def test_character_has_attack_method():
    char1 = Character("Fred", "Neutral")
    assert char1.attack != None

def test_character_has_attack_roll_value():
    char1 = Character("Fred", "Neutral")
    char2 = Character("Wilma", "Evil")
    char1.attack(4, 3, char2)
    assert char1.attack != 0

def test_character_has_attack_opp_armor_value():
    char1 = Character("Fred", "Neutral")
    char2 = Character("Wilma", "Evil")
    assert char1.attack(4, 3, char2) != 0

def test_attack_roll_20():
    char1 = Character("Fred", "Neutral")
    char2 = Character("Wilma", "Evil")
    char1.attack(20, 4, char2) != 0
    assert char1.attack(20, 4, char2) == 'hit'

def test_attack_roll_greater_than_opp_armor():
    char1 = Character("Fred", "Neutral")
    char2 = Character("Wilma", "Evil")
    assert char1.attack(5, 4, char2) == 'hit'

def test_character_has_damage_points():
    char1 = Character("Fred", "Neutral")
    assert char1.damage_points != None

def test_character_attack_damage_plus_one():
    char1 = Character("Fred", "Neutral")
    char2 = Character("Wilma", "Evil")
    char2_preattack_damage = char2.damage_points
    char1.attack(8, 3, char2)
    assert char2.damage_points == char2_preattack_damage + 1

def test_character_attack_damage_times_2():
    char1 = Character("Fred", "Neutral")
    char2 = Character("Wilma", "Evil")
    char2_preattack_damage = char2.damage_points
    char1.attack(20, 3, char2)
    assert char2.damage_points == char2_preattack_damage * 2

def test_character_has_attack_method():
    char1 = Character("Fred", "Neutral")
    assert char1.is_alive != None

def test_character_hit_points_value_dead():
    char1 = Character("Fred", "Neutral")
    char2 = Character("Wilma", "Evil")
    char1.attack(20, 3, char2)
    char1.hit_points = 0
    char1.is_alive = False

def test_character_has_strength():
    char1 = Character("Fred", "Neutral")
    assert char1.strength != None

def test_character_has_dexterity():
    char1 = Character("Fred", "Neutral")
    assert char1.dexterity != None

def test_character_has_constitution():
    char1 = Character("Fred", "Neutral")
    assert char1.constitution != None

def test_character_has_wisdom():
    char1 = Character("Fred", "Neutral")
    assert char1.wisdom != None

def test_character_has_intelligence():
    char1 = Character("Fred", "Neutral")
    assert char1.intelligence != None

def test_character_has_charisma():
    char1 = Character("Fred", "Neutral")
    assert char1.charisma != None

def test_character_minimum_damage():
    char1 = Character("Fred", "Neutral")
    char2 = Character("Wilma", "Evil")
    char1.attack(18, 3, char2)
    char1.hit_points = 0
    assert char2.damage_points >= 1

def test_rolled_num_gets_modifier():
    char1 = Character("Fred", "Neutral")
    char2 = Character("Wilma", "Evil")
    rolled_num = 18
    modifiers = 3
    modified_roll = char1.modify_roll(rolled_num, modifiers)
    assert modified_roll == 21

def test_armor_equals_armor_plus_dexterity_mod():
    char1 = Character("Larry", "Good")
    char2 = Character("Bob", "Neutral")
    old_armor = char1.armor
    char1.attack(15, 4, char2)
    assert char1.armor == old_armor + char1.modifiers[char1.dexterity+1]

def test_hp_equals_hp_plus_const_mod():
    char1 = Character("Larry", "Good")
    char2 = Character("Bob", "Neutral")
    old_hp = char1.hit_points
    char1.attack(15, 4, char2)
    assert char1.hit_points == old_hp + char1.modifiers[char1.constitution+1]

def test_character_has_experience_points():
    char1 = Character("Fred", "Neutral")
    assert char1.experience_points != None

def test_character_experience_points_increase():
    char1 = Character("Larry", "Good")
    char2 = Character("Bob", "Neutral")
    char1.experience_points = 0
    char1.attack(15, 4, char2)
    assert char1.experience_points == 10


