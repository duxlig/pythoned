import smtplib
fromaddr='cruzarios@gmail.com'
toaddr='cruzarios@gmail.com'

msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: user_you@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
   ])


username='jorge@ievolutioned.com'
password='Pasion8576'
server=smtplib.SMTP('smtp.gmail.com:465')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr,toaddr,msg)
server.quit()
