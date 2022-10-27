# Pseudocode
## Iteration I

- Feature: Create a Character
    - As a character I want to have a name so that I can be distinguished from other characters
    - can get and set Name

    - Tests:
        - X 'Character' class exists
        - X Character.name exists
        - X Character name can be set

- Feature: Alignment
    - As a character I want to have an alignment so that I have something to guide my actions

    - Tests:
        - X Character class has alignment attribute
        - X Character.alignment can be set
        - X Character.alignment = ["Good", "Evil", "Neutral"]

- Feature: Armor Class & Hit Points
    - As a combatant I want to have an armor class and hit points so that I can resist attacks from my enemies

    - Tests:
        - X Character class has armor class
        - X Character.armor = 10 (default)
        - X Character class has hit points attribute
        - X Character.hit_points = 5 (default)

- Feature: Character Can Attack
    - As a combatant I want to be able to attack other combatants so that I can survive to fight another day

    - Tests:
        - X Character class has an attack() method
        - X Character.attack(roll) accepts a dice roll as parameter (1-20)
        - X Character.attack(roll, opp_armor) accepts opponent's armor class as parameter
        - X Character.attack() should check for roll=20 and return 'hit'
        - X Character.attack() should compare roll and opp_armor and return 'hit' if roll>opp_armor

- Feature: Character Can Be Damaged
    - As an attacker I want to be able to damage my enemies so that they will die and I will live

    - Tests:
        - X Character() has damage_points attribute
        - X If char1.attack() returns 'hit', char2.damage_points = char2.damage_points+1 (Might need to revisit)
        - X If char1.attack.roll == 20, char2.damage_points = char2.damage_points*2
        - X Character() has alive? attribute
        - L If char2.hit_points <=0, alive? = False

- Feature: Character Has Abilities Scores
    - As a character I want to have several abilities so that I am not identical to other characters except in name

    - Tests:
        - X Character() has strength attribute = (1 - 20) 10 (default)
        - X Character() has dexterity attribute = (1 - 20) 10 (default)
        - X Character() has constitution attribute = (1 - 20) 10 (default)
        - X Character() has wisdom attribute = (1 - 20) 10 (default)
        - X Character() has intelligence attribute = (1 - 20) 10 (default)
        - X Character() has charisma attribute = (1 - 20) 10 (default)

            Abilities have modifiers according to the following table (Revisit)
            Score	Modifier
            1   	-5	
            2   	-4	
            3   	-4	
            4	    -3	
            5   	-3	
            6       -2
            7      -2
            8      -1
            9      -1
            10      0
            11      0
            12      1
            13      1
            14      2
            15      2
            16      3
            17      3
            18      4
            19      4
            20      5

- Feature: Character Ability Modifiers Modify Attributes
    - As a character I want to apply my ability modifiers improve my capabilities in combat so that I can vanquish my enemy with extreme prejudice

    - Tests:
        - X Character.attack() if successful --> minimum damage = 1
        - X Character.attack() ---> Add strength modifier to roll and damage dealt (Revisit)
        - X If Character.attack roll = 20, add 2x strength modifier
        - X Character.armor = Character.armor + dexterity modifier
        - X Character.hit_points = Character.hit_points + constitution modifier

- Feature: A Character can gain experience when attacking
    - As a character I want to accumulate experience points (xp) when I attack my enemies so that I can earn bragging rights at the tavern

    - Tests:
        - X Character() has experience_points attribute
        - X If Character.attack() successful, Character.experience_points = +10

- Feature: A Character Can Level
    - As a character I want my experience points to increase my level and combat capabilities so that I can bring vengeance to my foes

    - Tests:
        - X Character() has a level attribute
        - X Character.level = 1 (default)
        - X Every time Character.experience_points increases by 1000, Character.level = +1
        - X Every time Character.experience_points increases by 1000, Character.hit_points = +5 + .constitution_modifier
        - X 1 is added to attack roll for every even level achieved
        

         