# python3
# main.py
# Entrypoint for tensorflow-ai project
# --------------------------------------

# Main libraries

# Import IMAP library
from imap.imap import IMAP as imap
from input_cli import input_cli_start


def main():
    # No input mode?
    imap_login = input_cli_start()

    print("Hello World!")

    print("Your first name is: " + imap_login)


if __name__ == "__main__":
    main()