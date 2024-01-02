import os
import shutil

def organize_desktop(desktop_path):
    # Define subfolder names
    image_folder = "Images"
    document_folder = "Documents"
    zip_folder = "Archives"

    # Create subfolders if they don't exist
    subfolders = [image_folder, document_folder, zip_folder]
    for folder in subfolders:
        folder_path = os.path.join(desktop_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    # List all files on the desktop
    entries = os.scandir(desktop_path)

    for entry in entries:
        if entry.is_file():
            # Get file extension
            _, file_extension = os.path.splitext(entry.name)

            # Move files to corresponding subfolders
            if file_extension.lower() in (".jpg", ".jpeg", ".png", ".gif", ".bmp"):
                move_to_folder(entry.path, os.path.join(desktop_path, image_folder))
            elif file_extension.lower() in (".doc", ".docx", ".pdf", ".txt"):
                move_to_folder(entry.path, os.path.join(desktop_path, document_folder))
            elif file_extension.lower() == ".zip":
                move_to_folder(entry.path, os.path.join(desktop_path, zip_folder))

def move_to_folder(source_path, destination_folder):
    # Move file to destination folder
    destination_path = os.path.join(destination_folder, os.path.basename(source_path))
    print(source_path, "  |  " ,destination_path)
    shutil.move(source_path, destination_path)

if __name__ == "__main__":
    # Specify your desktop path
    desktop_path = "C:/Users/basil/OneDrive/Área de Trabalho/"

    # Organize files on the desktop
    organize_desktop(desktop_path)
