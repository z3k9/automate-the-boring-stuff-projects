import ezgmail

#sending mail from a gmail account
ezgmail.send('recipient mail', 'subject', 'body')

# To attach files, provide an extra list of arguments to the send() function
ezgmail.send('recipient mail', 'subject', 'body', ['attachment.jpg', 'attachment.mp3'])

# to include cc and bcc
ezgmail.send('recipient mail', 'subject', 'body', cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')

# ezgmail has a GmailThread object and GmailMessage object to represent conversation threads and individual emails respectively
# A GmailThread object has a message attribute that holds a list of Gmailmessage objects. The unread() function returns a list of
# GmailThread objects for all unread emails which can be passed to ezgmail.summary() to print a summary of the conversation threads
# in that list

unread_threads = ezgmail.unread()
ezgmail.summary(unread_threads)

# To access specific messages and parts of messages, examine the message attribute of the GmailThread object. The message attribute
# contains a list of GmailMessage objects that make up the thread and these have subject, body, timestamp, sender and recipient attributes

print(unread_threads[0])
print(len(unread_threads[0].messages))

print(unread_threads[0].messages[0])

print(unread_threads[0].messages[0].subject)

# The ezgmail.recent() will return the 25 most recent threads, pass the optional maxResults to change this limit
ezgmail.recent(maxResults=100)

# You can perform search just like you'd on gmail webapp
ezgmail.search()

result_threads = ezgmail.search()
ezgmail.summary(result_threads)

# downloading attachments

threads = ezgmail.search('vacation photos')
threads[0].messages[0].attachments
threads[0].messages[0].downloadAllAttachments(downloadFolder='python_tutorial')
threads[0].messages[0].downloadAttachment('tulips.jpg')


