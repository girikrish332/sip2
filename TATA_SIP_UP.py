import smtplib 
from datetime import datetime
from email.message import EmailMessage

try: 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 
    smtp.starttls() 
    smtp.login("ggdharan2413@gmail.com","")
    d = datetime.now()
    message = 'Subject: {}\n\n{}\n{}\n{}'.format('Alert !. BSNL SIP UP %s' %d, 'Need action. BSNL SIP is UP from Puducherry Elderline SIP Server.','Thanks and Regards,','Puducherry Elderline')
    smtp.sendmail("ggdharan2413@gmail.com", "girikrish332@gmail.com",message) 
    smtp.quit() 
    print ("Email sent successfully!") 
except Exception as ex: 
    print("Something went wrong....",ex)
