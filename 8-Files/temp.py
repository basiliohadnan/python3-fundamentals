import os

#Main program
def main():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is its definition?\n')

    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the 'acronyms.txt' file
    file_path = os.path.join(script_dir, 'acronyms.txt')

    with open(file_path, 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

main()