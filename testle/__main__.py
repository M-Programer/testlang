from sys import argv

def __main__(cmd="help", *args):
	match cmd:
		case "help":
			print("Commands:")
			print("help: views this help message.")
			print("create: creates a new testlang project.")
		case "create":
			print(f"Directory ‘{args[0]}’ will be created/wiped to create project, continue? [Y/n]")
			while (choice := input().lower()) not in "yn":
				choice = input("Continue? [Y/n]")
				if choice == "n":
					print("Terminating...")
					return # Go outside the function
				else:
					break # Go outside the loop
			print("Creating project...")

if __name__ == "__main__":
	args = argv[1:]
	__main__(*args)