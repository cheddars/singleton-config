from sconf import Config

conf = Config()

print(conf.cfg("celery", "rabbit_user"))