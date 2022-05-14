from PyQt5.QtWidgets import *
from gui1620window import Ui_MainWindow_proj1

class Controller(QMainWindow, Ui_MainWindow_proj1):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton_One.clicked.connect(lambda : self.one())

        self.pushButton_One.clicked.connect(lambda: self.two())

        self.pushButton_One.clicked.connect(lambda: self.three())

    def one(n):
        n = self.textEdit_one_n_input.getInt()
        if type(n) != int:
            raise TypeError('Invalid Input')
        else:
            n = int(n)
        if n <= 0:
            raise ValueError('Invalid Input')
        if n > 1:
            return n + one(n-1)
        if n == 1:
            return 1

    def two(num, pow):
        num = self.textEdit_one_num_input.getInt()
        pow = self.textEdit_one_pow_input.getInt()
        if (type(pow) != int) or (type(num) != (int)):
            raise TypeError('Invalid Input')
        if pow < 0:
            raise ValueError('Invalid Input')
        if pow == 0:
            return 1
        if pow > 0:
            return num * two(num, pow - 1)

    def three(n):
        n = self.textEdit_one_n_input.getInt()
        if type(n) != int:
            raise TypeError('Invalid Input')
        if n <= 0:
            raise ValueError('Invalid Input')
        if n > 0:
            print(n, end=" ")
            n -= 1
            three(n-1)