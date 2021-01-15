import requests
import bs4


def get_article(word):
    website = "https://de.pons.com/%C3%BCbersetzung/deutsch-englisch/" + word
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }

    res = requests.get(website, headers=headers)

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    article_element = soup.find_all("span", attrs={"class": "genus"})

    try:
        if word[0].isupper():
            if article_element[0].text == "m":
                return "der"
            elif article_element[0].text == "nt":
                return "das"
            elif article_element[0].text == "f":
                return "die"
            else:
                return ""
        else:
            return ""
    except IndexError:
        return ""
