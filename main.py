from movie import Movie
import fresh_tomatoes

fountain = Movie(
  "The Fountain",
  "As a modern-day scientist, Tommy is struggling with mortality, desperately searching for the medical breakthrough that will save the life of his cancer-stricken wife, Izzi.",
  "http://ia.media-imdb.com/images/M/MV5BMTU5OTczMTcxMV5BMl5BanBnXkFtZTcwNDg3MTEzMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
  "https://youtu.be/dAuxryJ6pv8")

donnie = Movie(
  "Donnie Darko",
  "A troubled teenager is plagued by visions of a large bunny rabbit that manipulates him to commit a series of crimes, after narrowly escaping a bizarre accident.",
  "http://ia.media-imdb.com/images/M/MV5BMTczMzE4Nzk3N15BMl5BanBnXkFtZTcwNDg5Mjc4NA@@._V1_SX214_AL_.jpg",
  "https://youtu.be/ZZyBaFYFySk")

sin_city = Movie(
  "Sin City",
  "A film that explores the dark and miserable town, Basin City, and tells the story of three different people, all caught up in violent corruption.",
  "http://ia.media-imdb.com/images/M/MV5BMTI2NjUyMDUyMV5BMl5BanBnXkFtZTcwMzU0OTkyMQ@@._V1_SY317_CR4,0,214,317_AL_.jpg",
  "https://youtu.be/T2Dj6ktPU5c")

print (fountain.title, fountain.description, fountain.poster_image_url, fountain.trailer_youtube_url)

movies = [fountain, donnie, sin_city]

fresh_tomatoes.open_movies_page(movies)