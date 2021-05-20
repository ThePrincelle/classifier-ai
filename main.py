# python3
# main.py
# Entrypoint for classifier-ai project
# Created by Maxime Princelle
# --------------------------------------

import pandas as pd
from .classifier import classifier
from .imap.imap import IMAP as imap
from .input_cli import input_cli_start, ImapLoginInfo
from dotenv import load_dotenv
import os
import sys

def main(login_info=None):
	print("Email classification program powered by machine learning.")
	print("Created by Maxime Princelle\n")

	# Init variables
	mails = None
	imap_login = ImapLoginInfo()

	# Load .env or parameter
	if os.path.exists("./.env"):
		print("Load .env file.")
		load_dotenv(".env")

	if ("MAIL_ADDRESS" in os.environ) and ("MAIL_PASS" in os.environ) and ("MAIL_SERVER" in os.environ):
		imap_login.email = os.getenv("MAIL_ADDRESS")
		imap_login.password = os.getenv("MAIL_PASS")
		imap_login.server = os.getenv("MAIL_SERVER")
	else:
		if login_info is not None:
			imap_login.email = login_info['email']
			imap_login.password = login_info['password']
			imap_login.server = login_info['server']

	if imap_login.email == "" or imap_login.password == "" or imap_login.server == "":
		login_info = False
	else:
		login_info = imap_login

	# No input mode?
	if login_info:
		imap_login = login_info
	else:
		print("\nNo login info found, asking for them...")
		imap_login = input_cli_start()

	if imap_login:
		print(f"\nYour email address is: '{imap_login.email}'.")
		print(
			f"Your password is '{imap_login.password[:1]}...' no just kidding - "
			f"I'm not going to tell anyone. 🤫"
		)
		print(f"Your mailbox IMAP server is: {imap_login.server}.\n")

		# Check if export file
		if len(sys.argv) > 1 and sys.argv[1] == "-i":
			print(f"-i detected, importing data from ./export_{imap_login.email}.pickle")
			mails = pd.read_pickle(f"./export_{imap_login.email}.pickle")
		else:
			print("\nRetrieve mails from INBOX (takes a looong time...)")
			mailbox = imap(imap_login.email, imap_login.password, imap_login.server)
			mailbox.connect()

			mails = mailbox.fetch_mails_from_inbox()

		# print(mails)

		# If -e then export data.
		if len(sys.argv) > 1 and sys.argv[1] == "-e":
			print(f"-e detected, exporting data to ./export_{imap_login.email}.pickle")
			if os.path.exists(f"./export_{imap_login.email}.pickle"):
				os.remove(f"./export_{imap_login.email}.pickle")
			mails.to_pickle(f"./export_{imap_login.email}.pickle")

		# ML Processing
		categorised_mails = classifier(mails)

		print("\nCategories\n")
		print(categorised_mails.keys())

		print("\nDone.")
		return categorised_mails

	else:
		print("Error on getting mailbox login info.")


if __name__ == "__main__":
	main()
