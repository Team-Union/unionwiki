from .tool.func import *

def main_error_403_2(conn):
    curs = conn.cursor()

    if os.path.exists('403.html') and flask.request.path != '/':
        return open('403.html', encoding='utf8').read()
    else:
        return redirect('/w/' + url_pas(wiki_set(2)))