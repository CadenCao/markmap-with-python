from urllib.parse import quote

def url_genenate(markdown,host,port):
    markdown_quote=quote(markdown)
    return rf'http://{host}:{port}/markmap?markdown={markdown_quote}'

if __name__=='__main__':
    markdown="""# Heading1\n## Heading2\n### Heading3
    """
    host,port='127.0.0.1',5491
    url=url_genenate(markdown,host,port)
    print(url)