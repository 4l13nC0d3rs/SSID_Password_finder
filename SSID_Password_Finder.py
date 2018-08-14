__author__ = "Katoh jeremiah"

import os

#This will list all the save SSIDs on the systems
def ssid_finder():
	os.system("netsh wlan show profile")

#This will take the SSID and find a password match that is save on the system
def Password_finder(ssid):
	os.system("netsh wlan show profile " +ssid+" key=clear")

def main():
	ssid_finder() 
	SSID = raw_input("Please Enter SSID: ")
	password = Password_finder(SSID)
if __name__ == '__main__':
	main()