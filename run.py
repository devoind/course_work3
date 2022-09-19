# Основная программа

import default_config
from app.posts.views import posts_blueprint
from app.api.views import api_blueprint
from app import logger
from setup import create_app

app = create_app(default_config)

logger.create_logger()

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
