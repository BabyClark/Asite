
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendemail(name,adress,content):
    from_addr="892114041@qq.com"
    to_addr="892114041@qq.com"
    # content=''
    name=name+': '+adress
    password="nwmgrtiqruecbahi"
    smtp_server="smtp.qq.com"
    meg= MIMEMultipart()
    meg["From"]=Header(from_addr)
    #meg["From"]='http'
    meg["To"]=Header(to_addr,'utf-8')
    meg["Subject"]=Header("网站建议form {}".format(name),"utf-8").encode()
    meg.attach(MIMEText(content,'plain','utf-8'))
    server=smtplib.SMTP_SSL(host=smtp_server,port=465)
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],meg.as_string())
    server.quit()

