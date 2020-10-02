from .tool.func import *

def vote_end_2(conn, num):
    curs = conn.cursor()

    curs.execute(db_change('select name, subject, data, type from vote where id = ? and user = ""'), [num])
    data_list = curs.fetchall()
    if not data_list:
        return redirect('/vote')

    data = '' + \
        '<h2>' + data_list[0][0] + '</h2>' + \
        '<b>' + data_list[0][1] + '</b>' + \
    ''

    if admin_check() == 1:
        if data_list[0][3] == 'open' or data_list[0][3] == 'n_open':
            data += '' + \
                '<hr class="main_hr">' + \
                '<a href="/close_vote/' + num + '">(' + load_lang('close_vote') + ')</a>' + \
            ''
        else:
            data += '' + \
                '<hr class="main_hr">' + \
                '<a href="/close_vote/' + num + '">(' + load_lang('re_open_vote') + ')</a>' + \
            ''

    vote_data = re.findall(r'([^\n]+)', data_list[0][2].replace('\r\n', '\n'))
    for i in range(0, len(vote_data)):
        data += '<h2>' + vote_data[i] + '</h2>'
        data += '<ul>'
        
        curs.execute(db_change('select user from vote where id = ? and user != "" and data = ?'), [num, str(i)])
        data_list_2 = curs.fetchall()
        if data_list[0][3] == 'open' or data_list[0][3] == 'close':
            all_ip = ip_pas([j[0] for j in data_list_2])
            for j in data_list_2:
                data += '<li>' + all_ip[j[0]] + '</li>'

        data += '<li>' + load_lang('result') + ' : ' + str(len(data_list_2)) + '</li>'
        data += '</ul>'

    return easy_minify(flask.render_template(skin_check(),
        imp = [load_lang('result_vote'), wiki_set(), custom(), other2([0, 0])],
        data = data,
        menu = [['vote', load_lang('return')]]
    ))