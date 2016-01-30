#!/usr/bin/env python
#coding:utf-8

import imaplib

def checkGmail():
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
												msg = u"%s件の未読メールがあります。" % str(mcount)
								else:
												msg = u"未読メールはありません。"
				else:
								msg = u"メールを取得できません。"
				mail.close()
				mail.logout()
				return msg
