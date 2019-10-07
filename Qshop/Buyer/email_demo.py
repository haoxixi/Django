import smtplib
from email.mime.text import MIMEText
subject = "明天要穿长袖"
content = """
123123
123123

"""
sender = "15225467786@163.com"
recver = """
1783297132@qq.com
"""

password = "123456abc"

message = MIMEText(content,"plain","utf-8")

message["Subject"] = subject
message["From"] = sender
message["To"] = recver
smtp = smtplib.SMTP_SSL("smtp.163.com",465)
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(",\n"),message.as_string())
smtp.close()