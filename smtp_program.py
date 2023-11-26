import smtplib


# SMTP deals with sending emails to others, a different protocol IMAP handles recieving emails

smtp_obj = smtplib.SMTP('smtp@example.com',587) # create your smtp object representing the connection to an smtp server

smtp_obj.ehlo() # Establish a connection to the server. If the first item in the returned tuple is integer 250(code for 'success' in SMTP) then the greeting succeeded

smtp_obj.starttls() # puts smtp connection in tls mode. The 220 in the return value says server is ready.

smtp_obj.login('bob@example.com', 'MY_SECRET_PASSWORD')

smtp_obj.sendmail('bob@example.com', 'alice@example.com', 'Subject: so long dear Alice \nDear Alice, so long and thanks for the fish.\nSincerly, Bob')

smtp_obj.quit()

