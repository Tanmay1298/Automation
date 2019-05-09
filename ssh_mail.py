import subprocess as sp
		
ip = input("enter ip")

cmd1 = "scp /root/Desktop/pythonFiles/mail.py {}:/root/Desktop/mail.py".format(ip)

cmd2 = "ssh {} python36 /root/Desktop/mail.py".format(ip)

sp.getoutput(cmd1)
sp.getoutput(cmd2)

