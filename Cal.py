import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Consider using a QGridLayout instead of manual setGeometry for responsiveness
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 450)
        MainWindow.setStyleSheet("background-color: rgb(248, 244, 236);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Display
        self.txtcalc = QtWidgets.QLineEdit(self.centralwidget)
        self.txtcalc.setGeometry(QtCore.QRect(20, 10, 421, 71))
        self.txtcalc.setReadOnly(True)
        # Use triple-quoted string for multiline stylesheet
        self.txtcalc.setStyleSheet("""
            background-color: rgb(248, 244, 236);
            color: rgb(64, 43, 58);
            font: 10pt "MV Boli";
        """)
        self.txtcalc.setObjectName("txtcalc")
        # Digit buttons
        positions = [(i, j) for i in range(3) for j in range(3)]
        for pos, num in zip(positions, range(1, 10)):
            btn = QtWidgets.QPushButton(self.centralwidget)
            btn.setGeometry(QtCore.QRect(20 + pos[1]*110, 90 + pos[0]*70, 93, 61))
            btn.setStyleSheet("background-color: rgb(255, 155, 210); font: 10pt \"MV Boli\";")
            btn.setObjectName(f"btn_{num}")
            btn.setText(str(num))
            setattr(self, f"btn_{num}", btn)
        # Zero and point
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(20, 300, 93, 61))
        self.btn_0.setText("0")
        self.btn_0.setStyleSheet("background-color: rgb(255, 155, 210); font: 10pt \"MV Boli\";")
        self.btnpoint = QtWidgets.QPushButton(self.centralwidget)
        self.btnpoint.setGeometry(QtCore.QRect(130, 300, 93, 61))
        self.btnpoint.setText(".")
        self.btnpoint.setStyleSheet("background-color: rgb(255, 155, 210); font: 10pt \"MV Boli\";")
        # Operators (rename 'supply' to 'multiply' for clarity)
        ops = {"add": "+", "minus": "-", "multiply": "*", "divide": "/"}  # renamed key
        for idx, (name, symbol) in enumerate(ops.items()):
            btn = QtWidgets.QPushButton(self.centralwidget)
            btn.setGeometry(QtCore.QRect(350, 90 + idx*70, 93, 61))
            btn.setText(symbol)
            btn.setObjectName(f"btn{name}")
            btn.setStyleSheet("background-color: rgb(255, 155, 210); font: 10pt \"MV Boli\";")
            setattr(self, f"btn{name}", btn)
        # Equal, clear, backspace
        self.btnequal = QtWidgets.QPushButton(self.centralwidget)
        self.btnequal.setGeometry(QtCore.QRect(240, 300, 93, 61))
        self.btnequal.setText("=")
        self.btnclear = QtWidgets.QPushButton(self.centralwidget)
        self.btnclear.setGeometry(QtCore.QRect(20, 370, 311, 61))
        self.btnclear.setText("clear")
        self.btnclear.setStyleSheet("background-color: rgb(214, 52, 132); font: 10pt \"MV Boli\";")
        self.btnbackspace = QtWidgets.QPushButton(self.centralwidget)
        self.btnbackspace.setGeometry(QtCore.QRect(350, 370, 93, 61))
        self.btnbackspace.setText("<---")
        self.btnbackspace.setStyleSheet("background-color: rgb(214, 52, 132); font: 10pt \"MV Boli\";")
        MainWindow.setCentralWidget(self.centralwidget)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.current_expr = ""
        # Beware of late binding with lambda in loop: use default argument to capture value
        for num in range(10):
            getattr(self, f"btn_{num}").clicked.connect(lambda _, v=str(num): self.input_value(v))
        self.btnpoint.clicked.connect(lambda: self.input_value('.'))
        # Connect operator buttons
        self.btnadd.clicked.connect(lambda: self.input_operator('+'))
        self.btnminus.clicked.connect(lambda: self.input_operator('-'))
        self.btnmultiply.clicked.connect(lambda: self.input_operator('*'))
        self.btndivide.clicked.connect(lambda: self.input_operator('/'))
        # Connect actions
        self.btnequal.clicked.connect(self.calculate)
        self.btnclear.clicked.connect(self.clear)
        self.btnbackspace.clicked.connect(self.backspace)

    def input_value(self, val):
        self.current_expr += val
        self.txtcalc.setText(self.current_expr)

    def input_operator(self, op):
        if self.current_expr and self.current_expr[-1] not in '+-*/':
            self.current_expr += op
            self.txtcalc.setText(self.current_expr)

    def calculate(self):
        try:
            # Avoid eval for safety: consider using a parsing library or implementing a simple parser
            result = str(eval(self.current_expr))
        except Exception:
            result = 'Error'
        self.txtcalc.setText(result)
        self.current_expr = result if result != 'Error' else ''

    def clear(self):
        self.current_expr = ''
        self.txtcalc.clear()

    def backspace(self):
        self.current_expr = self.current_expr[:-1]
        self.txtcalc.setText(self.current_expr)

if __name__ == "__main__":
    # Consider moving app initialization into a separate function for testability
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
