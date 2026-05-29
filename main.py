def email_tekshir(email):
    if '@' in email:
        return True
    else:
        return False

email = input("Email kiriting: ")
if email_tekshir(email):
    print("Email '@' belgisi mavjud.")
else:
    print("Email '@' belgisi yo'q.")
