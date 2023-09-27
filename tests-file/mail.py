import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("anprsys@gmail.com", "hrunzgcqpxrqbyzi")
 
# message to be sent
message = "Message_you_need_to_send"
 
# sending the mail
s.sendmail("anprsys@gmail.com", "jainv6464@gmail.com", message)
 
# terminating the session
s.quit()
