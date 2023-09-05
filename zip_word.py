import zipfile
import time


folder = input("path to the file: ")
zipf = zipfile.ZipFile(folderpath)

global results
result = 0

global duration
duration = time()

global tried
tried = 0
c=0

if not zipf:
    print("the zip/file or folder is not password protected! you can successfully open it :)")

else:
    starttime = time.time()
    wordListFile = open('wordList.txt','r',errors = 'ignore')
    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        password = word.encode('utf8').strip()
        c=c+1
        print('trying to decode password by:{}'.format(word))  
        try:
            with zipfile.ZipFile(folderpath,'r') as zf:
                zf.extractall(pwd=password)
                print("success the password is:"+word)
                endtime = time.time()
                result = 1
            break
        except:
            pass

if(result == 0):
    print("Sorry, password not found.A total of "+str(c)+ " possible combinations tried in "+str(duration)+"seconds, password has more the 4 characters.")

else:
    duration = endtime = starttime
    print('congratulation!!! password found after trying'+str(c)+'combinations in'+str(duration)+' seconds')



            

        








