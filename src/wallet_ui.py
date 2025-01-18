import sys
from utils import parse_data_to_SDJWT
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,  QPushButton, QLineEdit, QWidget, QPlainTextEdit)

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
        
        self.button.setCheckable(True)
        self.button.clicked.connect(self.handling_data)


    def handling_data(self):
        f = open("data/text/dynamic_claims.txt", "w")
        for label_widget, text_widget in zip(self.label_list, self.text_list):
            label = label_widget.text()
            text = text_widget.text()
            f.write(f"{label} {text}\n")
        f.close()

        sd_jwt, secret_key = parse_data_to_SDJWT("data/text/dynamic_claims.txt")
        print(sd_jwt)

        self.token_info_UI = Token_Info_UI(sd_jwt, secret_key) 
        self.token_info_UI.show()

        self.hide()



class Token_Info_UI(QWidget):

    def __init__(self, sd_jwt, secret_key):
        super().__init__()

        self.sd_jwt = sd_jwt
        self.secret_key = secret_key

        self.setGeometry(650, 250, 600, 600)

        self.label_sign_alg = QLabel("Algorithm", self)
        self.text_sign_alg = QLineEdit(self)
        self.label_secret = QLabel("Secret", self)
        self.text_secret = QPlainTextEdit(self)
        self.label_token_title = QLabel("SD-JWT", self)
        self.text_token = QPlainTextEdit(self)

        # self.button = QPushButton("Submit", self)

        self.initUI()

    
    def initUI(self):

        self.label_sign_alg.setGeometry(20, 50, 170, 40)
        self.text_sign_alg.setGeometry(140, 50, 170, 40)  
        self.text_sign_alg.setText("SHA256")    
        self.text_sign_alg.setReadOnly(True)


        self.label_secret.setGeometry(20, 110, 170, 40)
        self.text_secret.setGeometry(100, 100, 400, 60)
        self.text_secret.setPlainText(self.secret_key)
        self.text_secret.setReadOnly(True)
        self.text_secret.setStyleSheet("font-size: 20px;"
                                      "font-family: Arial;"
                                      "border: 2px solid black;"
                                      "border-radius: 5px;")


        self.label_token_title.setGeometry(20, 160, 170, 40)
        self.text_token.setGeometry(20,200,550,300)
        self.text_token.setPlainText(self.sd_jwt)
        self.text_token.setReadOnly(True)
        self.text_token.setStyleSheet("font-size: 25px;"
                                      "font-family: Arial;"
                                      "border: 5px solid black;"
                                      "border-radius: 8px;")

        
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
         """)
        
        #self.button.setCheckable(True)
        #self.button.clicked.connect(self.handling_data)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__== "__main__":
    main()