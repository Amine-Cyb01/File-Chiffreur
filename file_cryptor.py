import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import argparse

def generate_key(password: str, salt: bytes) -> bytes:
    return PBKDF2(password, salt, dkLen=32, count=1000000)

def encrypt_file(input_file: str, output_file: str, password: str):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    iv = os.urandom(16)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    with open(output_file, 'wb') as f:
        f.write(salt + iv + ciphertext)

def decrypt_file(input_file: str, output_file: str, password: str):
    with open(input_file, 'rb') as f:
        data = f.read()
    
    salt = data[:16]
    iv = data[16:32]
    ciphertext = data[32:]
    
    key = generate_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

def main():
    parser = argparse.ArgumentParser(description="Chiffreur/Déchiffreur de fichiers AES-256")
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help="Mode d'opération")
    parser.add_argument('-i', '--input', required=True, help="Fichier d'entrée")
    parser.add_argument('-o', '--output', required=True, help="Fichier de sortie")
    parser.add_argument('-p', '--password', required=True, help="Mot de passe de chiffrement")
    
    args = parser.parse_args()
    
    if args.mode == 'encrypt':
        encrypt_file(args.input, args.output, args.password)
    else:
        decrypt_file(args.input, args.output, args.password)

if __name__ == "__main__":
    main()
