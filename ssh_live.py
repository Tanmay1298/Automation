import subprocess as sp
		
ip = input("enter ip")

cmd1 = "scp /root/Desktop/pythonFiles/live_Stream.py {}:/root/Desktop/live.py".format(ip)

cmd2 = "ssh -X {} python36 /root/Desktop/live.py".format(ip)

#cmd3 = "scp {}:/root/Desktop/test.png /root/Desktop/remote.png".format(ip)

sp.getoutput(cmd1)
sp.getoutput(cmd2)
#sp.getoutput(cmd3)
