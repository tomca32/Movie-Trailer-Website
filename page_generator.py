import webbrowser
import os
import re

TEMPLATE_DIRECTORY = 'templates'
HTML_HEAD_FILENAME = 'head.html'
HTML_BODY_FILENAME = 'index.html'
HTML_MOVIE_FILENAME = 'movie.html'

def get_html_template(filename):
    '''Returns the HTML content of the passed file. Path to templates is defined by the TEMPLATE_DIRECTORY const.'''
    return open(TEMPLATE_DIRECTORY + '/' + filename, 'r').read()

def get_youtube_id(url):
    '''Returns the youtube id of a passed video url'''
    youtube_id_match = re.search(
        r'(?<=v=)[^&#]+', url)
    youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', url)
    return (youtube_id_match.group(0) if youtube_id_match else None)

def create_movie_tiles_content(movies):
    '''Returns generated HTML content for displaying the movies grid'''
    content = ''
    html = get_html_template(HTML_MOVIE_FILENAME)
    # Iterates through the passed movies and inserts their attributes into the html template
    for movie in movies:
        content += html.format(
            movie_title = movie.title,
            movie_description = movie.description,
            movie_year = movie.year,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = get_youtube_id(movie.trailer_youtube_url)
        )
    return content

def open_movies_page(movies):
    '''Generates fresh_tomatoes.html file from the passed movies and opens it in a web browser.'''
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = get_html_template(HTML_BODY_FILENAME).format(
        movie_tiles = create_movie_tiles_content(movies))

    # Output the file
    output_file.write(get_html_template(HTML_HEAD_FILENAME) + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
