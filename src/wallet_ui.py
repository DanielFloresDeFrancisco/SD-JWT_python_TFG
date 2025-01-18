import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,  QPushButton, QLineEdit)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(650, 250, 400, 400)

        self.label_title = QLabel("MyWallet", self)

        self.label_name = QLabel("Name:", self)
        self.label_surname = QLabel("Surname:", self)
        self.label_street = QLabel("Street:", self)
        self.label_list = [self.label_name, self.label_surname, self.label_street]



        self.text_name = QLineEdit(self)
        self.text_surname = QLineEdit(self)
        self.text_street = QLineEdit(self)
        self.text_list = [self.text_name, self.text_surname, self.text_street]

        self.button = QPushButton("Submit", self)

        self.initUI()

    
    def initUI(self):

        self.label_title.setGeometry(120, 25, 200, 50)
        self.label_title.setStyleSheet("font-size: 40px;")

        self.label_name.setGeometry(20, 100, 170, 40)
        self.label_surname.setGeometry(20, 150, 170, 40)
        self.label_street.setGeometry(20, 200, 170, 40)

        self.text_name.setGeometry(170, 100, 200, 40)
        self.text_surname.setGeometry(170, 150, 200, 40)
        self.text_street.setGeometry(170, 200, 200, 40)

        self.button.setGeometry(170, 280, 100, 40)
        
        self.setStyleSheet("""
        QLabel {
            font-size: 20px;
            font-family: Arial;
            font-weight: bold;
        }
        QLineEdit {
            font-size: 20px;
            font-family: Arial;
            border: 2px solid black;
            border-radius: 15px;
            padding: 5px;
        }
        QPushButton {
            font-size: 20px;
            font-family: Arial;
            border: 2px solid black;
            border-radius: 15px;
        }
         """)
        
        self.button.clicked.connect(self.handling_data)


    def handling_data(self):
        f = open("data/text/preuba.txt", "w")
        for label_widget, text_widget in zip(self.label_list, self.text_list):
            label = label_widget.text()
            text = text_widget.text()
            f.write(f"{label} {text}\n")
        f.close()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() #When creating a window, is hide by default
    sys.exit(app.exec_())



if __name__== "__main__":
    main()