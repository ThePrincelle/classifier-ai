# python3
# main.py
# Entrypoint for tensorflow-ai project
# --------------------------------------

# Main libraries
import questionary

# Import IMAP library
from imap.imap import IMAP as imap


def main():
    print("Hello World!")
    first_name = questionary.text("What's your first name?").ask()
    print("Your first name is: " + first_name)


if __name__ == "__main__":
    main()