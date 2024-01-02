import os

def find_acronym():
    look_up = input('What software acronym would you like to look up?\n')

    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the 'acronyms.txt' file
    file_path = os.path.join(script_dir, 'acronyms.txt')

    found = False
    try:
        with open(file_path) as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found!')
        return
    
    if not found:
        print('Acronym not found!')

def add_acronym():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is its definition?\n')

    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the 'acronyms.txt' file
    file_path = os.path.join(script_dir, 'acronyms.txt')

    with open(file_path, 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    choice = input('Do you want to find(F) or add(A) an acronym?\n')
    choice = choice.upper()
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()
    else:
        print('Option does not exist!')
        main()
main()