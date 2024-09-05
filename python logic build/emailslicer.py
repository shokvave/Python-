#collect email from user
#split email using @, save the first part as username and the second part as domain
#split the domain using . 
def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Input the email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension:", extension)

    
while True: 
    main()