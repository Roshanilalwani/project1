import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "d990fe65cc9e70"
host_pass = "3df080eb7596ec"
guest_address = "roshanilalwani1111@gmail.com"
subject = "Regarding failure of rebuild.py"
content = '''Hello, 
				Developer is in the last commit regarding error . it is rebuild agin
			THANK YOU'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.mailtrap.io', 2525)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')



