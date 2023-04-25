print("Welcome to the fantasy game character creator! \n Let's name the brave adventurers:\n")
character_1 = input("Please name the first character:")
character_2 = input("Please name the second character:")
character_3 = input("Please name the third character:")
character_4 = input("Please name the fourth character:")
character_5 = input("Please name the fifth character:")

print("***Your characters are complete***\n")

import random

# CHARACTER 1 

luck = random.randint(1,3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

character_type = ""
if luck == 1:
    character_type = "Warrior"
    strength *= 3
elif luck == 2:
    character_type = "Wizard"
    magic *= 3
else:
    character_type = "Potato"
    health *= 3

print(character_1 + " is a " + character_type)
print("Strength: ", strength)
print("Magic: ", magic)
print("Health: ", health)


# CHARACTER 2

luck = random.randint(1,3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

character_type = ""
if luck == 1:
    character_type = "Warrior"
    strength *= 3
elif luck == 2:
    character_type = "Wizard"
    magic *= 3
else:
    character_type = "Potato"
    health *= 3

print(character_2 + " is a " + character_type)
print("Strength: ", strength)
print("Magic: ", magic)
print("Health: ", health)


# CHARACTER 3

luck = random.randint(1,3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

character_type = ""
if luck == 1:
    character_type = "Warrior"
    strength *= 3
elif luck == 2:
    character_type = "Wizard"
    magic *= 3
else:
    character_type = "Potato"
    health *= 3

print(character_3 + " is a " + character_type)
print("Strength: ", strength)
print("Magic: ", magic)
print("Health: ", health)


# CHARACTER 4

luck = random.randint(1,3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

character_type = ""
if luck == 1:
    character_type = "Warrior"
    strength *= 3
elif luck == 2:
    character_type = "Wizard"
    magic *= 3
else:
    character_type = "Potato"
    health *= 3

print(character_4 + " is a " + character_type)
print("Strength: ", strength)
print("Magic: ", magic)
print("Health: ", health)


# CHARACTER 5

luck = random.randint(1,3)  # gives a random integer
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

character_type = ""
if luck == 1:
    character_type = "Warrior"
    strength *= 3
elif luck == 2:
    character_type = "Wizard"
    magic *= 3
else:
    character_type = "Potato"
    health *= 3

print(character_5 + " is a " + character_type)
print("Strength: ", strength)
print("Magic: ", magic)
print("Health: ", health)