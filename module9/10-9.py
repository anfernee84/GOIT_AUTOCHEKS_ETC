def get_favorites(contacts):
    return list(i for i in filter(lambda x : x['favorite'], contacts))





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

print(get_favorites(spisok))