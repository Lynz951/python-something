from evercraft import *

def test_passing():
    assert 42 == 42

def test_passing_2():
    assert 3 == 3

def test_character_class_fighter():
    assert Fighter("Fred", "Good", 5,5,5,5,5,5,5,5,5,5,5,5) != None

def test_fighter_has_level_roll_modifer_of_1():
    char3 = Fighter("Fred", "Good", 5,5,5,5,5,5,5,5,5,5,5,1)
    char3.level = 1
    assert char3.level_roll_modifier == 1

def test_fighter_gets_10_bonus_on_level_up():
    char3 = Fighter("Fred", "Good", 5,4,5,5,5,5,5,5,5,5,2999,3)
    char3.attack(5, 3, char1)
    assert char3.hit_points == 13

def test_character_class_rogue():
    assert Rogue("Fred", "Evil", 5,5,5,5,5,5,5,5,5,5,5,5) != None

def test_rogue_gets_3x_damage_on_critical_hit():
    char4 = Rogue("Fred", "Evil", 5,4,5,5,5,5,5,5,5,5,1,2)
    char1 = Character('George', 'Neutral', 3, 5, 10, True, 10, 12, 10, 10, 10, 10, 0, 1) 
    char4.attack(20,3,char1)
    assert char1.damage_points == 30

def test_rogue_not_good():
    assert Rogue.alignment != 'Good'

def test_character_class_monk():
    assert Monk("Fred", "Evil", 5,5,5,5,5,5,5,5,5,5,5,5) != None

def test_character_class_paladin():
    assert Paladin("Fred", "Good", 5,5,5,5,5,5,5,5,5,5,5,5) != None

def test_monk_gets_6_bonus_on_level_up():
    char3 = Monk("Fred", "Good", 5,4,5,5,5,5,5,5,5,5,2999,3)
    char3.attack(5, 3, char1)
    assert char3.hit_points == 9

def test_paladin_gets_8_bonus_on_level_up():
    char3 = Paladin("Fred", "Good", 5,4,5,5,5,5,5,5,5,5,2999,3)
    char3.attack(5, 3, char1)
    assert char3.hit_points == 11

def test_monk_does_3_plus_damage():
    char3 = Monk("Fred", "Good", 5,4,5,5,5,5,5,5,5,5,2999,3)
    char1 = Character('George', 'Neutral', 3, 5, 10, True, 10, 12, 10, 10, 10, 10, 0, 1) 
    char3.attack(5, 3, char1)
    assert char1.damage_points == 13

def test_paladin_only_good():
    assert Paladin.alignment != "Evil" 

def test_paladin_has_level_roll_modifer_of_1():
    char3 = Paladin("Fred", "Good", 5,5,5,5,5,5,5,5,5,5,5,1)
    char3.level = 1
    assert char3.level_roll_modifier == 1