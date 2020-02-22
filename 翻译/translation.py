import urllib.request, urllib.parse, json

word = input('请输入需要翻译的内容：')

url = 'http://fanyi.youdao.com/translate'

'''
header = {}
header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
'''

data = {}
data['i'] = word
data['to'] = 'AUTO'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

target = json.loads(html)
print('翻译结果：' + target['translateResult'][0][0]['tgt'])

print(req.headers)