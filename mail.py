#!/usr/bin/python36
import smtplib
email = input("Enter email to send message")
message = input("Enter message to send")
username = 'tanmaykhandal12988@gmail.com'
password = 'Tanmay98'
gmail_server = smtplib.SMTP(host='smtp.gmail.com', port= 587)
gmail_server.starttls()
gmail_server.login(username, password)
gmail_server.sendmail(username , '{}'.format(email),"{}".format(message))
msg.attach(MIMEImage(file("linux.jpg").read()))
gmail_server.quit()
