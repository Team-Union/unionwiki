from .tool.func import *

def main_error_503_2(conn):
    curs = conn.cursor()

    if os.path.exists('503.html') and flask.request.path != '/':
        return open('503.html', encoding='utf8').read()
    else:
        return redirect('/w/' + url_pas(wiki_set(2)))