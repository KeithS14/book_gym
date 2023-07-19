import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# SMTP server details
smtp_server = 'smtp-relay.sendinblue.com'
smtp_port = 587  # Example port, change it to the appropriate port for your SMTP server

# Email content and addresses
textfile_path = "textfile.txt"
to_email = "kscannell11@gmail.com"
from_email = "gymspotalert@gmail.com"

with open("textfile.txt", 'r', encoding='utf-8') as fp:
    # Read the contents of the file
    file_contents = fp.read()
    
    # Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Gym spot availible'
# me == the sender's email address
# family = the list of all recipients' email addresses
message = 'There is an availible spot for the red gym at x:xx'


# Create a text/plain message
msg = MIMEText(message)

# Create a text/plain message
#msg = MIMEText(file_contents)


# Set email headers
msg['From'] = from_email
msg['To'] = to_email

# Send the email
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        # Uncomment the following line if your SMTP server requires authentication
        #server.starttls()  # Enable a secure connection
        server.login('gymspotalerts@gmail.com', 'aPEDLxHpOWNk20mr')
        server.sendmail(from_email, to_email, msg.as_string())
    print("Email sent successfully!")
except smtplib.SMTPException as e:
    print("Error sending email:", str(e))

# 1113194489155166258
#f2e9ac0c2b7056ce7abc8dbf85693fea274c33dbcf71ec65d66be60aae601166