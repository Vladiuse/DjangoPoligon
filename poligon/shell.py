from django.db import connection
from django.db import reset_queries
from faker import Faker


OLD_Q = list()


def format_sql_query(string):
    return string.replace('WHERE', ' '*4+'\nWHERE')

def show_querys(show,reset=True, time=False):
    global OLD_Q
    # qs = connection.queries
    qs = show
    print('\n')
    for i, q in enumerate(qs):
        show_time = ''
        if time:
            show_time = f"Time: {q['time']}"
        query = format_sql_query(q['sql'])
        print(f'[{i}]', show_time, query, )

    print(f'\n-- {len(qs)} queries --')

    if reset:
        OLD_Q += qs
        reset_queries()


class SHowQ:

    def __init__(self, show):
        self.show = show

    def __repr__(self):
        if isinstance(self.show, list):
            show_querys(self.show)
        else:
            show_querys(self.show.queries)
        return ''


S = SHowQ(connection)
SO = SHowQ(OLD_Q)
faker = Faker()

print('Import Shell')


