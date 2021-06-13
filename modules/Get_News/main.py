import requests
from bs4 import BeautifulSoup


class GesNews:
    def __init__(self):
        # 初期化
        pass
        
    def content(self):
        # 内容の定義
        pass
    
    def get_news(self):
        def get_news():
        # yahooのサイトから情報取得
        response = requests.get('https://news.yahoo.co.jp')
        # レスポンスを成形
        html = BeautifulSoup(response.content, 'html.parser')
        # 特定のキーワードを抽出
        result = html.select(".sc-hmzhuo")
        
        for title in result:
            titles.append(title.text)
            
        return titles
