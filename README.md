# Password Generator
## Generate your Password by setting the conditions of password's length and strength

Code is written in Python using PyCharm, and Qt-Designer for the front-end. The generator makes use of several important modules, "secrets" for generating secure random numbers, "pyperclip" which gives the ability of copying and pasting text to the clipboard and finally "PyQt5" for using PyQt5 Widgets.

A you can see in the picture below, there are three condistions to generate a password, including: Username, Password Length and Strength. The Strength itself has three levels that based on each option, a different password is generated. This operation is handled by the "secrets" module which provides access to the most secure source of randomness that your operating system provides. The considered alphabets related to these three options are...
Weak: Digits, Lowercase Letters
Medium: Digits, Lowercase & Uppercase Letters
Strong: Digits, Lowercase & Uppercase Letters, Punctuations

![password_generator](https://github.com/ParnianSrb/Password-Generator/assets/82469872/593c676e-00ea-4113-8944-8dbf2f1c6011)

This project does not use a Database, however the complete version must do and get use of all these three conditions, mostly Username which would be the Primarykey rather than a useless input.
Please make contribution to build up the database and complete my project on your own special way!

Installation Instructions:
1. To use python I have tried coding with PyCharm which has been easy and straightforward. Here is the link to download and install: https://www.jetbrains.com/pycharm/download/?section=windows / https://www.jetbrains.com/help/pycharm/installation-guide.html#snap
2. To use all the modules please import them as I did in the code.
