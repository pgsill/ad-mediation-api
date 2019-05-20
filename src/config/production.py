from envparse import env

SQLALCHEMY_DATABASE_URI=env('SQLALCHEMY_DATABASE_URI', 'postgres://ad_network:4dn3tw0rk@postgres/ad_network')
PROPAGATE_EXCEPTIONS=False
SQLALCHEMY_TRACK_MODIFICATIONS=False
POPULATE_SAMPLE=env.bool('POPULATE_SAMPLE', default=False)
LOG_CONFIG={
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'default',
            'filename': "logs.txt",
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 3,
        }},
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file']
    }
}