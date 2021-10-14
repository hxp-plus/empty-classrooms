import requests
import sys

if(len(sys.argv) < 2):
    print("Please Input a Date in YYYY-MM-DD")
    sys.exit()

date = sys.argv[1]
import requests

cookies = {
    'BIGipServerpool_122.205.11.43_80': '2601126410.22811.0000',
    'JSESSIONID': '3FwMKpn9FGP91Fs-nljqb1tQt0kCbirAOWuX_yTyubb3w32lcn2p!2116535301',
}

headers = {
    'Host': 'hub.m.hust.edu.cn',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*',
    'Origin': 'http://hub.m.hust.edu.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030532)',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://hub.m.hust.edu.cn/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = {
  'buildingCode': 'C121%,%%E8%%A5%%BF%%E5%%8D%%81%%E4%%BA%%8C%%E6%%A5%%BCN',
  'borrowDate': date
}

response = requests.post('http://hub.m.hust.edu.cn/aam/room/selectFreeRoom.action', headers=headers, cookies=cookies, data=data, verify=False)


text_file = open("data/" + date + ".txt", "w")
text_file.write(response.text)
text_file.close()
