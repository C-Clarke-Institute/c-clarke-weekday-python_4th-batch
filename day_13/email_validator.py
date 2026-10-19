
def validate_email(email):

    if '@' not in email:
        return False

    if email.startswith('@') or email.endswith('@') or email.count('@') > 1:
        return False
    else:
        return True

is_valid_email = validate_email("g@test.gmail.com")

print(is_valid_email)
