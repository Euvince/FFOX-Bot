import html2text


def clean_markdown(html: str) -> str:
    if not html:
        return ""

    h = html2text.HTML2Text()
    h.ignore_links = False # On garde les liens pour la suite
    h.ignore_images = True
    h.ignore_emphasis = False
    h.body_width = 0  # Pas de wrapping automatique

    markdown = h.handle(html)
    return markdown.strip()


""" html = "<h1>Title</h1><p>Hello <a href='https://example.com'>world</a></p>"
print(clean_markdown(html)) """