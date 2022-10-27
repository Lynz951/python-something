Iteration 2 Pseudocode

Feature: Characters Have Classes
    - As a player I want a character to have a class that customizes its capabilities so that I can play more interesting characters

        Tests:
        - X changes in hit points
        - X changes in attack and damage
        - X increased critical range or damage
        - X bonuses/penalties versus other classes
        - X special abilities
        - X alignment limitations

Feature: As a player I want to play a Fighter so that I can kick ass and take names

        Tests:
        - X There is a Fighter class
        - X attacks roll is increased by 1 for every level instead of every other level
        - has 10 hit points per level instead of 5

Feature: As a player I want to play a Rogue so that I can defeat my enemies with finesse

        Tests:
        - does triple damage on critical hits
        - ignores an opponents Dexterity modifier (if positive) to Armor Class when attacking
        - adds Dexterity modifier to attacks instead of Strength
        - cannot have Good alignment

Feature: As a player I want to play a Monk so that I can enjoy being an Asian martial-arts archetype in a Medieval European setting

        Tests:
        - has 6 hit point per level instead of 5
        - does 3 points of damage instead of 1 when successfully attacking
        - adds Wisdom modifier (if positive) to Armor Class in addition to Dexterity
        - attack roll is increased by 1 every 2nd and 3rd level

Feature: As a player I want to play a Paladin so that I can smite evil, write wrongs, and be a self-righteous jerk

        Tests:
        - has 8 hit points per level instead of 5
        - +2 to attack and damage when attacking Evil characters
        - does triple damage when critting on an Evil character (i.e. add the +2 bonus for a regular attack, and then triple that)
        - attacks roll is increased by 1 for every level instead of every other level
        - can only have Good alignment