from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
import pandas as pd 
from collections import defaultdict
from datetime import datetime

def crawling_one_page(page_num, pre_df, result_file):
   
    data_all_dict = defaultdict(list) # 데이터 저장용 딕셔너리 (전체)
    for i in range(1,21):
        print(f'({i}/20)')
        ### 상세 페이지 이동 
        if page_num == 1 : 
            driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div[2]/div[2]/form/div[5]/table/tbody/tr[{i}]/td[2]/div[1]/p[1]/a').click()
        else:
            driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/table/tbody/tr[{i}]/td[2]/div[1]/p[1]/a').click()
        ### 0.5초 대기
        time.sleep(1) 

        data_one_dict = defaultdict(str) # 데이터 저장용 딕셔너리 (하나) : 크롤링 도중 error가 발생하면 데이터 추가 안함 !
        data_one_dict['회사'] = ''
        data_one_dict['제목'] = ''
        data_one_dict['마감일'] = ''
        data_one_dict['인원'] = ''
        data_one_dict['성별'] = ''
        data_one_dict['연령'] = ''
        data_one_dict['학력'] = ''
        data_one_dict['우대사항'] = ''
        data_one_dict['급여'] = ''
        data_one_dict['근무기간'] = ''
        data_one_dict['근무요일'] = ''
        data_one_dict['근무시간'] = ''
        data_one_dict['업직종'] = ''
        data_one_dict['고용형태'] = ''
        data_one_dict['복리후생'] = ''
        data_one_dict['모집분야'] = ''
        try : 
            ### 회사명 
            company = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]').text
            data_one_dict['회사'] = company

            ### 제목
            title = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/h1').text  
            data_one_dict['제목'] = title

            ### 모집조건 ( 마감일 / 인원 / 성별 / 연령 / 학력 / 우대사항 )
            tbody = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/table/tbody')
            for tr in tbody.find_elements_by_tag_name("tr"):
                th = tr.find_elements_by_tag_name("th")[0].text 
                td = tr.find_elements_by_tag_name("td")[0]
                data_one_dict[th] = td.text

            ### 근무조건 ( 급여 / 근무기간 / 근무요일 / 근무시간 / 업직종 / 고용형태 / 복리후생 )
            tbody = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody')
            for tr in tbody.find_elements_by_tag_name("tr"):
                th = tr.find_elements_by_tag_name("th")[0].text 
                td = tr.find_elements_by_tag_name("td")[0]
                data_one_dict[th] = td.text

            for key , value in data_one_dict.items():
                if key == '업직종': # 업직종의 경우, value 값 앞에 '}' 에가 항상 붙어잇음, 이를 제거 
                    value = value[2:] 
                data_all_dict[key].append(value)

        except :
            print('-'*50)
            print('크롤링 중 에러가 발생했습니다 !!!')
            print('회사 :',company)
            print('제목 :',title)
            print('-'*50)
            pre_df.to_csv(f"{result_file}.csv", index = False) # 에러 발생할 경우, 이전것까지 저장

        ### 뒤로가기    
        driver.back()    

        ### 0.5초 기다리기
        time.sleep(1)

    for key , value in data_all_dict.items():
        print(key , ' 길이 :',len(value))

    return pd.DataFrame(data_all_dict)


if __name__ == "__main__" :
    print('크롤링을 시작합니다')

    ### 저장할 파일명 지정 
    now_time = datetime.now()
    result_file = now_time.strftime('%Y-%m-%d')
    print('저장 파일명 :',result_file+'.csv')

    driver = webdriver.Chrome() #또는 chromedriver.exe
    driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

    # 브라우저 화면 크기 변경하기
    driver.set_window_size(1080, 800) 

    # 크롤링 값을 저장한 df
    data_df = pd.DataFrame() 

    # 알바몬 홈페이지 
    PAGE = 'https://www.albamon.com/list/gi/mon_icon_list.asp?itype=10'

    driver.get(PAGE) # 페이지 가져오기(이동)

    time.sleep(1) # 1초 대기

    PAGE_NOW_NUM = 1 
    idx = 1 
    while True : 
        print('페이지 :',PAGE_NOW_NUM)
        if idx > 2 : 
            pass
        ### 최대 1초 기다리기
        time.sleep(1)

        data_df = pd.concat([data_df,crawling_one_page(PAGE_NOW_NUM,data_df,result_file)], ignore_index=True)

        ### number 버튼 조회 
        if PAGE_NOW_NUM == 1 :
            number_btn = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/form/div[6]/ul')
        else:
            number_btn = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/form/div[5]/ul')
        page_nums = list()
        for num in number_btn.find_elements_by_css_selector('li'):
            if num.text != '다음' and num.text != '이전':
                page_nums.append(int(num.text))


        ### 현재 페이지가 마지막 일 때
        if PAGE_NOW_NUM == page_nums[-1] :
            break

        ### 다음 페이지로 이동 
        PAGE_NOW_NUM += 1 
        number_btn.find_elements_by_xpath(f".//*[contains(text(), {PAGE_NOW_NUM})]")[0].click()
        idx += 1 


    
    ### 파일 저장 (.csv)
    data_df.to_csv(f"{result_file}.csv", index = False)

    driver.quit() # 웹 브라우저 종료. driver.close()는 탭 종료