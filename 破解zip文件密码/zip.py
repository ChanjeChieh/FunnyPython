import zipfile

def pwdMaker():
    f = open('password.txt', 'w')
    for id in range(1000000):
        password = str(id).zfill(6) + '\n'
        f.write(password)
    f.close()

def extractFile(file, password):
    try:
        file.extractall(pwd=str.encode(password))
        return password
    except:
        return

def main():
    pwdMaker()
    file = zipfile.ZipFile('test.zip','r') # test.zip 是要解压文件夹的名字
    passFile = open('password.txt')
    print('暴力破解中，请稍后……')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(file, password)
        if(guess):
            print('\n密码是：' + password + '\n')
            exit(0)

if __name__ == '__main__':
    main()

