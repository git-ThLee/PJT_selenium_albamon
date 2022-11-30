# 프로젝트 설명

- 재택알바를 알아보기 위해 [알바몬](https://www.albamon.com/?utm_source=google&utm_medium=cpc&utm_campaign=000.%EB%B8%8C%EB%9E%9C%EB%93%9C&utm_content=000.%EB%B8%8C%EB%9E%9C%EB%93%9C&utm_term=%EC%95%8C%EB%B0%94%EB%AA%AC&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkpwFlhluFN7r9F_MsO7EZsBTVODoMmc6JOLe0YGR2q8Zf53fmxsmNEaAhBUEALw_wcB)에서 찾는 도중에 불필요한 정보가 너무 많았다. 그래서 필요한 정보만 보기위해 위 프로젝트를 시작한다.

- 시작일 : 2022년 11월 29일 (화) 
- ~~실패할수도있지만 일단 적어본다 ㅎ~~
- [파이썬 자동화(위키독스)](https://wikidocs.net/73537)
- [비전공자를 위한 파이썬 자동화(위키독스)](https://wikidocs.net/91474)

---

# 코드 실행 방법 

``` python
[VScode 환경]
    0. 새터미널 열기
    1. conda activate alcr
    # 만약 conda activate 해도 (alcr) 같은 표시가 안나타나면
    # conda init powershell 입력하고 다시 터미널 켜보기 
    2. python main.py 
    
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

