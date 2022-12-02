import pandas as pd 
import os 

def processing_num_of_people(x):
    p = list()
    p.append(x[:x.find('명')+1])
    if x.find('인원미정') != -1 :
        p.append('인원미정')
    if x.find('친구') != -1 :
        p.append('친구')
    return p

def processing_age(x):
    p = list()
    if x.find('무관') != -1 :
        p.append('무관')
        x = x[2:]
    else:
        p.append(x[:x.rfind(')')+1])
        x = x[x.rfind(')')+1:]
    x = x.strip().split()
    for i in x :
        p.append(i)
    return p

def processing_salary(x):
    p = [i for i in x.split('\n')]
    p.insert(1,p[0].split()[0]) # 급여형태
    p.insert(2,p[0].split()[1]) # 급여금액
    return p[1:] 

def processing_worktime(x):
    p = list()
    p.append(x.split()[0])
    x = ' '.join(x.split()[1:])
    if x.find('~') != -1 :
        p.append(x[:x.rfind(')')+1])
        x = x[x.rfind(')')+1:]
        p += x.split()
    else:
        p += x.split()
    return p

def processing_day_of_week(x):
    p = list()
    if x.find('요일협의') != -1 :
        p.append('요일협의')
        if len(x[5:]) > 1 :
            p.append(x[5:])
    else :
        x = x.split()
        p.append(x[0])
        x = ' '.join(x[1:])
        if len(x) > 1 :
            p.append(x)
    return p

def processing(df):
    '''
    - main.ipynb 를 py로 수정
    회사 : pass
    제목 : pass
    마감일 : pass 
    인원 -> 인원(00명) + 인원_추가사항(인원미정, 친구)
    성별 : pass 
    연령 -> 연령(2009~2003년생) + 연령_추가사항(청소년가능 등)
    학력 : pass 
    우대사항 : pass + fillna
    급여 : 급여형태(건별, 월급 등) + 급여금액(20000원) + 급여_추가사항(추후인상가능 등)
    근무기간 : 근무기간(1년이상 등) + 근무기간_추가사항(협의가능)
    근무요일 : 근무요일(주5일) + 근무요일_추가사항(월,화,수,목,금)
    근무시간 : 근무시간(0000~2300) + 근무시간_추가사항(휴계시간 60분)
    업직종 : pass 
    고용형태 : pass
    복리후생 : pass + fillna
    모집분야 : pass + fillna
    '''
    df['마감일'] = df['마감일'].apply(lambda x : ''.join(x.split()[0]))

    df['인원'] = df['인원'].apply(processing_num_of_people)
    df['인원_추가사항'] = df['인원'].apply(lambda x : "없음" if len(x) < 2 else ','.join(x[1:]))
    df['인원'] = df['인원'].apply(lambda x : ''.join(x[0]))

    df['연령'] = df['연령'].apply(processing_age)
    df['연령_추가사항'] = df['연령'].apply(lambda x : "없음" if len(x) < 2 else ','.join(x[1:]))
    df['연령'] = df['연령'].apply(lambda x : ''.join(x[0]))

    df['급여'] = df['급여'].apply(processing_salary)
    df['급여_추가사항'] = df['급여'].apply(lambda x : "없음" if len(x) < 3 else ','.join(x[2:]))
    df['급여형태'] = df['급여'].apply(lambda x : ''.join(x[0]))
    df['급여금액'] = df['급여'].apply(lambda x : ''.join(x[1]))

    df['근무기간'] = df['근무기간'].apply(processing_worktime)
    df['근무기간_추가사항'] = df['근무기간'].apply(lambda x : "없음" if len(x) < 2 else ','.join(x[1:]))
    df['근무기간'] = df['근무기간'].apply(lambda x : ''.join(x[0]))

    df['근무요일'] = df['근무요일'].apply(processing_day_of_week)
    df['근무요일_추가사항'] = df['근무요일'].apply(lambda x : "없음" if len(x) < 2 else ','.join(x[1:]))
    df['근무요일'] = df['근무요일'].apply(lambda x : ''.join(x[0]))

    df['근무시간'] = df['근무시간'].apply(lambda x : [x[:x.find('(')],x[x.find('('):]] if x.find('(') != -1 else [x])
    df['근무시간_추가사항'] = df['근무시간'].apply(lambda x : "없음" if len(x) < 2 else ','.join(x[1:]))
    df['근무시간'] = df['근무시간'].apply(lambda x : ''.join(x[0]))

    ### 결측치 처리
    df['우대사항'] = df['우대사항'].fillna("없음")
    df['복리후생'] = df['복리후생'].fillna("없음")
    df['모집분야'] = df['모집분야'].fillna("없음")

    return df

if __name__ == "__main__" :
    crawling_file_path = 'result'
    crawling_file_list = sorted([i for i in os.listdir(crawling_file_path) if i.find('re') == -1])
    if len(crawling_file_list) == 0 :
        raise Exception('저장된 크롤링데이터가 없어요') 

    latest_file_name = crawling_file_list[-1]
    # 원본 파일
    befor_df = pd.read_csv(os.path.join(crawling_file_path,latest_file_name), header=0)
    # 수정된 파일 
    after_df = processing(befor_df)

    # 저장 
    after_df.to_csv(f"result/re_{latest_file_name}", index = False)