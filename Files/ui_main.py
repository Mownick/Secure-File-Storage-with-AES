from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QLabel, QTextEdit, QInputDialog, QMessageBox
)
from crypto_utils import generate_key_iv, encrypt_file, decrypt_file
from file_manager import get_sha256, save_metadata, verify_integrity
import os

class SecureFileStorageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure File Storage - AES256")
        self.setGeometry(200, 200, 500, 300)
        layout = QVBoxLayout()

        label = QLabel("🔐 AES-256 Secure File Storage System")
        layout.addWidget(label)

        encrypt_btn = QPushButton("Encrypt File")
        encrypt_btn.clicked.connect(self.encrypt_file_gui)
        layout.addWidget(encrypt_btn)

        decrypt_btn = QPushButton("Decrypt File")
        decrypt_btn.clicked.connect(self.decrypt_file_gui)
        layout.addWidget(decrypt_btn)

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(self.output_box)

        self.setLayout(layout)

    def encrypt_file_gui(self):
        path, _ = QFileDialog.getOpenFileName(self, "Choose file to encrypt")
        if not path:
            return

        key, iv = generate_key_iv()
        os.makedirs("storage", exist_ok=True)
        enc_path = os.path.join("storage", os.path.basename(path) + ".enc")
        encrypt_file(path, enc_path, key, iv)
        sha256 = get_sha256(path)
        save_metadata(path, enc_path, key.hex(), sha256)

        self.output_box.setText(
            f"[+] File Encrypted Successfully!\n"
            f"Saved to: {enc_path}\n\n"
            f"[KEY] Save this AES key for decryption:\n{key.hex()}"
        )

    def decrypt_file_gui(self):
        path, _ = QFileDialog.getOpenFileName(self, "Choose encrypted file")
        if not path:
            return

        key_hex, ok = QInputDialog.getText(self, "Enter AES Key", "AES Key (hex):")
        if not ok or not key_hex:
            return

        try:
            key = bytes.fromhex(key_hex)
        except ValueError:
            QMessageBox.critical(self, "Invalid Key", "AES key must be in hex format.")
            return

        out_path, _ = QFileDialog.getSaveFileName(self, "Save decrypted file as")
        if not out_path:
            return

        try:
            decrypt_file(path, out_path, key)
            meta_path = f"metadata/{os.path.basename(path)}.json"

            if verify_integrity(out_path, meta_path):
                self.output_box.setText("✓ Decryption successful. File verified.")
            else:
                self.output_box.setText("⚠ Decryption done, but integrity check failed!")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Decryption failed:\n{str(e)}")

