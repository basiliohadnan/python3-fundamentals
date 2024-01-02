import os

folder_original = "C:/Users/basil/OneDrive/Área de Trabalho/"
folder_destination = "C:/Users/basil/OneDrive/Área de Trabalho/CleanedUp/"

## Make the folder CleanedUp/
os.mkdir(folder_destination)

## List the files in the Desktop/ folder
for entry in os.scandir(folder_original):
## For each file in Desktop/ folder
    ## Move the file to the CleanedUp/ folder
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)