import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def SendMail():
    fromaddr = '03-033@mail.ru'
    toaddr = '03-033@mail.ru'
    mypass = 'NbdvyGcR7R6ULXngAwZq'
    reportname = "C:/PycharmProjects/Auto_Test_Mob_Py/Lesson4/task_1/log.txt"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Привет от Питона"

    with open(reportname, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachment; filename="%s"' %basename(reportname)
        msg.attach(part)

    body = "Это пробное сообщение"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()