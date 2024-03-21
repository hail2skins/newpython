# Ask the user what acronym they want to add
acronym = input('What acronym do you want to add?\n')
definition = input('What is the definition?\n')
with open('software_acronyms.txt', 'a') as file:
    file.write(f"{acronym} - {definition}\n")

