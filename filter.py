import mailbox
import nltk
from bs4 import BeautifulSoup
from textblob import TextBlob

def showpayload(message):
    payload = message.get_payload()
    if message.is_multipart():
        for subpart in payload:
            showpayload(subpart)
    else:
        if message.get_content_type() == "text/plain":
            return payload.decode('utf-8', 'ignore')
        if message.get_content_type() == "text/html":
            return BeautifulSoup(payload.decode('utf-8', 'ignore')).get_text()

phish_mbox = mailbox.mbox('phishing3.mbox')
training = {}
for message in phish_mbox:
    parsed_message = showpayload(message)
    if parsed_message:
        parsed_message = parsed_message.replace('\n', '')
        blob = TextBlob(parsed_message.encode('utf-8'))
        training[parsed_message.encode('utf-8')] = 'phish'

spam_mbox = mailbox.mbox('spam.mbox')
for message in spam_mbox:
    parsed_message = showpayload(message)
    if parsed_message:
        parsed_message = parsed_message.replace('\n', '')
        blob = TextBlob(parsed_message.encode('utf-8'))
        training[parsed_message.encode('utf-8')] = 'spam'

print training
