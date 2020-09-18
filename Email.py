
def send():
    import smtplib as email
    gserver= email.SMTP('smtp.gmail.com',587)
    gserver.starttls()
    gserver.login("mdmantejsingh@gmail.com","email_pwd")
    sender = 'mdmantejsingh@gmail.com'
    receivers = ['mdmantejsingh@gmail.com']

    message ="""From: Mantej Singh
To: Me 
Subject: Data is Cleaned!  

This is a test e-mail message. Data is extracted and cleaned
"""
#indentation is very imp here!!!
    gserver.sendmail(sender, receivers, message)         
    print ("Successfully sent email")
