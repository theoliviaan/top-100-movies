# top-100-movies
Created a text file listing the top 100 movies of all time using BeautifulSoup


## WEB SCRAPING

```rb
## WEB SCRAPING

from bs4 import BeautifulSoup
import requests

movies_site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# import lxml


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

with open("movies.txt", mode="w") as file:
     for movie in movies:
         file.write(f"{movie}\n")


# print(movies)

```
