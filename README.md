# 概要

HTTP クライアントの例

## curl

ターミナル上で下記を実行

```sh
curl ${任意のURL}
```

## [HTTPie](https://httpie.io/)

1. [HTTPie](https://httpie.io/)をインストール
2. ターミナル上で下記を実行

```sh
http ${任意のURL}
```

## Python の HTTP クライアント

### [urllib](https://docs.python.org/ja/3/howto/urllib2.html)

```sh
docker compose run python python urllib_sample.py
```

### [Requests](https://requests.readthedocs.io/en/latest/)

```sh
docker compose run python python requests_sample.py
```

### [HTTPX](https://www.python-httpx.org/)

```sh
docker compose run python python httpx_sample.py
```
