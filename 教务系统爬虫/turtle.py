import execjs, requests
import urllib.request
import urllib.parse

def get_des_psswd(data):
    jsstr = get_js()
    ctx = execjs.compile(jsstr) #加载JS文件
    return (ctx.call('encodeInp', data))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数

def get_js():
    f = open("jiami.js", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr

def download():
    img_url = 'http://jwgl.sdust.edu.cn/jsxsd/verifycode.servlet'
    req = urllib.request.Request(img_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
    req.add_header('Cookie', 'JSESSIONID=00550EB89D9F94AF593817085FF3544C')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
    try:
        response = urllib.request.urlopen(req)
        img_name = 'code.jpg'
        filename = img_name
        if(response.getcode() == 200):
            with open(filename, 'wb') as f:
                f.write(response.read())
            return filename
    except:
        return 'failed'

def login(encode, RANDOMCODE):
    data = {}
    data['encode'] = encode
    data['RANDOMCODE'] = RANDOMCODE
    data = urllib.parse.urlencode(data).encode('utf-8')
    posturl = 'http://jwgl.sdust.edu.cn/jsxsd/xk/LoginToXk' # 验证码图片地址
    req = urllib.request.Request(posturl, data)
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
    req.add_header('Accept-Encoding', 'gzip, deflate')
    req.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
    req.add_header('Cache-Control', 'no-cache')
    req.add_header('Connection','keep-alive')
    req.add_header('Content-Length','65')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('Cookie', 'JSESSIONID=00550EB89D9F94AF593817085FF3544C')
    req.add_header('Host','jwgl.sdust.edu.cn')
    req.add_header('Origin', 'http://jwgl.sdust.edu.cn')
    req.add_header('Pragma', 'no-cache')
    req.add_header('Referer', 'http://jwgl.sdust.edu.cn/jsxsd/xk/LoginToXk')
    req.add_header('Upgrade-Insecure-Requests','1')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
    response = urllib.request.urlopen(req)
    url = 'http://jwgl.sdust.edu.cn/jsxsd/framework/xsMain.jsp'
    rep = urllib.request.urlopen(url)
    htm = rep.read().decode('utf-8')
    print(htm)

if __name__ == '__main__':
    xh = input('请输入学号')
    pwd = input('请输入密码')
    encode = get_des_psswd(xh) + "%%%" + get_des_psswd(pwd)
    download()
    RANDOMCODE = input('清查看code.jpg并输入其中验证码')
    login(encode, RANDOMCODE)