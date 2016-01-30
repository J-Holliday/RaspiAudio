#!/usr/bin/env python

import imaplib

f = open("/home/pi/workspace/raspi-audio/mail/gmail.conf")
res = f.read()
ary = res.split("\n")
f.close()

SERVER_NAME = "imap.gmail.com"
USERNAME = ary[0] 
PASSWORD = ary[1]

mail = imaplib.IMAP4_SSL(SERVER_NAME)
mail.login(USERNAME, PASSWORD)
mail.list()
mail.select("Inbox")
st, mlist = mail.status('Inbox', "(UNSEEN)")

if st == "OK":
				mcount = int(mlist[0].split()[2].strip(').,]'))
				if mcount > 0:
								print("You have %s Mail.") % str(mcount)
				else:
								print("No new Mail.")
else:
				print("Can't get Mail status.")
mail.close()
mail.logout()
