# simple_email_formatter.py
def format_email(name, domain):
    email = f"{name}@{domain}"
    return email

if __name__ == "__main__":
    name = input("Enter name: ")
    domain = input("Enter domain: ")
    email = format_email(name, domain)
    print(f"Formatted email: {email}")
