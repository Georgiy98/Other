from socket import *
from threading import Thread
from time import sleep
from random import randint
import dns.resolver
class DNS_Proxy_Server:
    def __init__(self, host='', file="config.txt"):

        # structure of config.txt:
        # main host
        # message if request is in black list
        # 1st black list's item
        # 2nd black list's item
        # ...
        # last black list's item

        self.host = host
        self.port = 53
        info = []
        with open(file, 'r') as config_file:
            info = config_file.readlines()
        self.main_address = info[0][:-1]
        self.bad_mesg = info[1][:-1]
        self.black_list = [line[:-1] for line in info[2:]]
        if self.black_list[-1] == '':
            self.black_list.pop(len(self.black_list) - 1)

    def start(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.clients = []
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = [self.main_address]
        Thread(target=self.listen).start()
        Thread(target=self.answer).start()

    def listen(self):
        while True:
            self.server.listen(1)
            self.clients.append(self.server.accept()[0])

    def answer(self):
        while True:
            for client in self.clients.copy():
                data = client.recv(1024)
                if data:
                    data = data.decode("utf-8")
                    if self.inBlackList(data):
                        Thread(target=lambda: client.send(bytes(self.bad_mesg, encoding="utf-8"))).start()
                    else:
                        res=""
                        try:
                            res=self.resolver.query(data,"A")
                            res = str(list(res)[0])
                        except:
                            res="DNS cannot found so server"
                        client.send(bytes(res,encoding="utf-8"))

    def inBlackList(self, domen):
        for black_domen in self.black_list:
            if black_domen in domen:
                return True
        return False

def start_client():  # Test clients to check
    #print("client started\n",end="")
    sock = socket(AF_INET, SOCK_STREAM)  # Only for Ipv4. It is easy to remake
    sock.connect(('192.168.43.78', 53))  # You should use here your ip
    #print("client connected\n",end="")
    text = test_list[randint(0, len(test_list) - 1)]
    sock.send(bytes(text, encoding="utf-8"))
    #print("client sent information\n",end="")
    data = sock.recv(1024)
    #print("client got information\n",end="")
    print("%-40s- %s\n"%(text,data.decode('utf-8')), end="")
    sock.close()


test_black_list = ['black1', 'black2', 'black3', 'black4', 'black5', 'black6', 'black7', 'black8', 'black9', 'black10',
                   'black11', 'black12', 'black13', 'black14']
test_list = ["telegram.org","youtube.com","facebook.com","google.com"]
test_list += test_black_list

serv = DNS_Proxy_Server()  # create dns proxy server
Thread(target=serv.start).start()  # start dns proxy server
sleep(1)
for i in range(5000):  # start clients
    Thread(target=start_client).start()
