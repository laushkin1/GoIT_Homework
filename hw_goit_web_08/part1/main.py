import connect
from models import Author, Quote
from cache import cache


@cache
def search_quotes(command, data):
    if command == "tag":
        quotes = Quote.objects(tags__icontains=data)
        return quotes
    elif command == "tags":
        data = data.split(",")
        quotes = Quote.objects(tags__in=data)
        return quotes
    elif command == "name":
        author = Author.objects(fullname__icontains=data).first()
        if author:
            quotes = Quote.objects(author=author)
            return quotes
        print("There is no such name in db.")
    else:
        print("There is no such data")
        return []


if __name__ == "__main__":
    while True:
        user_command = input(">>> ").strip()
        if user_command == "exit":
            break

        try:
            user_command, user_data = user_command.split(": ")
            quotes = search_quotes(user_command, user_data)
        except ValueError:
            print("Pleace enter: <command>: <value>")
            continue

        if quotes:
            for quote in quotes:
                author_fullname = quote.author.fullname
                quote_text = quote.quote
                author_fullname_utf8 = author_fullname.encode("utf-8").decode("utf-8")
                quote_text_utf8 = quote_text.encode("utf-8").decode("utf-8")

                print("-" * 75)
                print(f"Author: {author_fullname}")
                print(f'Tags: {", ".join(quote.tags)}.')
                print(f"Quote: {quote_text}")
                print()
