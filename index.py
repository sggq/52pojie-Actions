import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from Server import *
def main():
    dt = ''
    # 页面范围1—5，但是只提取第一页的信息
    add = '&page=' + str(1)
    html = requests.get('https://www.52pojie.cn/forum.php?mod=guide&view=hot'+add)
    sever = 'https://www.52pojie.cn/'
    soup = BeautifulSoup(html.text, 'html.parser')
    get = soup.find('div', class_='tl bm bmw')
    geta = get.find_all('a', class_='xst')    
    # 返回信息封装组合
    count = 1
    for x in geta:
        dt = dt + str(count) +'. ##### ['+x.string+']('+sever+x.get('href')+')\n'
        count = count + 1
    # 微信推送信息
    se = Server()
    se.push(dt)
if __name__ == "__main__":
    main()
