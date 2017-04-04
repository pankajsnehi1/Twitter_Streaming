Name = ""
Desc = ""
Gender = ""
Race = ""

# Prompt user for user-defined information
Name = input('What is your Name? ')
Desc = input('Describe yourself: ')
Gender = input('What Gender are you? (male / female / unsure): ')
Race = input('What fantasy Race are you? - (Pixie / Vulcan / Gelfling / Troll): ')

# Output the character sheet
line = "<~~==|#|==~~++**\@/**++~~==|#|==~~>"
print("\n", line)
print("\t", Name)
print("\t", Race, Gender)
print("\t", Desc)
print(line, "\n")