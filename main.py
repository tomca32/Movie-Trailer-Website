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


movies = [fountain, donnie, sin_city]

page_generator.open_movies_page(movies)