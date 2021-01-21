import requests

if __name__ == '__main__':

    res = requests.post('http://localhost:5000/api/echo', json={"hello": "world"})
    print(res)
    if res.ok:
        print(res.json())
