import string
import secrets
import pyperclip
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QLineEdit, QPushButton, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The Ui File
        uic.loadUi('P1-Password_Generator.ui', self)

        # Define Widgets
        self.user_label = self.findChild(QLabel, 'user_label')
        self.passLength_label = self.findChild(QLabel, 'passLength_label')
        self.strength_label = self.findChild(QLabel, 'strength_label')

        self.user_lineEdit = self.findChild(QLineEdit, 'user_lineEdit')
        self.passLength_lineEdit = self.findChild(QLineEdit, 'passLength_lineEdit')
        self.passGenerate_lineEdit = self.findChild(QLineEdit, 'passGenerate_lineEdit')

        self.passGenerator_button = self.findChild(QPushButton, 'passGenerator_button')
        self.reset_button = self.findChild(QPushButton, 'reset_button')
        self.copy_button = self.findChild(QPushButton, 'copy_button')

        self.weak_radio = self.findChild(QRadioButton, 'weak_radio')
        self.medium_radio = self.findChild(QRadioButton, 'medium_radio')
        self.strong_radio = self.findChild(QRadioButton, 'strong_radio')

        # Click Buttons
        self.passGenerator_button.clicked.connect(self.generator)
        self.reset_button.clicked.connect(self.reset)
        self.copy_button.clicked.connect(self.copy)

        # Set Strong Radio Button To Checked
        self.strong_radio.setChecked(True)

        # Show The App
        self.show()

    def generate_password(self, alphabet):
        i = 0
        self.password = ''
        self.passLength = int(self.passLength_lineEdit.text())
        for i in range(self.passLength):
            self.password += ''.join(secrets.choice(alphabet))
        self.passGenerate_lineEdit.setText(self.password)

    def generator(self):
        if self.weak_radio.isChecked():
            self.alphabet = string.digits + string.ascii_lowercase
            self.generate_password(self.alphabet)

            self.medium_radio.setCheckable(False)
            self.strong_radio.setCheckable(False)

        elif self.medium_radio.isChecked():
            self.alphabet = string.digits + string.ascii_letters
            self.generate_password(self.alphabet)

            self.weak_radio.setCheckable(False)
            self.strong_radio.setCheckable(False)

        elif self.strong_radio.isChecked():
            self.alphabet = string.digits + string.ascii_letters + string.punctuation
            self.generate_password(self.alphabet)

            self.weak_radio.setCheckable(False)
            self.medium_radio.setCheckable(False)

        # Disable the QLineEdits after pressing the Generate button
        self.user_lineEdit.setEnabled(False)
        self.passLength_lineEdit.setEnabled(False)
        self.passGenerate_lineEdit.setEnabled(False)

    def reset(self):

        # Enable the QLineEdits
        self.user_lineEdit.setEnabled(True)
        self.passLength_lineEdit.setEnabled(True)
        self.passGenerate_lineEdit.setEnabled(True)

        self.user_lineEdit.clear()
        self.passGenerate_lineEdit.clear()
        self.passLength_lineEdit.clear()

        self.weak_radio.setCheckable(True)
        self.strong_radio.setCheckable(True)
        self.strong_radio.setCheckable(True)

        # Set Strong Radio Button Back To Checked
        self.strong_radio.setChecked(True)

    def copy(self):
        self.copy = self.passGenerate_lineEdit.text()
        pyperclip.copy(self.copy)


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
