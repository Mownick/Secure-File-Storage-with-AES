from PyQt5.QtWidgets import QApplication
from ui_main import SecureFileStorageApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SecureFileStorageApp()
    window.show()
    sys.exit(app.exec_())
