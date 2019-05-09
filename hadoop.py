#!/usr/bin/python36
import os
import subprocess
import getpass

##---------------------------------------------Taking Inputs-----------------------------------------##

ip = input("enter ip")
ch = input("Enter choice Master/Slave/Client/JT/TT")
hostname_master = input("Enter master's hostname")
hostname_jt = input("Enter jobtracker's hostname")

##---------------------------------------------Sending RPM Files--------------------------------------##

os.system("scp /root/Desktop/jdk-8u171-linux-x64.rpm  {}:/root/jdk-8u171-linux-x64.rpm ".format(ip))
os.system("scp /root/Desktop/hadoop-1.2.1-1.x86_64.rpm  {}:/root/hadoop-1.2.1-1.x86_64.rpm  ".format(ip))

##---------------------------------------------Installing JDK and Hadoop-----------------------------##

os.system("ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm".format(ip))
os.system("ssh {} 'echo export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/ >> /root/.bashrc'".format(ip))
os.system("ssh {} 'echo export PATH=/usr/java/jdk1.8.0_171-amd64/bin:$PATH >> /root/.bashrc'".format(ip))

os.system("ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(ip))

##--------------------------------------------Creating Master----------------------------------------##

if ch == "Master":
	os.system("ssh {} mkdir  /myname".format(ip))
	hdfs_master="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/myname</value>
</property>
</configuration>
"""
	file = open("/root/hdfs-site.xml",'w')
	file.write(hdfs_master)
	file.close()
	os.system("scp /root/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ip))


	core_master= """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>{}:9001</value>
</property>
</configuration>
""".format(hostname_master)
	file = open("/root/core-site.xml",'w')
	file.write(core_master)
	file.close()
	os.system("scp /root/core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
	
	os.system("ssh {} 'firewall-cmd --add-port=0-65535/tcp --permanent'".format(ip))
	os.system("ssh {} 'firewall-cmd --add-port=0-65535/udp --permanent'".format(ip))
	os.system("ssh {} 'hadoop namenode -format'".format(ip))
	os.system("ssh {} 'hadoop-daemon.sh start namenode'".format(ip))
	os.system("ssh {} 'watch jps'".format(ip))

##----------------------------------------------Creating Slave----------------------------------------##


elif ch == "Slave":
	os.system("ssh {0} 'mkdir {0} /data'".format(ip))
	hdfs_slave="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/data</value>
</property>
</configuration>
"""
	file = open("/root/hdfs-site.xml",'w')
	file.write(hdfs_slave)
	file.close()
	os.system("scp /root/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ip))


	core_slave="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>ps
<value>{}:9001</value>
</property>
</configuration>
""".format(hostname_master)
	file = open("/root/core-site.xml",'w')
	file.write(core_slave)
	file.close()
	os.system("scp /root/core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))

	os.system("ssh {} 'firewall-cmd --add-port=0-65535/tcp --permanent'".format(ip))
	os.system("ssh {} 'firewall-cmd --add-port=0-65535/udp --permanent'".format(ip))
	os.system("ssh {} 'hadoop-daemon.sh start datanode'".format(ip))
	os.system("ssh {} 'watch jps'".format(ip))

##-----------------------------------------------Creating Client----------------------------------------##


elif ch == "Client":
	core_client="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>ps
<value>{}:9001</value>
</property>
</configuration>
""".format(hostname_master)
	file = open("/root/core-site.xml",'w')
	file.write(core_client)
	file.close()

	os.system("scp /root/core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))

	mapred_client="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>
</configuration>
""".format(hostname_jt)
	file = open("/root/mapred-site.xml",'w')
	file.write(mapred_client)
	file.close()
	
	os.system("scp /root/mapred-site.xml {}:/etc/hadoop/mapred-site.xml".format(ip))

	os.system("ssh {} 'firewall-cmd --add-port=0-65535/tcp --permanent'".format(ip))
	os.system("ssh {} 'firewall-cmd --add-port=0-65535/udp --permanent'".format(ip))

##--------------------------------------------------Creating JobTracker--------------------------------##


elif ch == "JT":
	mapred_jt="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>
</configuration>
""".format(hostname_jt)
	file = open("/root/mapred-site.xml",'w')
	file.write(mapred_jt)
	file.close()
	
	os.system("scp /root/mapred-site.xml {}:/etc/hadoop/mapred-site.xml".format(ip))
	
	
	core_jt = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>ps
<value>{}:9001</value>
</property>
</configuration>
""".format(hostname_master)
	file = open("/root/core-site.xml",'w')
	file.write(core_jt)
	file.close()
	
	os.system("scp /root/core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
		
	os.system("ssh {} 'firewall-cmd --add-port=0-65535/tcp --permanent'".format(ip))
	os.system("ssh {} 'firewall-cmd --add-port=0-65535/udp --permanent'".format(ip))
	os.system("ssh {} 'hadoop-daemon.sh start jobtracker'".format(ip))
	os.system("ssh {} 'watch jps'".format(ip))

##--------------------------------------------Creating TaskTracker--------------------------------------##

elif ch == "TT":
	mapred_TT="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>
</configuration>
""".format(hostname_jt)
	file = open("/root/mapred-site.xml",'w')
	file.write(mapred_TT)
	file.close()
	
	os.system("scp /root/mapred-site.xml {}:/etc/hadoop/mapred-site.xml".format(ip))
		
	os.system("ssh {} 'firewall-cmd --add-port=0-65535/tcp --permanent'".format(ip))
	os.system("ssh {} 'firewall-cmd --add-port=0-65535/udp --permanent'".format(ip))
	os.system("ssh {} 'hadoop-daemon.sh start tasktracker'".format(ip))
	os.system("ssh {} 'watch jps'".format(ip))
else:
