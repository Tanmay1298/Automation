#!/usr/bin/python36
import os
import subprocess
import getpass
os.system("tput setaf 1")
print("\t\t\t Hello Welcome To My Tools")
os.system("tput setaf 0")
print("\t\t\t----------------------")
while True:
	print("""
	Press 1 to check DATE
	Press 2 for CALENDER
	Press 3 for create a FILE
	Press 4 for create a USER
	Press 5 to Mail_A_Message
	Press 6 to click PHOTO
	Press 7 to make VIDEO
	Press 8 to create HADOOP(Only on remote)
	Press 9 to setup DOCKER	
	Press 10 to setup DockerWithAnsible
	Press 11 to setup WebServer
	Press 12 to FaceDetection
	Press 13 to FaceRecognition
	Press 14 to LiveSteamWithMobile
	Press 15 to EXIT
	""")

	print("Where you want to run your tools (remote/local)??")
	platform = input()

	print("Enter your choice")
	ch = int(input())

	if platform == "local":
		if ch == 1:
			print(subprocess.getstatusoutput("date"))
	
		elif ch == 2:
			print(os.system("cal"))

		elif ch == 3:
			print("Enter your filename")
			file_name = input()
			file_create_output = subprocess.getstatusoutput("touch {}".format(file_name))
			print("Your file created...!!!")
	
		elif ch == 4:
			print("Enter your username")
			user_name = input()
			user_create_output = subprocess.getstatusoutput("useradd {}".format(user_name))
			if user_create_output[0] == 0:
				print("Your user created...!!!")
			else:
				print("not created{}".format(user_create_output[1]))
		elif ch == 5:
			os.system("python36 mail.py")		
		elif ch == 6:
			os.system("python36 /root/Desktop/pythonFiles/cam.py")
		elif ch == 7:
			os.system("python36 /root/Desktop/pythonFiles/live_Stream.py")
		elif ch == 8:
			print("HADOOP will setup only on remote system")
		elif ch == 9:
			os.system("python36 docker_local.py")
		elif ch == 10:
			os.system("python36 ansible_docker.yml")
		elif ch == 11:
			os.system("python36 ansible_webserver.py")
		elif ch == 12:
			os.system("python36 facedetection.py")
		elif ch == 13:
			os.system("python36 facerecognition.py")
		elif ch == 14:
			os.system("python36 lsm.py")
			
		elif ch == 15:
			exit()
		else:
			print("Choose correct option")
	elif platform == "remote":
		remote_ip = input("Enter ip of another user :")
		if ch == 1:
			output=subprocess.getstatusoutput("ssh {} date".format(remote_ip))
			print(output)

		elif ch == 2:
			output=subprocess.getstatusoutput("ssh {} cal".format(remote_ip))
			print(output)

		elif ch == 3:
			print("Enter your filename")
			file_name = input()
			file_create_output = subprocess.getstatusoutput("ssh {} touch {}".format(remote_ip,file_name))
			print("Your file created...!!!")
		
		elif ch == 4:
			print("Enter your username")
			user_name = input()
			user_create_output = subprocess.getstatusoutput("ssh {} useradd {}".format(remote_ip,user_name))
			if user_create_output[0] == 0:
				print("Your user created...!!!")
			else:
				print("not created{}".format(user_create_output[1]))
		
		elif ch == 6:
			os.system("python36 ssh_mail.py")		
		elif ch == 5:
			os.system("python36 /root/Desktop/pythonFiles/ssh.py")
		elif ch == 6:
			os.system("python36 ssh_live.py")
		elif ch == 7:
			os.system("python36 hadoop.py")		
		elif ch == 8:
			os.system("python36 docker.py")		
		elif ch == 9:
			exit()
		else:
			print("Choose correct option")


