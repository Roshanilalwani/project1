import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "smtp.mailtrap.io"
host_pass = "3df080eb7596ec"
guest_address = "roshanilalwani1111@gmail.com"
subject = "Regarding failure of main.py"
content = '''Hello, 
				Your mail is sent successfully.Developer used the commit and it failed
			THANK YOU'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')



