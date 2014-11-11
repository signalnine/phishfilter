import mailbox


phish_mbox = mailbox.mbox('phishing3.mbox')
for message in phish_mbox:
    if message['subject']:
        subject = message['subject'].decode('latin1')
        subject = subject.replace('\n', '')
        subject = subject.replace('\"', '')
        print "{\"text\": \"" + subject.encode('ascii', 'ignore') + "\", \"label\": \"phish\"},"

spam_mbox = mailbox.Maildir('/Users/gortiz/Downloads/2011/12/')
for message in spam_mbox:
    if message['subject']:
        subject = subject.replace('\n', '')
        subject = subject.replace('\"', '')
        subject = message['subject'].decode('latin1')
        print "{\"text\": \"" + subject.encode('ascii', 'ignore') + "\", \"label\": \"spam\"},"

