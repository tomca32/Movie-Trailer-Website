from movie import Movie
import page_generator

fountain = Movie(
  "The Fountain",
  "As a modern-day scientist, Tommy is struggling with mortality, desperately searching for the medical breakthrough that will save the life of his cancer-stricken wife, Izzi.",
  2006,
  "http://ia.media-imdb.com/images/M/MV5BMTU5OTczMTcxMV5BMl5BanBnXkFtZTcwNDg3MTEzMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
  "https://youtu.be/dAuxryJ6pv8")

donnie = Movie(
  "Donnie Darko",
  "A troubled teenager is plagued by visions of a large bunny rabbit that manipulates him to commit a series of crimes, after narrowly escaping a bizarre accident.",
  2001,
  "http://ia.media-imdb.com/images/M/MV5BMTczMzE4Nzk3N15BMl5BanBnXkFtZTcwNDg5Mjc4NA@@._V1_SX214_AL_.jpg",
  "https://youtu.be/ZZyBaFYFySk")

sin_city = Movie(
  "Sin City",
  "A film that explores the dark and miserable town, Basin City, and tells the story of three different people, all caught up in violent corruption.",
  2005,
  "http://ia.media-imdb.com/images/M/MV5BMTI2NjUyMDUyMV5BMl5BanBnXkFtZTcwMzU0OTkyMQ@@._V1_SY317_CR4,0,214,317_AL_.jpg",
  "https://youtu.be/T2Dj6ktPU5c")

empire = Movie(
  "Star Wars: Empire Strikes Back",
  "After the rebels have been brutally overpowered by the Empire on their newly established base, Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by Darth Vader as part of his plan to capture Luke.",
  1980,
  "http://ia.media-imdb.com/images/M/MV5BMjE2MzQwMTgxN15BMl5BanBnXkFtZTcwMDQzNjk2OQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
  "https://youtu.be/96v4XraJEPI")

good_bad_ugly = Movie(
  "The Good, the Bad and the Ugly",
  "A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.",
  1966,
  "http://ia.media-imdb.com/images/M/MV5BOTQ5NDI3MTI4MF5BMl5BanBnXkFtZTgwNDQ4ODE5MDE@._V1_SX214_AL_.jpg",
  "https://youtu.be/JdkSuurdbDA")

matrix = Movie(
  "The Matrix",
  "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
  1999,
  "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
  "https://youtu.be/vKQi3bBA1y8")

movies = [fountain, donnie, sin_city, empire, good_bad_ugly, matrix]

page_generator.open_movies_page(movies)