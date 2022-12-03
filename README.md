# 📡 프로젝트 설명

> 재택알바를 알아보기 위해 [알바몬](https://www.albamon.com/?utm_source=google&utm_medium=cpc&utm_campaign=000.%EB%B8%8C%EB%9E%9C%EB%93%9C&utm_content=000.%EB%B8%8C%EB%9E%9C%EB%93%9C&utm_term=%EC%95%8C%EB%B0%94%EB%AA%AC&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkpwFlhluFN7r9F_MsO7EZsBTVODoMmc6JOLe0YGR2q8Zf53fmxsmNEaAhBUEALw_wcB)에서 찾는 도중에 불필요한 정보(광고 및 블로그,인스타 댓글알바류)가 너무 많았다. 이것이 불편하여 필요한 정보만 꺼내볼려고 한다.

### 📟 프로젝트 계획

1. 알바몬 홈페이지에서 "재택알바" 페이지로 이동하여 크롤링을 한다
2. 크롤링한 데이터를 csv로 만들어서 저장한다
3. csv파일을 이용하여 불필요한 알바를 제거하고 웹으로 출력한다

![image](https://user-images.githubusercontent.com/55564114/205448584-79faf584-9600-44df-9aaf-6064d62a259d.png)  

---

# 📃 🖋 기록

|분류|내용|날짜|
|:---:|:---|:---:|
|진행중|프로젝트 시작!! |22.11.29(화)|
|진행중|크롤링 파일(main.py) 작성완료|22.11.29(화)|
|문제|크롤링 과정에서 가끔 차단당함,  time.sleep으로 1차적으로 막았지만, 그래도 발생함.  (완벽히 해결 못함,대신에 에러발생하면 전에 수집한 크롤링 데이터를 저장하게 만들어놓음) |22.11.29(화)|
|진행중|크롤링한 데이터를 csv로 저장|22.11.29(화)|
|진행중|csv파일로 간단히 EDA진행|22.11.30(수)|
|진행중|전처리(processing.py)작성완료|22.11.30(수)|
|진행중|재밌는 알바 찾음  (제페토 접속 테스트해주는 알바임. 실제로 하는중ㅎ)|22.11.30(수)|
|진행중|EDA과정에서 ipynb파일로만 보니까 답답함, flask를 이용해서 웹으로 보기로 결정|22.12.01(목)|
|진행중|Flask(app.py)작성완료|22.12.01(목)|
|진행중|Flask(index.html)작성완료|22.12.02(금)|

---

# 참고 위키독스

- [파이썬 자동화(위키독스)](https://wikidocs.net/73537)
- [비전공자를 위한 파이썬 자동화(위키독스)](https://wikidocs.net/91474)

# 사용 템플릿
- [부트스트랩](https://bootswatch.com/flatly/)

---

# Flask 

![image](https://user-images.githubusercontent.com/55564114/205446740-48b913f0-56ad-4dc6-b80b-3cb44257bfe5.png)
 
---

# 파일설명
```python
    [main.py] : 크롤링 파일
    [main.ipynb] : EDA 파일
    [processing.py] : 데이터 전처리 파일
    [app.py] : Flask 파일
    [requirement.txt] : conda install 항목
```

---

# 코드 실행 방법 

``` python
[VScode 환경]
    0. 새터미널 열기
    1. conda activate alcr
    # 만약 conda activate 해도 (alcr) 같은 표시가 안나타나면
    # conda init powershell 입력하고 다시 터미널 켜보기 
    2. python main.py             # 크롤링 실행
    3. python processing.py       # 데이터전처리 실행
    4. python app.py              # Flask 실행

[Anaconda Prompt 환경]
    0. 크롬드라이버 및 패키지는 준비되었다는 가정
    1. Anaconda Prompt 실행한다
    2. conda activate alcr        # 가상환경 실행
    3. cd git                     # 디렉토리 이동
    4. cd PJT_selenium_albamon    # 디렉토리 이동
    5. python main.py             # 파일 실행 
    6. conda deactivate           # 가상환경 종료 
```

---

# 1. Chromedriver(크롬드라이버) 준비 

> 크롬 우측 상단 메뉴버튼을 클릭 후 [도움말] - [Chrome 정보]를 가서 "나의 크롬 버전"을 확인한다

![image](https://user-images.githubusercontent.com/55564114/204452238-7b2f6bc2-6927-4673-9db8-59cb090b5ca1.png)  

> "나의 크롬 버전"은 `버전 107.0.5304.108`이다

![image](https://user-images.githubusercontent.com/55564114/204452461-51ef0e32-b89c-4bd0-a78d-65a4f1f23c90.png)  

> [크롬드라이버 다운로드](https://chromedriver.chromium.org/downloads) 로 이동해서 "나의 크롬 버전"과 같은 버전을 다운로드한다(완전히 같은 버전이 없을 경우, 내 버전보다 낮은 버전을 고르면 된다. 나같은 경우, 내 버전이 `107.0.5304.108`인데 없어서 `107.0.5304.18`을 선택했다)

![image](https://user-images.githubusercontent.com/55564114/204453255-4bac4c59-202a-4e47-9405-7bb7808213a8.png)

> 자신의 환경에 맡는 걸로 다운로드 해준다. 나는 Window이니까 win32.zip을 다운로드했다. (자세히 따지면 64인데 64없으니까 32도 되겟지...?)

![image](https://user-images.githubusercontent.com/55564114/204453676-f89bcc96-f76e-48a0-804b-8036cfff933c.png)  

> 압축을 풀고, 폴더 안으로 이동한다. (압축을 풀면 `chromedriver.exe`가 있다)

![image](https://user-images.githubusercontent.com/55564114/204453876-ff9a5a5e-1fef-47ec-bfaf-8764b15a6013.png)

# 2. anaconda(아나콘다) 설치 및 실행 

> 설치 과정은 생략한다
> 1. 콘다 실행한다

![image](https://user-images.githubusercontent.com/55564114/204456136-9bf7925e-d8f3-4bd3-811e-72af579c7574.png)  

> 2. "conda create -n 가상환경이름" 입력한다
> (e.g. conda create -n alcr)

![image](https://user-images.githubusercontent.com/55564114/204457021-5652e348-250a-446b-86e5-3e90f04c263b.png)  

> 3. 도중에 뭐 물어보면 y 입력한다 (아마두 저장위치가 맡냐고 물어보는 것일거 같다)

![image](https://user-images.githubusercontent.com/55564114/204457149-d6b625d0-873e-40e3-8f5e-76068a27a323.png)  

![image](https://user-images.githubusercontent.com/55564114/204457501-062adf09-d73c-4d1d-9d4f-64691c368f01.png)

> 4. conda 실행하기 
> "conda activate alcr"
>> (아래 사진에서 base -> alcr 로 바꼈다면 정상적으로 콘다 실행완료)

![image](https://user-images.githubusercontent.com/55564114/204457639-e3edf5e0-6ec0-4b79-b001-34d2f5c91d67.png)  

> 5. conda 패키지 확인
> "conda list"
>> (방금 만든 가상환경이라 패키지가 1개도 없는게 정상~)

![image](https://user-images.githubusercontent.com/55564114/204457912-fcbf22e7-903e-4c55-8c69-43c0e7f2ec97.png)  

# 3. selenium 패키지 설치

> (conda 환경에서) "conda install selenium" 
> (도중에 y 입력하기)
>> "conda list" 입력해서 설치된 패키지를 확인해보면 python부터 pip 등등 생겼네요~

![image](https://user-images.githubusercontent.com/55564114/204458517-1cbf950f-643e-4dfc-be7d-a8a2dba99b42.png)  

# 4. 코드 실행 방법

> (디렉토리 이동) cd git 
> (디렉토리 이동) cd PJT_selenium_albamon
> (파일 실행) python main.py

``` python
[main.py]
    # 간단하게 구글페이지만 켜기 
    from selenium import webdriver
    driver = webdriver.Chrome()
    url = 'https://www.google.com'
    driver.get(url)
```

> 실행

![image](https://user-images.githubusercontent.com/55564114/204459868-80c781cf-248d-4f16-9bf1-8aa7b3aaf20c.png)  

> 결과 

![image](https://user-images.githubusercontent.com/55564114/204459960-09bd6f14-8f72-453f-8500-c70658d4b7f0.png)  

> 끄는법 
>> anaconda prompt 에서 ctrl + c 눌러야 종료된다
>>> 크롬페이지 닫는다고 종료안된다

