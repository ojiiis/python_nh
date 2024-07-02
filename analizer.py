import requests
import string

def analize(content,character):
    count = 0
    for i in content:
        if i == character:
            count = count + 1
    return "You have {0} occurance of {1} in your content".format(count,character)













r = requests.get("https://trust-coin.github.io/app/signin.html")
if r.status_code == 200:
   
    f = open("login.html","w")
    f.write(r.content.decode())
    f.close()

 

    ch = list(string.ascii_lowercase)
    file = open("login.html","r")
    content = file.read()
    for i in ch:
      print(analize(content,i))
    file.close()