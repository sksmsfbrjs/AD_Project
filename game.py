from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit, QToolButton, QLCDNumber

from word import Word
from score import Score
from timer import Timer


class EnglishWordRelay(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.word = Word('words.txt')

        mainLayout = QGridLayout()

        # timer 관련 위젯 생성
        lcdlbl = QLabel("Timer")
        lcdlbl.setAlignment(Qt.AlignRight)

        mainLayout.addWidget(lcdlbl, 0, 0)
        self.timeLcd = QLCDNumber()
        mainLayout.addWidget(self.timeLcd, 0, 1)
        self.timeLcd.setNumDigits(2)
        self.timeLcd.display('10')

        # score 관련 위젯 생성
        scorelbl = QLabel("Score")
        mainLayout.addWidget(scorelbl, 0, 2)
        scorelbl.setAlignment(Qt.AlignRight)

        self.scoreLcd = QLineEdit()
        self.scoreLcd.setReadOnly(True)
        self.scoreLcd.setAlignment(Qt.AlignRight)
        font = self.scoreLcd.font()
        font.setPointSize(font.pointSize() + 15)
        self.scoreLcd.setFont(font)
        self.scoreLcd.setFixedWidth(100)
        mainLayout.addWidget(self.scoreLcd, 0, 3)

        # 단어 message 위젯 설정
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignCenter)
        font = self.message.font()
        font.setPointSize(font.pointSize() + 8)
        self.message.setFont(font)
        self.message.setMaxLength(52)
        mainLayout.addWidget(self.message, 1, 0, 1, 4)

        # Input 위젯 설정
        self.Input = QLineEdit()
        font = self.Input.font()
        font.setPointSize(font.pointSize() + 8)
        self.Input.setFont(font)
        self.Input.setMaxLength(20)
        # 게임에서 send 버튼의 클릭 기능을 엔터키로도 할 수 있게 기능 추가
        self.Input.returnPressed.connect(self.sendClicked)
        mainLayout.addWidget(self.Input, 2, 0, 1, 3)

        # sendButton 위젯 설정
        self.sendButton = QToolButton()
        self.sendButton.setText('Send')
        self.sendButton.clicked.connect(self.sendClicked)

        mainLayout.addWidget(self.sendButton, 2, 3)

        # newGameButton 위젯 설
        newGameButton = QToolButton()
        newGameButton.setText('New Game')
        newGameButton.clicked.connect(self.startGame)
        mainLayout.addWidget(newGameButton, 3, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle('English Word Relay Game')
        self.setFixedSize(400, 300)
        self.move(750, 300)

        # 게임 시작
        self.startGame()

    def startGame(self):

        # 게임을 시작할 때마다 Timer, Score 클래스를 호출하여 제한 시간 10초, 점수 0점으로 초기화
        self.timer = Timer(self.timeLcd, self.message, self.scoreLcd, self.sendButton, self.Input)
        self.scoreValue = Score()

        self.message.clear()
        self.Input.clear()
        self.message.setText(self.word.startRandFromDB())
        self.scoreLcd.setText(str(self.scoreValue.score))

        self.sendButton.setDisabled(False)
        self.Input.setReadOnly(False)

    def sendClicked(self):
        answer = self.Input.text()
        self.Input.clear()

        # 입력된 단어의 유효성 검사
        if self.word.testWord(answer):
            # 사용자의 입력의 마지막 글자로 시작하는 다음 단어 출력
            firstChar = answer.strip()[-1]
            self.message.setText(self.word.relayRandomFromDB(firstChar))
            # 점수 추가 & 점수 출력
            self.scoreValue.increaseScore(answer)
            self.scoreLcd.setText(str(self.scoreValue.score))
            # 시간 초기화
            if self.timer.gameTime > 0:
                self.timer.gameTime = 10


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    game = EnglishWordRelay()
    game.show()
    sys.exit(app.exec_())
