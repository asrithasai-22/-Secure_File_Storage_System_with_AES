### 📄 `README.md`

```markdown
# 🔐 Secure File Storage System with AES-256

This project is a **Secure File Storage System** built in **Python** using **AES-256 encryption (CBC mode)**. It allows users to encrypt files, store them securely, and later decrypt them with integrity verification using SHA-256.

---

## ✅ Features

- AES-256 encryption with CBC mode
- Auto-generated AES key (saved securely)
- SHA-256 hash verification to detect tampering
- File encryption with `.enc` extension
- Decryption restores original file in a separate folder
- Metadata storage (`metadata.json`) for tracking
- Command-Line Interface (CLI) support
- Easy to extend into a GUI using PyQt5

---

## 🛠️ Tools & Technologies

- **Python 3.6+**
- [cryptography](https://cryptography.io/en/latest/) library
- JSON for metadata
- CLI interface (GUI optional via PyQt5)

---

## 📁 Project Structure

```

secure\_file\_storage/
│
├── main.py                 # CLI application
├── crypto\_utils.py         # AES encryption/decryption + hashing
├── file\_manager.py         # File I/O and metadata handling
├── requirements.txt        # Required packages
├── metadata.json           # Metadata (auto-created)
├── encrypted\_files/        # Stores .enc encrypted files
└── decrypted\_files/        # Output for decrypted files

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/secure_file_storage.git
cd secure_file_storage
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python main.py
```

---

## 🔐 How to Use

### 🔒 Encrypt a File

1. Choose Option `1`
2. Enter path to any file (e.g., `C:\Users\Asi\Documents\file.txt`)
3. File is encrypted to `encrypted_files/` and added to `metadata.json`

### 🔓 Decrypt a File

1. Choose Option `2`
2. Enter the **original filename** (e.g., `file.txt`)
3. Decrypted file appears in `decrypted_files/`
4. If tampered, it will alert you via SHA256 mismatch

---

## 📌 Example

```
Secure File Storage System
1. Encrypt File
2. Decrypt File
3. Exit
Enter your choice: 1
Enter path to the file: test.docx
[+] Encrypted and stored test.docx

Enter your choice: 2
Enter filename to decrypt: test.docx
[+] Decrypted successfully and stored at decrypted_files/test.docx
```

---

## 🛡️ Security Notes

* AES-256 key is generated and stored in `aes.key`
* SHA-256 ensures the file wasn’t altered during storage
* Avoid sharing `aes.key` publicly or on GitHub

---

## 📌 Future Improvements

* ✅ PyQt5 GUI with file browser
* ✅ File upload drag-drop
* ✅ Password-protected key storage
* ✅ Cloud integration for secure sync

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 💬 Developed By

**Asritha Sai**
