import requests

url_data = 'https://jsonplaceholder.typicode.com/posts'
url_picture = 'https://www.meme-arsenal.com/memes/52365d75819cd9aebdb4c09db8e0d24f.jpg'
res = requests.get(url = url_data)
with open('content.txt', 'w') as f:
    f.write(res.text)
    print(res.json())
########################################################################################################
r = requests.get(url=url_picture)
with open('picture.jpg','wb') as f:
    f.write(r.content)

