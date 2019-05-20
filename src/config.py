ENV='development'
MONGO_URI=""
DEBUG=True
SECRET=""
PROPAGATE_EXCEPTIONS=True
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
            'filename': "./logs/logs.log",
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 3,
        }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file']
    }
}