import string


def check_password_strength(password):
	"""Return a strength label and the checks passed by a password."""
	checks = {
		"At least 8 characters": len(password) >= 8,
		"Contains a lowercase letter": any(character.islower() for character in password),
		"Contains an uppercase letter": any(character.isupper() for character in password),
		"Contains a number": any(character.isdigit() for character in password),
		"Contains a special character": any(character in string.punctuation for character in password),
	}

	score = sum(checks.values())
	if score <= 2:
		strength = "Weak"
	elif score <= 4:
		strength = "Medium"
	else:
		strength = "Strong"

	return strength, checks


def main():
	password = input("Enter a password to check: ")
	strength, checks = check_password_strength(password)

	print(f"\nPassword strength: {strength}")
	print("Checks:")
	for check, passed in checks.items():
		status = "Pass" if passed else "Fail"
		print(f"- {check}: {status}")


if __name__ == "__main__":
	main()
