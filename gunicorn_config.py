# gunicorn_config.py
bind = '127.0.0.1:5000'
workers = 4
accesslog = '-'
errorlog = '-'
loglevel = 'info'