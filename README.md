# 🔐 AES-256 Secure File Storage System (PyQt5 GUI) 

## Table of Contents
- [Project Overview](#project-overview)
- [Purpose and Use Case](#purpose-and-use-case)
- [Features](#features)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [GUI Workflow](#gui-workflow)
- [Technical Background and Theory](#technical-background-and-theory)
- [File Integrity Verification](#file-integrity-verification)
- [Project Structure](#project-structure)
- [Limitations and Future Improvements](#limitations-and-future-improvements)
- [Author](#author)
- [License](#license)
- [Notes](#notes)

---

## Project Overview

This project implements a **local secure file storage system** with encryption and decryption functionalities using the **AES-256 symmetric encryption algorithm**. It features a user-friendly **Graphical User Interface (GUI)** built with **PyQt5** to simplify file security management without needing command-line interaction.

---

## Purpose and Use Case

With increasing concerns about data privacy and security, protecting sensitive files on local machines is essential. This project provides:

- **Confidentiality:** Encrypt sensitive files to prevent unauthorized access.
- **Integrity:** Verify that files have not been tampered with after encryption.
- **Usability:** A simple GUI for users who do not have technical expertise.
- **Portability:** Designed to run cross-platform on Kali Linux, Windows, and other environments supporting Python and PyQt5.

Typical use cases include storing personal documents, confidential reports, research data, and any files requiring encryption before sharing or backup.

---

## Features

| Feature                      | Description                                    |
|-----------------------------|------------------------------------------------|
| AES-256 Encryption           | Industry-standard 256-bit symmetric encryption.|
| CBC Mode                    | Cipher Block Chaining mode ensures strong diffusion.|
| PKCS7 Padding                | Handles plaintext sizes not aligned to AES block size.|
| GUI Interface                | PyQt5-based intuitive interface for file operations.|
| File Selection Dialogs       | Native dialogs to pick input/output files.    |
| Automatic Metadata Storage   | Stores filename, key, timestamp, and hash securely.|
| SHA-256 Integrity Check      | Verifies decrypted file integrity post-decryption.|
| Error Handling               | User-friendly error messages and validations. |
| Local Only                   | No cloud storage or external transmission — offline operation.|

---

##  Installation

### 🔗 Requirements
- Python 3.8+
- PyQt5
- cryptography

### 📥 Install Packages

```bash
pip install pyqt5 cryptography
```

## 🛠️ Installation

> **On Kali Linux**, if `pip install pyqt5` has issues, use the following:

```bash
sudo apt update
sudo apt install python3-pyqt5 -y
pip install cryptography
```

#  How to Run
Open your terminal or command prompt.
Navigate to the project directory.
Run the main application:
```
python3 main.py
```
The GUI window will open, ready to encrypt or decrypt files.

# GUI Workflow

## Encrypt a File

Click "Encrypt File".

# Select any file from your system.

The app:

Encrypts the file using AES-256.

Saves the encrypted version as .enc in the storage/ folder.

Generates and shows the AES key (copy & save it!).

Stores metadata in the metadata/ folder.

# 🔓 Decrypt a File

Click "Decrypt File".

Select a previously encrypted .enc file.

Enter the AES key used during encryption.

Choose where to save the decrypted output.

The app:

Decrypts the file using the AES key.

Checks SHA-256 hash for integrity.

Shows whether the file was tampered or safe.


## Technical Background and Theory
AES (Advanced Encryption Standard) is a symmetric key encryption algorithm.

This project uses:

🔐 AES-256 → 256-bit key for strong encryption.

🔄 CBC Mode → Cipher Block Chaining for better diffusion.

📦 PKCS7 Padding → Ensures data aligns to AES block size.

📌 A random AES key and IV (Initialization Vector) are generated for each encryption.

The IV is stored with the ciphertext.

The AES key is not stored — it is shown once and must be saved by the user securely.


# File Integrity Verification
During encryption, the tool calculates the SHA-256 hash of the original file.

During decryption, it calculates the SHA-256 hash again on the decrypted file.

If both hashes match → ✅ File is authentic and untampered.

If hashes do not match → ❌ File was corrupted or modified.

# Project Structure
```
pgsql
Copy code
SecureFileStorage_GUI/
├── main.py              # Launches GUI
├── ui_main.py           # GUI layout and logic
├── crypto_utils.py      # AES encryption/decryption
├── file_manager.py      # Metadata, hashing, and integrity checks
├── storage/             # Encrypted files go here (AUTO CREATION)
├── metadata/            # Stores JSON metadata files (AUTO CREATION)
└── README.md            # Project documentation
```

#  Limitations and Future Improvements

🔑 Key Management: Currently, the AES key is shown only once.

✅ Future: Use password-based key derivation (PBKDF2).

🔐 Authentication: CBC doesn't provide authentication.

✅ Future: Upgrade to AES-GCM for built-in integrity checking.

📁 File Size: Entire file is loaded into memory.

✅ Future: Support for large files with streaming encryption.

🧑‍💻 User Interface: Basic design.

✅ Future: Add batch mode, key manager, progress bars.

📦 Cross-platform Packaging:

✅ Future: Build .exe (Windows), .deb (Linux), .AppImage (portable).

#  Author
Name: Mohankumar 

#  License
This project is provided for educational and personal use only.
No warranty is provided. Attribution is appreciated.

#  Notes

🔐 Store your AES key safely — it is never saved by the program. Without it, decryption is impossible.

🌐 This is an offline-only tool — no internet connection or cloud storage is used.

✅ Always verify the decrypted file's integrity to ensure it was not modified.
