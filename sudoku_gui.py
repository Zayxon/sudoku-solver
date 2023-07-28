from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sudoku_solver import Sudoku

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,500)
        self.setWindowTitle("Sudoku solver")
        self.f_num = QFont('Verdana')
        self.f_butt = QFont('Verdana')
        self.f_num.setPointSize(25)
        self.f_butt.setPointSize(10)
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.list_of_fields = []

        # Creating sudoku fields for entering a number
        for i in range(81):
            x = QLineEdit()
            x.setValidator(QIntValidator(1, 9))
            x.setAlignment(Qt.AlignCenter)
            x.setFont(self.f_num)
            self.list_of_fields.append(x)

        # Creating layout
        layout = QGridLayout()

        # Adding sudoku fields to our layout
        iteration = -1
        for field in self.list_of_fields:
            iteration += 1
            row = iteration // 9
            col = iteration % 9
            layout.addWidget(field, row, col, 1, 1)

        # Creating buttons
        self.button_solve = QPushButton("Solve!")
        self.button_solve.setFont(self.f_butt)
        self.button_new_input = QPushButton("Enter new sudoku")
        self.button_new_input.setFont(self.f_butt)

        # Connecting buttons to specific functions
        self.button_solve.clicked.connect(self.solve)
        self.button_new_input.clicked.connect(self.null_board)
        
        # Adding buttons to our layout
        layout.addWidget(self.button_solve, 9, 0, 1, 4)
        layout.addWidget(self.button_new_input, 9, 5, 1, 4)

        # Add our layout to our window
        self.setLayout(layout)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        # setting the color, width, type of line
        pen = QPen(QColor(0,116,232), 2, Qt.SolidLine)
        qp.setPen(pen)

        # coordinates from which point to which point we want to draw the line
        # from X, from Y, to X, to Y
        qp.drawLine(12, 160, 488, 160)
        qp.drawLine(12, 311, 488, 311)
        qp.drawLine(170, 12, 170, 458)
        qp.drawLine(331, 12, 331, 458)
        qp.end()

    def solve(self):
        # Saving user input into our prepared empty sudoku board
        iteration = -1
        for field in self.list_of_fields:
            iteration += 1
            row = iteration // 9
            col = iteration % 9
            if field.text() != '':
                self.board[row][col] = int(field.text())
            else:
                self.board[row][col] = 0

        # Calling our solve method to get solution
        s = Sudoku(self.board)
        s.solve()

        # "Printing" the solution into our app
        iteration = -1
        for field in self.list_of_fields:
            iteration += 1
            row = iteration // 9
            col = iteration % 9
            field.setText(str(self.board[row][col]))
    
    def null_board(self):
        iteration = -1
        for field in self.list_of_fields:
            iteration += 1
            row = iteration // 9
            col = iteration % 9
            field.setText('')
            self.board[row][col] = 0

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()