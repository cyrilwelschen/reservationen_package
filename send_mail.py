import smtplib

from_address = "example@gmail.com"
to_address = "example@gmail.com"

msg = "Test cron job"

usr = "example.user"
pwd = "PASSWORD"

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(usr, pwd)
server.sendmail(from_address, to_address, msg)
server.quit()
