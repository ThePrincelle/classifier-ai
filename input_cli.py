# input_cli.py
# Handles inputs from CLI
# --------------------------------------

# Main libraries
import questionary
import re


class ImapLoginInfo:
	email = ""
	password = ""
	server = ""


regex_email = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
regex_url = "[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)"


def input_cli_start():
	imap_login = ImapLoginInfo()
	print("\nPlease enter your login info for IMAP connection...")

	imap_login.email = questionary.text(
			"What's your email address?",
			default=imap_login.email,
			validate=lambda a: (
				True if (len(a) > 0 and re.search(regex_email, a)) else "You must enter an email address.")
		).ask() \
		or ""

	imap_login.password = questionary.password(
			"What's the password of your mailbox? (don't worry we don't keep it)",
			default=imap_login.password,
			validate=lambda a: (
				True if (len(a) > 2) else "You must enter a real password...")
		).ask() \
		or ""

	imap_login.server = questionary.text(
			"What's the server address of your mailbox? (IMAP URL)",
			default=imap_login.server,
			validate=lambda a: (
				True if (len(a) > 0 and re.search(regex_url, a)) else "You must enter a server URL.."
		)).ask() \
		or ""

	print("\nHere's your login info: ")
	print(f"Your email address is: '{imap_login.email}'.")
	print(
		f"Your password is '{imap_login.password[:2]}...' no just kidding - "
		f"I'm not going to tell anyone. 🤫"
	)
	print(f"Your mailbox IMAP server is: {imap_login.server}.")

	print()
	confirmation = questionary.confirm("is this correct?").ask()

	if confirmation:
		print("That is amazing! - Let's continue 💥🚀")
	else:
		print("That is unfortunate 🐡 - Well... Let's start again!")
		return input_cli_start()

	return imap_login
