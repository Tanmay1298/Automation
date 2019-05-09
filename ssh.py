import subprocess as sp
		
ip = input("enter ip")

cmd1 = "scp /root/Desktop/pythonFiles/cam.py {}:/root/Desktop/cam.py".format(ip)

cmd2 = "ssh {} python36 /root/Desktop/cam.py".format(ip)

cmd3 = "scp {}:/root/Desktop/Test.png /root/Desktop/remote.png".format(ip)

sp.getoutput(cmd1)
sp.getoutput(cmd2)
sp.getoutput(cmd3)
