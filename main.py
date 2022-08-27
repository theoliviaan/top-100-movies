## WEB SCRAPING

from bs4 import BeautifulSoup
import requests

movies_site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# import lxml

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# all_anchor_tags = soup.findAll(name="a")
#
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)

# response = requests.get("https://news.ycombinator.com/")
# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, "html.parser")
#
# # using css selector
# # first_news = soup.select_one(selector=".titlelink")
# # print(first_news.string)
#
# # using find
# articles = soup.find_all(name="a", class_="titlelink")
# article_texts = []
# article_links = []
#
#
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)
#
# # article_upvote = soup.find_all(name="span", class_="score").getText()
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#

# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)
#
# print(article_texts[largest_index])

response = requests.get(movies_site)
movies_webpage = response.text

# print(movies_webpage)
soup = BeautifulSoup(movies_webpage, "html.parser")

# using find
movie_titles = soup.find_all(name="h3", class_="title")

# print(movie_titles.getText())
# using select
# art = soup.select(selector="section div h3")


movies = []
for one_movie in movie_titles:
    movie_text = one_movie.getText()
    # print(type(movie_text))
    # print(movie_text)

    try:
        number = movie_text.split(")")[0]
        movie_name = movie_text.split(")")[1]
        # print(movie_no)
    except IndexError:
        movie_name = movie_text.split(":")[1]
        number = movie_text.split(":")[0]

    number = int(number)
    movies.append(f"{number}) {movie_name}")

# reverse the list
movies = movies[::-1]

# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")







# print(movies)
