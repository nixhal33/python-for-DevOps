import os

folders = input("Please provide me the list of folders that starts with spaces :- ").split()

for folder in folders:
    
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name to search!!")
        #continue
        break #to stop the program if wrong folder name is given let's try
    except PermissionError:
        print("No access to this folder as it may have root user :-" + folder)
  
    print("###############listing files for the folder :-" + folder)
    
    for file in files:
        print(file)
