from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes
import os

def generate_key():
    key = os.urandom(32)  # 256 bits
    with open("aes.key", "wb") as f:
        f.write(key)
    return key

def load_key():
    with open("aes.key", "rb") as f:
        return f.read()

def encrypt_file(data):
    key = load_key()
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted

def decrypt_file(enc_data):
    key = load_key()
    iv = enc_data[:16]
    actual_data = enc_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted = decryptor.update(actual_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(decrypted) + unpadder.finalize()

def get_sha256(data):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(data)
    return digest.finalize().hex()
