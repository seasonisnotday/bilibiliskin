import requests,json,re,os,time,sys
from urllib import request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

print("作者b站@你看清楚了吗\n输入特定名称即可得到图片，另附文本显示表情位置，可以试试输入“汗”\n基于https://tool.bili.fan/emoji")
a=input("输入:")
url=r'https://bili2.unq.cc/api/biliemoji.php?action=search&kw={}&type=default'.format(a)
jsons = requests.get(url, headers=headers).text
dicts = json.loads(jsons)
path= './表情'
if os.path.exists(path) == False:
    os.mkdir(path)
    os.mkdir(path+'/图片')
else:
    print("请删除和程序同一文件夹下的" + "'"+'表情'+"'" + "文件夹")
    input('回车以结束')
    sys.exit(0)
def boat(ruid):
    file = open(path+'/表情名称.txt','a',encoding='utf-8')
    file.write(ruid+ '\n')
    file.close()
def zuo(ruid):
    uid1 = re.findall('\\[(.*?)_', ruid)
    txt = format('  '.join(uid1))
    return txt
try:
    for j in range(0, 2000, 1):
        name = dicts['data'][j]['item_name']
        image = dicts['data'][j]['image']
        id=dicts['data'][j]['id']
        print(str(j+1)+"---"+name)
        request.urlretrieve(image, path+'/图片/' + zuo(name) +' '+str(id)+ '.png')
        boat(name+"---"+str(id))
except:
    pass
input('完成，回车以结束')