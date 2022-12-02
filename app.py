from flask import Flask, render_template, request
import main
import pandas as pd 
import csv 
import os 

app = Flask(__name__)

@app.route('/')
def index():
    # pandas를 이용하여 csv파일을 읽어온다.
    crawling_file_path = 'result'
    crawling_file_list = sorted([x for x in os.listdir(crawling_file_path) if x.find('re')!= -1])
    if len(crawling_file_list) == 0 :
        print("저장된 크롤링데이터가 없어요")
        return render_template('index.html')

    latest_file_name = crawling_file_list[-1]
    data = pd.read_csv(os.path.join(crawling_file_path,latest_file_name), header=0)
    return render_template('index.html', data = data, data_len = len(data))
    #return data.to_html()

if __name__ == '__main__':
    app.run(debug = True)