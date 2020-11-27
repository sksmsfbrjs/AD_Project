from PyQt5.QtCore import *

from rank import RankInput


class Timer:

    def __init__(self, lcd, message, score, send_button, inputLine):
        # 변수 설정
        self.gameTime = 10
        self.lcdDisplay = lcd
        self.endMessage = message
        self.finalScore = score
        self.sendButton = send_button
        self.inputLine = inputLine

        # QTimer() 호출
        self.gameTimer = QTimer()
        # startTimer() 호출
        self.startTimer()

    def game_function(self):
        # 시간 출력
        self.lcdDisplay.display(self.gameTime)
        # 1초 감소
        self.gameTime -= 1
        # 제한 시간에 도달했을 때 타이머 정지 후 점수 출력
        if self.gameTime == -1:
            self.gameTimer.stop()
            self.endMessage.setText("Score : " + self.finalScore.text())
        # 게임이 끝났을 때 버튼을 비활성화 & subWindow 실행
        if self.gameFinished():
            self.sendButton.setDisabled(True)
            self.inputLine.setReadOnly(True)
            RankInput(self.finalScore).showModal()

    # 타이머 시작
    def startTimer(self):
        self.gameTimer.start()
        self.gameTimer.setInterval(1000)
        self.gameTimer.timeout.connect(self.game_function)

    def gameFinished(self):
        if self.gameTimer.isActive():
            return False
        else:
            return True
