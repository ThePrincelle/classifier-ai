# input_cli.py
# Handles inputs from CLI
# --------------------------------------

# Main libraries
import questionary


def input_cli_start():
	first_name = questionary.text("What's your first name?").ask()
	return first_name
