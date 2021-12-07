from subprocess import sys
import os
def cleanConsole():
	command = 'clear'
	if os.name in ('nt','dos'):  # If Machine is running on Windows, use cls
		command = 'cls'
	os.system(command)

def validateUser():
	print("\tPrestaNow")
	user=input("USUARIO : ")
	passwprd=input("PASSWORD : ")
	if user == 'ANGEL'	and passwprd=='angel790347':
		return True
	return False	

def app():
	while True:
		is_validated = validateUser()
		cleanConsole()
		if is_validated:
			pass
		else:
			
			print("Invalid Credentials Try Again")


if __name__ == '__main__':
	app()
