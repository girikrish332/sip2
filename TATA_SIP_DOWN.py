import smtplib 
from datetime import datetime
from email.message import EmailMessage

try: 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 
    smtp.starttls() 
    smtp.login("ggdharan2413@gmail.com","")
    d = datetime.now()
    message = 'Subject: {}\n\n{}\n{}\n{}'.format('Alert !. TATA SIP DOWN %s' %d, 'Need action. TATA SIP is Down from Puducherry Elderline SIP Server.','Thanks and Regards,','Puducherry Elderline')
    smtp.sendmail("ggdharan2413@gmail.com", "girikrish332@gmail.com",message) 
    smtp.quit() 
    print ("Email sent successfully!") 
except Exception as ex: 
    print("Something went wrong....",ex)
