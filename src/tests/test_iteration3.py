from evercraft import *
import math

def test_passing():
    assert 42 == 42

def test_orc_gets_plus_2_strength():
    char10 = Character("Bob", "Neutral", 5,5,5,True,5,5,5,5,5,5,5,1)
    char10.is_an_orc()
    assert char10.strength == 7

def test_orc_intelligence_minus_1():
    char10 = Character("Bob", "Neutral", 5,5,5,True,5,5,5,5,5,5,5,1)
    char10.is_an_orc()
    assert char10.intelligence == 4

def test_orc_wisdom_minus_1():
    char10 = Character("Bob", "Neutral", 5,5,5,True,5,5,5,5,5,5,5,1)
    char10.is_an_orc()
    assert char10.wisdom == 4

def test_orc_charisma_minus_1():
    char10 = Character("Bob", "Neutral", 5,5,5,True,5,5,5,5,5,5,5,1)
    char10.is_an_orc()
    assert char10.charisma == 4

def test_orc_armor_plus_2():
    char10 = Character("Bob", "Neutral", 5,5,5,True,5,5,5,5,5,5,5,1)
    char10.is_an_orc()
    assert char10.armor == 7

def test_orc_is_an_orc():
    char10 = Character("Bob", "Neutral", 5,5,5,True,5,5,5,5,5,5,5,1)
    char10.is_an_orc()
    assert char10.race == "Orc"

# def test_monk_orc_armor_plus_2():
#     char10 = Monk("Bob", "Neutral", 5,5,5,True,5,5,5,5,5,5,5,1)
#     char10.is_an_orc()
#     char10.attack(5,4,char1)
#     assert char10.armor == 5