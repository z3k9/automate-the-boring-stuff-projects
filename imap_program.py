import imapclient, pyzmail, imaplib

imap_obj = imapclient.IMAPClient('imap@example.com', ssl=True)

imap_obj.login('imap@example.com', 'MY_SECRET_PASSWORD')

imap_obj.select_folder('INBOX', readonly=True)

UIDs = imap_obj.search(['SINCE 05-Jul-2019'])
# UIDs = [40032, 40033, 40034, 40035, 40036, 40037,40038,40039,40040, 40041]

raw_messages = imap_obj.fetch([40041], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(raw_messages[40041][b'BODY[]'])
message.get_subject()
message.get_address('from')
message.get_address('to')
message.get_address('cc')
message.get_address('bcc')

if message.text_part != None:
    message.text_part.get_payload().decode(message.text_part.charset)

if message.html_part != None:
    message.html_part.get_payload().deconde(message.html_part.charset)


# Change the size of the fetched emails 
imaplib._MAXLINE = 10000000

# Fetching an email and marking it as read
# To do this you'll need to pass readonly= False to select_folder


# to delete emails
imap_obj.delete_messages(UIDs)

imap_obj.expunge()


imap_obj.logout()