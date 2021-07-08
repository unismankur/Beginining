
import imaplib
import credentials
import base64

with open('C:\\Users\\unism\\OneDrive\\Desktop\\académica\\Python\\Secrets.py') as f: 
    s = f.read()
base64.b64decode(s).decode("utf-8")


imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
username = "unismankur@gmail.com"
password = base64.b64decode(s).decode("utf-8")
server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)

server.login(username, password)
# server.select('INBOX')

# data = server.uid('search',None, '(SUBJECT "MY QUERY HERE!")')
# print(data)