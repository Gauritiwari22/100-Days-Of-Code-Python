import requests
from bs4 import BeautifulSoup

url="https://news.ycombinator.com/"
response=requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")
articles=soup.find_all("a", class_="titlelink")

for article in articles:
    print(article.getText())

for article in articles:
    title=article.getText()
    link=article.get("href")

    print(title)
    print(link)

scores=soup.find_all("span", class_="score")

for score in scores:
    print(score.getText())


scores=[int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]
max_score=max(scores)
print(max_score)