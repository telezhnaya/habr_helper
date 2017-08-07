
import habrahabr


with open('secret.txt') as f:
    client, token = f.read().strip().split(' ', 2)
    print(client, token)
    auth = habrahabr.Auth(client=client, token=token)
api = habrahabr.Api(auth)

posts = api.search.posts('python')
print(type(posts), posts)


