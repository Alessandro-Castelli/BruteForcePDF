import pikepdf
from tqdm import tqdm
import PyPDF2

#copio il file con le password su una lista
#in questo caso il file passwords.txt contiene le 100000 password più usate ad oggi nel mondo
passwords = [line.strip() for line in open("passwords.txt")]
print(passwords)

#iniziamo a ciclare le password
key = ""
for password in tqdm(passwords, "Decrypting PDF:"):
    try:
        #apro il file pdf da forzare
        with pikepdf.open("eiei.pdf", password=password) as pdf:
            key = password
            print("Password trovata: ", password)
            break
    except pikepdf.PasswordError as e:
        continue

if key == "" :
    print("Mi dispiace compa non l'ho trovata... che te devo di... prova con qualche altra combinazione")