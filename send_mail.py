import smtplib

from_address = "cyril.welschen@gmail.com"
to_address = "cj.welschen@gmail.com"

msg = "Test crown job"

usr = "cyril.welschen"
pwd = "PASSWORD"

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(usr, pwd)
server.sendmail(from_address, to_address, msg)
server.quit()
