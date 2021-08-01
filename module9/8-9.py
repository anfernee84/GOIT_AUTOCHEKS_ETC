def get_emails(list_contacts):
    ls = list(map(lambda x : x['email'], list_contacts))
    return ls


spisok = [
     {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
     {
        "name": "Vasya Pupkin",
        "email": "vasya@pisem.net",
        "phone": "(992) 914-3792",
        "favorite": True,
    },
     {
        "name": "Gurbanguly Berdymuhamedov",
        "email": "gurbanguly@zhopa.tochikiston",
        "phone": "(992) 914-3792",
        "favorite": False,
    }  
]

print(get_emails(spisok))





