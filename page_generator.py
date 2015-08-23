import webbrowser
import os
import re

template_directory = "templates"

def get_youtube_id(url):
    youtube_id_match = re.search(
        r'(?<=v=)[^&#]+', url)
    youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', url)
    return (youtube_id_match.group(0) if youtube_id_match else None)

def create_movie_tiles_content(movies):
    content = ''
    html = get_movie_html()
    for movie in movies:
        content += html.format(
            movie_title = movie.title,
            movie_year = movie.year,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = get_youtube_id(movie.trailer_youtube_url)
        )
    return content

def get_page_body():
    return open(template_directory + '/index.html', 'r').read()

def get_movie_html():
    return open(template_directory + '/movie.html', 'r').read()

def get_page_head():
    return open(template_directory + '/head.html', 'r').read()

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = get_page_body().format(
        movie_tiles = create_movie_tiles_content(movies))

    # Output the file
    output_file.write(get_page_head() + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
