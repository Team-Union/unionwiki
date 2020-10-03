from .tool.func import *

def main_error_400_2(conn):
    curs = conn.cursor()

    if os.path.exists('400.html') and flask.request.path != '/':
        return open('400.html', encoding='utf8').read()
    else:
        return redirect('/w/' + url_pas(wiki_set(2)))
def main_error_403_2(conn):
    curs = conn.cursor()

    if os.path.exists('403.html') and flask.request.path != '/':
        return open('403.html', encoding='utf8').read()
    else:
        return redirect('/w/' + url_pas(wiki_set(2)))

def main_error_404_2(conn):
    curs = conn.cursor()

    if os.path.exists('404.html') and flask.request.path != '/':
        return open('404.html', encoding='utf8').read()
    else:
        return redirect('/w/' + url_pas(wiki_set(2)))

def main_error_410_2(conn):
    curs = conn.cursor()

    if os.path.exists('410.html') and flask.request.path != '/':
        return open('410.html', encoding='utf8').read()
    else:
        return redirect('/w/' + url_pas(wiki_set(2)))

def main_error_429_2(conn):
    curs = conn.cursor()

    if os.path.exists('429.html') and flask.request.path != '/':
        return open('429.html', encoding='utf8').read()
    else:
        return redirect('/w/' + url_pas(wiki_set(2)))
def main_error_500_2(conn):
    curs = conn.cursor()

    if os.path.exists('500.html') and flask.request.path != '/':
        return open('500.html', encoding='utf8').read()
    else:
        return redirect('/w/' + url_pas(wiki_set(2)))
def main_error_503_2(conn):
    curs = conn.cursor()

    if os.path.exists('503.html') and flask.request.path != '/':
        return open('503.html', encoding='utf8').read()
    else:
        return redirect('/w/' + url_pas(wiki_set(2)))
def main_error_504_2(conn):
    curs = conn.cursor()

    if os.path.exists('504.html') and flask.request.path != '/':
        return open('504.html', encoding='utf8').read()
    else:
        return redirect('/w/' + url_pas(wiki_set(2)))