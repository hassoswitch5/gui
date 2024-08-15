import PyQt5.QtWidgets as qtw
from hussein import Ui_MainWindow

class main_window(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.send_button.clicked.connect(self.add_message)
    def add_message(self):
        name = self.message_input.text()
        msg = self.msg_textbox.text()
        whole_text = name + ";" +msg
        message = qtw.QLabel()
        message.setText(whole_text)        
        self.verticalLayout.addWidget(message)

app = qtw.QApplication
application_window = main_window()
application_window.show

app.exec_()