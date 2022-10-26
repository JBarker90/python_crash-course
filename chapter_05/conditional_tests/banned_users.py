banned_users = ['andrew', 'carolina', 'david']
your_user = input("Please type your name to see if you are blocked: ")

if your_user not in banned_users:
    print(f"{your_user.title()}, you are safe!")
else:
    print("Do not pass go! Do not collect $200!")