def domain_name(url):
    url = url.split('//')[-1]
    url = url.split('www.')[-1]
    url = url.split('.')[0]

    return url


print(domain_name("http://www.zombie-bites.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
