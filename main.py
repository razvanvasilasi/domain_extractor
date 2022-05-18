def domain_name(url):
    from urllib.parse import urlparse
    result = urlparse(url).netloc.lstrip('www.')
    if len(result)>0:
        lst1=result.split('.')
        return lst1[0]
    else:
        lst1 = url.split('.')
        if 'www' in lst1[0]:
            return lst1[1]
        else:
            return lst1[0]
