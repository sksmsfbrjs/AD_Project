from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from rankList import SubWindow


class RankInput(QDialog):

    def __init__(self, score):
        super().__init__()

        self.finalScore = score

        # UI 구현
        self.setWindowTitle('Rank')
        self.move(850, 400)
        mainLayout = QGridLayout()

        self.nameLbl = QLabel("Input Name")
        mainLayout.addWidget(self.nameLbl, 0, 0)
        self.nameLbl.setAlignment(Qt.AlignHCenter)

        self.nameInput = QLineEdit()
        self.nameInput.setMaxLength(15)
        self.nameInput.returnPressed.connect(self.enterClicked)
        mainLayout.addWidget(self.nameInput, 1, 0)

        self.sendButton = QToolButton()
        self.sendButton.setText('Enter')
        self.sendButton.clicked.connect(self.enterClicked)
        mainLayout.addWidget(self.sendButton, 1, 1)

        self.setLayout(mainLayout)

        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

    def enterClicked(self):
        win = SubWindow('rankDB.txt', [{"이름": self.nameInput.text(), "점수": self.finalScore.text()}])
        win.showModal()
        self.close()

    def showModal(self):
        super().exec_()
