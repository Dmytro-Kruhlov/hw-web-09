import json
from models import Authors





def add_authors(data):
    for item in data:
        author = Authors(
            fullname=item["fullname"],
            born_date=item["born_date"],
            born_location=item["born_location"],
            description=item["description"]
        )
        author.save()





