from PyQt5.QtWidgets import *


def readRankDB(filename):
    fH = open(filename)

    rank = eval(fH.read())
    fH.close()
    return rank


def writeRankDB(filename, rank):
    fH = open(filename, 'w')
    fH.write(str(rank) + '\n')
    fH.close()


class SubWindow(QDialog):
    def __init__(self, filename, rank):
        super().__init__()

        # self.rankList에 rankDB.txt 내용을 대입
        self.rankList = readRankDB(filename)
        # 입력 받은 정보를 추가하고 rankDB를 갱신
        self.rankList += rank
        writeRankDB(filename, self.rankList)

        # UI 구현
        mainLayout = QVBoxLayout()

        lbl = QTextEdit()
        lbl.setText(self.showRankDB())
        mainLayout.addWidget(lbl)

        self.setLayout(mainLayout)

        self.setWindowTitle('Rank')
        self.setGeometry(100, 100, 400, 500)
        self.move(1100, 300)

    def showModal(self):
        super().exec_()

    # String 타입으로 점수를 내림차순 기준으로 정렬한 rankDB 리턴
    def showRankDB(self):
        text = ""
        rankDB = sorted(self.rankList, key=lambda x: int(x["점수"]), reverse=True)

        for num, i in enumerate(rankDB, start=1):
            text += str(num) + "위 : "
            for value in i:
                text += value + " : " + i[value] + " "
            text += "\n"

        return text
