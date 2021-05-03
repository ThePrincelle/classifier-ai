# python3
# main.py
# Entrypoint for tensorflow-ai project
# Created by Maxime Princelle
# --------------------------------------

# Main libraries

# Import IMAP library
from imap.imap import IMAP as imap
from input_cli import input_cli_start


def main():
    print("Email classification program powered by Tensorflow.")
    print("Created by Maxime Princelle")

    # No input mode?
    imap_login = input_cli_start()

    print(f"Your email address is: '{imap_login.email}'.")
    print(
        f"Your password is '{imap_login.password[:2]}...' no just kidding - "
        f"I'm not going to tell anyone. 🤫"
    )
    print(f"Your mailbox IMAP server is: {imap_login.server}.")


if __name__ == "__main__":
    main()