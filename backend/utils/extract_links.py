import re
from typing import List


def extract_links() -> List[str]:
    return [
        'https://github.com',
        'https://jsonplaceholder.typicode.com'
    ]


def extract_links_with_regex(markdown: str) -> List[str]:
    if not markdown:
        return []

    # Match des liens Markdown : [label](url)
    link_pattern = r'\[.*?\]\((http[s]?://[^\s)]+)\)'
    return re.findall(link_pattern, markdown)


md = """
Bonjour [Google](https://google.com),
ensuite [GitHub](https://github.com)
et [JsonPlaceholder](https://jsonplaceholder.typicode.com)
"""
# print(extract_links(md))