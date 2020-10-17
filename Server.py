import time
import datetime
import json
import requests


class Server:
        def A(self):
                print("11111")
        def push(self,message):
                print("ddd")
                SCKEY = 'SCU108040Tf09c907000038959b4d698f31583067a5f26356cc656a'
                now_time = datetime.datetime.now()
                bj_time = now_time + datetime.timedelta(hours=8)
                test_day = datetime.datetime.strptime('2020-12-19 00:00:00','%Y-%m-%d %H:%M:%S')
                date = (test_day - bj_time).days
                desp = f"""
------
### 现在时间：
```
{bj_time.strftime("%Y-%m-%d %H:%M:%S %p")}
```
### 打卡信息：
```
{message}
```
> 关于打卡信息
>
> 1、成功则打卡成功
>
> 2、系统异常则是打卡频繁

### ⚡考研倒计时:
```
{date}天
```

>
> [GitHub项目地址](https://github.com/ReaJason/17wanxiaoCheckin-Actions) 
>
>期待你给项目的star✨
"""

                headers = {
                    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
                }

                send_url = f"https://sc.ftqq.com/{SCKEY}.send"

                params = {
                    "text": f"完美校园健康打卡---{bj_time.strftime('%H:%M:%S')}",
                    "desp": desp
                }
                    
                # 发送消息
                response = requests.post(send_url, data=params, headers=headers)
                if response.json()["errmsg"] == 'success':
                        print("Server酱推送服务成功")
                else:
                        print("Something Wrong")
