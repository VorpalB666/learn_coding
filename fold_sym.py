from cryptography.fernet import Fernet
import argparse, subprocess, os

def encrypt(to_entcrypt):
    filename = to_entcrypt.split("/"[-1])
    filename = str(filename).strip("['").strip("']")
        
    key = Fernet.generate_key()

    with open(f"{filename}.secret.key", "wb") as key_file:
        key_file.write(key)

    cipher_suite = Fernet(key)

    with open(to_entcrypt, "rb") as file:
        data = file.read()

    encrypted_data = cipher_suite.encrypt(data)

    with open(f"encrypted_{filename}".strip("[").strip("]"), "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def fold_enc(folder_path):
    files = os.listdir(folder_path)

    d = "encrypted"
    parent_d = str(folder_path)
    path = os.path.join(parent_d, d)
    os.mkdir(path)

    k = "keys"
    key_path = os.path.join(path, k)
    os.mkdir(key_path)

    f = "files"
    file_path = os.path.join(path, f)
    os.mkdir(file_path)

    for file in files:
        key = Fernet.generate_key()
        filename = str(file).split("/")[-1]

        with open(f"{key_path}/{file}.secret.key", "wb") as key_file:
            os.chdir(key_path)
            key_file.write(key)

        cipher_suite = Fernet(key)

        with open(f"{folder_path}/{file}", "rb") as e_file:
            data = e_file.read()

        encrypted_data = cipher_suite.encrypt(data)

        with open(f"{file_path}/encrypted_{filename}", "wb") as encrypted_file:
            os.chdir(file_path)
            encrypted_file.write(encrypted_data)

def decrypt(to_decrypt, key_path):
    filename = to_decrypt.split("/")[-1]

    with open(to_decrypt, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

    with open(key_path, "rb") as key_file:
            key = key_file.read()

    cipher_suite = Fernet(key)
    decrytped_data = cipher_suite.decrypt(encrypted_data)

    with open(f"decrypted_{filename}", "wb") as decrypted_file:
         decrypted_file.write(decrytped_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verschlüsseln und Entschlüsseln von Dateien")
    parser.add_argument("--encrypt", type=str, help="Pfad der zu verschlüsselnden Datei")
    parser.add_argument("--fold_enc", type=str, help="Pfad des Ordners, in dem alle Dateien verschlüsselt werden sollen")
    parser.add_argument("--decrypt", type=str, help="Pfad der zu entschlüsselnden Datei")
    parser.add_argument("--key", type=str, help="Pfad zum Schlüssel für die Entschlüsselung")

    args = parser.parse_args()

if args.encrypt:
    encrypt(args.encrypt)
elif args.fold_enc:
    fold_enc(args.fold_enc)
elif args.decrypt and args.key:
    decrypt(args.decrypt, args.key)
else:
    parser.error("Der Schalter --decrypt muss zusammen mit --key verwendet werden")
