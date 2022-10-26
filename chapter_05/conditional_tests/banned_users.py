banned_users = ['andrew', 'carolina', 'david']
your_user = input("Please type your name to see if you are blocked: ")

if your_user in banned_users:
    print("Do not go! Do not collect $200! ")
else:
    print("You are safe!")