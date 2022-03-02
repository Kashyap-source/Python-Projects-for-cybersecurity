from urllib.request import urlopen
cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'

def ClickJacking():
    host=input("Enter Host >>")
    port=int(input("Enter Port >>"))
    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print("could not fetch data for the given PORT")
    
    url = (port+host)

    data = urlopen(url)
    header = data.info()

    if not "X-Fram-Options" in headers:
        print(green+"website is vulnerable to clickJacking")
    else:
        print(red+"Website is not vulnerable to ClickJacking")

if __name__=="__main__":
    ClickJacking()

