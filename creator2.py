import random

# Ask the user for five character names
print('Welcome to the fantasy game character creator!')
print("Let's name the brave adventurers:\n")
character_1 = input('Please name the first character: ')
character_2 = input('Please name the second character: ')
character_3 = input('Please name the third character: ')
character_4 = input('Please name the fourth character: ')
character_5 = input('Please name the fifth character: ')

print('\n***YOUR CHARACTERS ARE COMPLETE***\n')


def character_creator(char_name):
    """
    The user input will be randomly a warrior, wizard or potato with the respective
    stats of strength, magic and health according to the character
    """

    # A character will randomly be a Warrior, Wizard or Potato
    luck = random.randint(1,3)

    # Each character has stats: Health, Strength and Magic;
    # Each stat is random, between 5 and 10 
    strength = random.randint(5,10)
    magic = random.randint(5,10)
    health = random.randint(5,10)

    # A character will randomly be a Warrior, Wizard or Potato
    character_type = ""
    if luck == 1:
        character_type = "Warrior"
        strength *= 3                  # Warriors will have triple Strength
    elif luck == 2:
        character_type = "Wizard"
        magic *= 3                      # Wizards will have triple Magic
    else:
        character_type = "Potato"
        health *= 3                     # Potatoes will have triple Health

    # Generate the team of five characters
    print(f'"{char_name}" is a {character_type}!')
    print('     Strength: ', strength)
    print('     Magic: ', magic)
    print('     Health: ', health)

# Apply the function to the user input
character_creator(character_1)
character_creator(character_2)
character_creator(character_3)
character_creator(character_4)
character_creator(character_5)
