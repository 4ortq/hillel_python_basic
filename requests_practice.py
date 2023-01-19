import requests


url_data = 'https://jsonplaceholder.typicode.com/posts'
url_picture = 'https://www.meme-arsenal.com/memes/52365d75819cd9aebdb4c09db8e0d24f.jpg'

def request_data(data):
    res = requests.get(url = data)
    with open('content.txt', 'w') as f:
        f.write(res.text)
        print(res.json())
########################################################################################################
def requst_picture(picture):
    r = requests.get(url=picture)
    with open('picture.jpg','wb') as f:
        f.write(r.content)
request_data(url_data)
requst_picture(url_picture)

