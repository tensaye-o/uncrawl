import html
from newspaper import Article


def write_in(file, content, n=2):
    file.write(f"{html.escape(content)}" + ('\n' * n))


def process_article(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article


def write_list(file, title, items):
    write_in(file, f"## {title}")
    if items:
        for item in items[:-1]:
            write_in(file, item)
        write_in(file, items[-1])
    else:
        write_in(file, f"No {title.lower()} found")


def write_article_to_file(file, article: Article):
    sections = [
        ("", article.title),
        ("Authors", article.authors),
        ("Publish Date", [str(article.publish_date)]
         if article.publish_date else []),
        ("Keywords", article.keywords),
        ("Summary", [article.summary]),
        ("Full Content", [article.text]),
    ]

    for title, content in sections:
        if title:
            write_list(file, title, content)
        else:
            write_in(file, f"# {content}")
            print(article.title)


def uncrawl(url, path):
    """
    :type url: str
    :type path: int 
        path with markdown filename
    """
    file_name = path + '.md'

    with open(file_name, 'w'):
        pass

    article = process_article(url)
    with open(file_name, 'a') as file:
        write_article_to_file(file, article)
