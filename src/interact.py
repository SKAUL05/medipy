import requests
import json

MEDIUM_API = "https://api.rss2json.com/v1/api.json"
MEDIUM_HANDLER = "@kaul.sarath"


def print_output(output_list, header):
    print(header)
    print("===") * 20
    for out in output_list:
        print(out)
    print("===") * 20


def fetch_titles(story_json):
    titles = list()
    for item in story_json["items"]:
        titles.append(item["title"])
    return titles


if __name__ == "__main__":
    rss_uri = "https://medium.com/feed/{}".format(MEDIUM_HANDLER)
    response = requests.get(url=MEDIUM_API, params={"rss_url": rss_uri},)
    json_response = json.loads(response.text)
    returned_titles = fetch_titles(json_response)
    print_output(returned_titles, "Titles")
