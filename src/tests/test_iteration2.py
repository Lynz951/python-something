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
    char3 = Fighter("Fred", "Good", 5,5,5,5,5,5,5,5,5,5,2999,3)
    char3.attack(5, 3, char1)
    assert char3.hit_points == char3.hit_points + 10 + char3.modifiers[char3.constitution+1]
