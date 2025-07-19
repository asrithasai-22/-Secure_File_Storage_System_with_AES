import os
import json
import time
from crypto_utils import encrypt_file, decrypt_file, get_sha256

ENC_DIR = "encrypted_files"
DEC_DIR = "decrypted_files"
META_FILE = "metadata.json"

def ensure_dirs():
    os.makedirs(ENC_DIR, exist_ok=True)
    os.makedirs(DEC_DIR, exist_ok=True)
    if not os.path.exists(META_FILE):
        with open(META_FILE, "w") as f:
            json.dump({}, f)

def load_metadata():
    with open(META_FILE, "r") as f:
        return json.load(f)

def save_metadata(meta):
    with open(META_FILE, "w") as f:
        json.dump(meta, f, indent=4)

def encrypt_and_store(filepath):
    ensure_dirs()
    filename = os.path.basename(filepath)

    with open(filepath, "rb") as f:
        data = f.read()

    encrypted_data = encrypt_file(data)
    sha_hash = get_sha256(data)

    enc_path = os.path.join(ENC_DIR, filename + ".enc")
    with open(enc_path, "wb") as f:
        f.write(encrypted_data)

    meta = load_metadata()
    meta[filename] = {
        "encrypted_file": enc_path,
        "timestamp": time.ctime(),
        "sha256": sha_hash
    }
    save_metadata(meta)
    print(f"[+] Encrypted and stored {filename}")

def decrypt_and_verify(filename):
    ensure_dirs()
    meta = load_metadata()
    if filename not in meta:
        print("[-] File not found in metadata.")
        return

    enc_path = meta[filename]["encrypted_file"]
    with open(enc_path, "rb") as f:
        enc_data = f.read()

    decrypted_data = decrypt_file(enc_data)
    calculated_hash = get_sha256(decrypted_data)

    if calculated_hash != meta[filename]["sha256"]:
        print("[-] WARNING: Hash mismatch. File may be tampered!")
        return

    out_path = os.path.join(DEC_DIR, filename)
    with open(out_path, "wb") as f:
        f.write(decrypted_data)

    print(f"[+] Decrypted successfully and stored at {out_path}")
