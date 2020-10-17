import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from Server import *
def main():
    for i in tqdm(range(1,5)):
        add = '&page=' + str(i)
        html = requests.get('https://www.52pojie.cn/forum.php?mod=guide&view=hot'+add)
        sever = 'https://www.52pojie.cn/'
        soup = BeautifulSoup(html.text, 'lxml')
        get = soup.find('div', class_='tl bm bmw')
        geta = get.find_all('a', class_='xst')
        
        # 返回信息封装组合
        dt = ''
        for x in geta:
            dt = dt+x.string+'\n'
    # 微信推送信息
    se = Server()
    se.push(dt)
if __name__ == "__main__":
    main()
