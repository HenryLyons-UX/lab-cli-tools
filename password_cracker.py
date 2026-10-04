from zipfile import ZipFile, BadZipFile
import zlib

def password_reader():
    passwords = []
    with open('Ashley-Madison.txt') as file:
        for line in file:
            passwords.append(line.strip())
    return passwords


def white_house(passwords):
    for password in passwords:
        try:
            with ZipFile('whitehouse_secrets.zip') as zf:
                zf.extractall(pwd=password.encode())
            print("Password found:", password)
            break
        except(RuntimeError, BadZipFile, zlib.error):
            continue
passwords = password_reader()
white_house(passwords)