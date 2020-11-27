import random


class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            word = line.rstrip()
            self.words.append(word)
        self.len_words = len(self.words)

        self.usedWords = []

    # EnglishWordRelay.startGame()에서 쓰일 첫 단어를 리턴하는 메소드
    def startRandFromDB(self):
        return self.words[random.randrange(self.len_words)]

    # 사용자가 입력한 단어의 다음 단어를 리턴하는 메소드
    def relayRandomFromDB(self, startWord):
        relayList = []
        for i in self.words:
            if i[0] == startWord:
                relayList.append(i)
        return relayList[random.randrange(len(relayList))]

    # 이미 사용한 단어이거나, 입력된 문자열이 단어가 아닌 구(2어절 이상)이거나
    # 이 단어가 영어사전에 등재되지 않은 경우(ex : eee, lololol ...etc)
    # 또는 단어의 길이가 2보다 작은 경우(ex : a, '')
    # 틀린 답으로 간주!
    def testWord(self, answer):
        result = True
        if len(answer.split()) != 1:
            result = False
        elif answer not in self.words:
            result = False
        elif len(answer) <= 1:
            result = False
        elif answer in self.usedWords:
            result = False

        if result:
            # 사용한 단어를 데이터에 저장
            self.usedWords.append(answer)
        return result
