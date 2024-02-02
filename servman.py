import os

def update_services(servname):
	print("PyOS Servman Utility 0.0.5")
	with open('oth/'+servname+'service.py') as bb:
		av = bb.read()
		print("Running service, please wait...")
		exec(av)

def update_conf(servname):
	print("PyOS Servman Utility 0.0.5")
	with open('conf/'+servname+'service.conf') as bb:
		av = bb.read()
		print(av)



def edit_conf(servname):
	print("PyOS Servman Utility 0.0.5")
	with open('conf/'+servname+'service.conf') as bf:
		print("Please wait, this feature isn't working right now.")
