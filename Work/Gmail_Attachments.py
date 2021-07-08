import base64
import os
import email
import getpass, imaplib
import sys

with open('C:\\Users\\unism\\OneDrive\\Desktop\\académica\\Python\\Secrets.py') as f: 
    s = f.read()

# userName  = 'unismankur@gmail.com'
# passwd  = base64.b64decode(s).decode("utf-8")
# imap_ssl_host = 'imap.gmail.com'

user = 'unismankur@gmail.com'
password = base64.b64decode(s).decode("utf-8")
imap_url = 'imap.gmail.com'


# Function to get email content part i.e its body part 
def get_body(msg): 
    if msg.is_multipart(): 
        return get_body(msg.get_payload(0)) 
    else: 
        return msg.get_payload(None, True) 


def search(key, value, con):  
    result, data = con.search(None, key, '"{}"'.format(value)) 
    return data 
  
# Function to get the list of emails under this label 
def get_emails(result_bytes): 
    msgs = [] # all the email data are pushed inside an array 
    for num in result_bytes[0].split(): 
        typ, data = con.fetch(num, '(RFC822)') 
        msgs.append(data) 
  
    return msgs   


con = imaplib.IMAP4_SSL(imap_url)  
con.login(user, password)   

print('Successful Authentication')

con.select('Inbox') 
print('Step 1')
msgs = get_emails(search('FROM', 'unismankur@gmail.com', con)) 
print('Step 2')

for msg in msgs[::-1]:  
    for sent in msg: 
        if type(sent) is tuple:  
  
            # encoding set as utf-8 
            content = str(sent[1], 'utf-8')  
            data = str(content) 
  
            # Handling errors related to unicodenecode 
            try:  
                indexstart = data.find("ltr") 
                data2 = data[indexstart + 5: len(data)] 
                indexend = data2.find("</div>") 
  
                # printtng the required content which we need 
                # to extract from our email i.e our body 
                print(data2[0: indexend]) 
  
            except UnicodeEncodeError as e: 
                pass