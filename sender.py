import smtplib
fromaddr='jorge@ievolutioned.com'
toaddr='bensandsower@gmail.com'

msg = "\r\n".join([
  "From: jorge@ievolutioned.com",
  "To: bensandsower@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
   ])


username='jorge@ievolutioned.com'
password='Pasion8576'
server=smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr,toaddr,msg)
server.quit()
