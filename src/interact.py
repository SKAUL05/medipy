import requests
import json

MEDIUM_API = "https://api.rss2json.com/v1/api.json"
MEDIUM_HANDLER = "@kaul.sarath"

if __name__ == "__main__":
    response = requests.get(
        url=MEDIUM_API,
        params={"rss_url": "https://medium.com/feed/{}".format(MEDIUM_HANDLER)},
    )
    print(json.loads(response.text))
