import pikepdf
from tqdm import tqdm
import PyPDF2

#crea un file di testo con numeri da 1 a n
f = open("passwords.txt", "w")

for i in range (123400,123457):
    f.write(str(i)+"\n")

f.close()


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