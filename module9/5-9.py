def format_phone_number(func):
    def wrapper(arg):
        numb = func(arg)
        if len(numb) == 12:
            numb = "+" + numb
        elif len(numb) == 10:
            numb = "+38" + numb
        return numb
    return wrapper



@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


print(sanitize_phone_number("+38(050)123-32-34"))