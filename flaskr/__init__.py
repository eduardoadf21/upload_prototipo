from flask import Flask
import os

#application factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True )

    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, "uploads")   
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['ALLOWED_EXTENSIONS'] = ['.jpg','.jpeg','.png','.gif']

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
