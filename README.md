# AD_PROJECT
------------

## 프로젝트 설명
> PyQt5를 이용하여 영어 끝말잇기를 구현했습니다.
------------

### game 모듈 설명
------------
1. __init__(self)
    * UI 구현
    * Word 클래스 호출

2. startGame(self)
    * Timer 클래스 호출 (매개변수로 time, score, 출력메세지, InputLine, sendButton 설정)
    * Score 클래스 호출 (startGame이 실행될 때마다 점수를 초기화주기 위해)
    * UI 초기화 (제한시간 = 10, 점수 = 0, sendButton 활성화, InputLine 활성화, message에 새로운 단어 출력)

3. sendClicked(self)
    * 입력된 단어의 유효성 검사
     * 사용자의 입력의 마지막 글자로 시작하는 다음 단어 출력
     * 점수 추가 & 점수 출력
     * 정답 입력 시 시간 10초로 초기화
   
### timer 모듈 설명
------------
1. __init__(self)
    * 변수 설정(gameTime)
    * game으로부터 받은 변수 재설정
    * QTimer() 선언, startTimer() 호출
  
2. startTimer(self)
    * 타이머를 시작시킴
    * 1초 간격으로 game_function()이 호출되게 connect

3. game_function(self)
    * 시간 출력 & 1초 감소 기능
    * 제한 시간에 도달했을 때 타이머 정지 후 점수 출력
    * 게임이 끝났을 때 버튼을 비활성화 & subWindow 실행
    
4. gameFinished(self)
    * 타이머가 비활성화일때 True 리턴, 아니라면 False 리턴
  
### word 모듈 설명
------------
1. __init__(self)
    * 영어 단어 모음(words.txt) 호출하여 self.words에 리스트의 형태로 저장
    * 사용한 단어 리스트(usedWords) 선언

2. startRandFromDB(self)
    * game 모듈에서 startGame 메소드에 쓰일 단어 리턴

3. relayRandomFromDB(self, startWord)
    * 사용자가 입력한 단어의 다음 단어를 리턴하는 메소드
    
4. testWord(self, answer)
    * 이미 사용한 단어이거나, 입력된 문자열이 단어가 아닌 구(2어절 이상)이거나 이 단어가 영어사전에 등재되지 않은 경우 (ex : eee, lololol ...etc) 또는 단어의 길이가 2보다 작은 경우(ex : a, '') 틀린 답으로 간주
    * 위 조건을 모두 만족할 경우 usedWords에 추가하고 True 리턴, 위 조건중 하나라도 만족하지 못하면 False 리턴
    
### score 모듈 설명
------------
1. __init__(self)
    * self.score 필드 설정
    
2. increaseScore(self, answer)
    * 단어의 길이가 길수록 큰 점수 부여
    
### rank 모듈 설명
------------
1. __init__(self, score)
    * UI 구현 (게임 이용자의 이름을 입력하는 창)
    * 입력받은 score를 self.finalScore에 할당

2. enterClicked(self)
    * 엔터가 클릭 되었을 때 rankList 호출
    * rankList 호출 시 매개변수에 rankDB.txt, 입력받은 이름과 finalScore값의 사전을 대입

3. showModal(self)
    * 이 클래스가 서브 윈도우로써 호출되게 하게끔 하는 메소드

### rankList 모듈 설명
------------
1. readRankDB(filename)
    * static 메소드로써 rankDB를 읽어들임

2. writeRankDB(filename, rank)
    * static 메소드로써 rankDB 갱신

3. __init__(self, filename, rank)
    * UI 구현 (이 게임 이용자들의 순위를 나타내는 윈도우)
    * self.rankList 선언 (self.rankList = readRankDB(filename))
    * rank 모듈에서 실행된 enterClicked에서 받았던 정보들을 rankList에 추가 (self.rankList += rank 호출)
    * rankDB 갱신 (writeRankDB 호출)
    
4. showModal(self)
    * 이 클래스가 서브 윈도우로써 호출되게 하게끔 하는 메소드
    
5. showRankDB(self)
    * self.rankList에서 점수를 내림차순 기준으로 정렬한 rankDB라는 리스트 생성
    * text에 rankDB를 형식에 맞게 대입하여 리턴
