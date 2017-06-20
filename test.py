POSTGRES = {
        'user': 'postgres',
            'pw': 'password',
                'db': 'my_database',
                    'host': 'localhost',
                        'port': '5432',
}
print('postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES)

