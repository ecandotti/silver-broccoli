import requests

Post = requests.post('http://127.0.0.1:5000/insert',
    json = {
        'url': 'http://youtube.com/',
        'title': 'Wonder Woman',
        }).status_code
if Post == 201:
    print(Post, "Post OK ✅")
else:
    print(Post, "Post KO ❌")

Get = requests.get('http://127.0.0.1:5000').status_code
if Get == 200:
    print(Get, "Get OK ✅")
else:
    print(Get, "Get KO ❌")

Put = requests.put('http://127.0.0.1:5000/update/3', 
    json = {
        'url': 'http://facebook.com/',
        'title': 'Wonder Woman',
        }).status_code
if Put == 200:
    print(Put, "Put OK ✅")
else:
    print(Put, "Put KO ❌")

Delete = requests.delete('http://127.0.0.1:5000/delete/1').status_code
if Delete == 200:
    print(Delete, "Delete OK ✅")
else:
    print(Delete, "Delete KO ❌")