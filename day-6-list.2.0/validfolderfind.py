# using proper functions to find the folder in the given directory

import os

# this function only contains the exception handling part only.
def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "No folder found!"
    except PermissionError:
        return None, "You cannot access this Folder as it is accessed by root user only"


# Main function where the prime operations are happening.
def main():
    folder_paths = input("Enter the valid folder path separated by spaces: ").split()

    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in '{folder_path}---->{error_message}'")

if __name__=="__main__":
    main()