import requests
import json
from collections import defaultdict 

MEDIUM_API = "https://api.rss2json.com/v1/api.json"
MEDIUM_HANDLER = "@kaul.sarath"


def print_output(output_list, header):
    print(header)
    print("===" * 20)
    for out in output_list:
        if type(out) == tuple:
            print(out[0], out[1])
        else:
            print(out)
    print("===" * 20)


def fetch_titles(story_json):
    titles = []
    for item in story_json["items"]:
        titles.append(item["title"])
    return titles

def fetch_categories(story_json):
    catg_list = set()
    catg_count = defaultdict(int)
    for item in story_json['items']:
        for category in item['categories']:
            catg_count[category] += 1
    sorted_catg = sorted(catg_count.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_catg

if __name__ == "__main__":
    rss_uri = "https://medium.com/feed/{}".format(MEDIUM_HANDLER)
    response = requests.get(url=MEDIUM_API, params={"rss_url": rss_uri},)
    json_response = json.loads(response.text)
    returned_titles = fetch_titles(json_response)
    print_output(returned_titles, "Titles")
    returned_categories = fetch_categories(json_response)
    print_output(returned_categories, "Categories")