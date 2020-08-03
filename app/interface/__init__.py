import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask

from app.infrastructure.config import app_config
from app.infrastructure.log import logger


def create_app(config=app_config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    from .api import api
    api.init_app(app)

    logger.info('start up')
    return app

