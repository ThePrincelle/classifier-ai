# python3
# main.py
# Entrypoint for tensorflow-ai project
# Created by Maxime Princelle
# --------------------------------------

# Main libraries

# Import IMAP library
import pandas as pd
from imap.imap import IMAP as imap
from input_cli import input_cli_start, ImapLoginInfo
from dotenv import load_dotenv
import os
import sys

def main(login_info=None):
	print("Email classification program powered by machine learning.")
	print("Created by Maxime Princelle\n")

	# Init variables
	mails = None

	# Load .env or parameter
	load_dotenv(".env")
	imap_login = ImapLoginInfo()
	imap_login.email = os.getenv("MAIL_ADDRESS") or login_info.email
	imap_login.password = os.getenv("MAIL_PASS") or login_info.password
	imap_login.server = os.getenv("MAIL_SERVER") or login_info.server

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
			mails = pd.read_feather(open(f"./export_{imap_login.email}.feather", 'r'))
		else:
			print("\nRetrieve mails from INBOX...")
			mailbox = imap(imap_login.email, imap_login.password, imap_login.server)
			mailbox.connect()

			mails = mailbox.fetch_mails_from_inbox()

		print(mails)

		# If -e then export data.
		if len(sys.argv) > 1 and sys.argv[1] == "-e":
			print(f"-e detected, exporting data to ./export_{imap_login.email}.feather")
			if os.path.exists(f"./export_{imap_login.email}.feather"):
				os.remove(f"./export_{imap_login.email}.feather")
			mails.to_feather(f"./export_{imap_login.email}.feather")

	else:
		print("Error on getting mailbox login info.")


if __name__ == "__main__":
	main()
