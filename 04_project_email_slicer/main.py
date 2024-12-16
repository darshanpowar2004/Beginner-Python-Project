while True:
    email = input("Enter your email : ")

    if "@" not in email:
        print(f"the {email} is not valid email.")

    else:
        index = email.index("@")
        username =email[:index]
        domain = email[index + 1:]

        print(f"Your user name is {username}.\nYour domain is {domain}.")

        break
