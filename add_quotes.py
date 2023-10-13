from models import Authors, Quotes


def add_quotes(data):
    for item in data:
        a_name = item["author"]
        q_author = Authors.objects(fullname=a_name).first()
        quote = Quotes(tags=item["tags"], author=q_author, quote=item["quote"])
        quote.save()
