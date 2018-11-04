from __future__ import print_function

from argparse import ArgumentParser
import json
import requests
import sys
import xml.etree.ElementTree as ET

class SiteReview(object):
    def __init__(self):
        self.baseurl = "https://sitereview.bluecoat.com/resource/lookup"
        self.headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

    def sitereview(self, url):
        payload = {"url": url, "captcha":""}
        
        try:
            self.req = requests.post(
                self.baseurl,
                headers=self.headers,
                data=json.dumps(payload),
            )
        except requests.ConnectionError:
            sys.exit("[-] ConnectionError: " \
                     "A connection error occurred")

        return

    def check_response(self, response):
        if self.req.status_code != 200:
            sys.exit("[-] HTTP {} returned".format(req.status_code))
        else:
            root= ET.fromstring(self.req.text)
            cats=[]
            for cat in root.findall("./translatedCategories/en/name"):
                cats.append(cat.text)
            self.categories = ', '.join(cats)
            self.url = root.find('url').text



def main(url):
    s = SiteReview()
    response = s.sitereview(url)
    s.check_response(response)
    border = "=" * (len("Symantec Site Review") + 2)

    print("\n{0}\n{1}\n{0}\n".format(border, "Symantec Site Review"))
    print("URL: {}\nCategories: {}\n".format(
        s.url,
        s.categories
        )
    )


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("url", help="Submit domain/URL to Symantec's Site Review")
    args = p.parse_args()

    main(args.url)
