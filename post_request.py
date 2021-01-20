import requests

msg = {
    "args": {},
    "data": "{\"hello\": \"world\"}",
    "files": {},
    "form": {},
    "headers": {
        "Accept": "application/json, */*;q=0.5",
        "Accept-Encoding": "gzip",
        "Api-Key": "foo",
        "Cdn-Loop": "cloudflare",
        "Cf-Connecting-Ip": "192.241.133.165",
        "Cf-Ipcountry": "US",
        "Cf-Ray": "614bb288af37f015-FRA",
        "Cf-Request-Id": "07c32de96c0000f0158b17f000000001",
        "Cf-Visitor": "{\"scheme\":\"http\"}",
        "Connection": "Keep-Alive",
        "Content-Length": "18",
        "Content-Type": "application/json",
        "Host": "pie.dev",
        "User-Agent": "HTTPie/2.3.0"
    },
    "json": {
        "hello": "world"
    },
    "origin": "192.241.133.165",
    "url": "http://pie.dev/put"
}


if __name__ == '__main__':
    res = requests.post('http://localhost:5000/api/echo', json=msg)
    print(res)
    if res.ok:
        print(res.json())
