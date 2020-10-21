import time
import datetime
import json
import requests


class Server:
        def push(self,message):
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
### 最热帖子：
"""
                desp =desp+message
                desp =desp+f"""

> 其他
>
> 1、仅仅抓取第一页信息
>
> 2、系统异常则是打卡频繁

### ⚡考研倒计时:
```
{date}天
```

>
> [CSDN博客](https://blog.csdn.net/qq_45197445) 
>
>期待你给项目的star✨
"""

                headers = {
                    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
                }

                send_url = f"https://sc.ftqq.com/{SCKEY}.send"

                params = {
                    "text": f"52最新热帖---{bj_time.strftime('%Y-%m-%d')}",
                    "desp": desp
                }
                    
                # 发送消息
                response = requests.post(send_url, data=params, headers=headers)
                if response.json()["errmsg"] == 'success':
                        print("Server酱推送服务成功")
                else:
                        print("Something Wrong")
