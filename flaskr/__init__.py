from flask import Flask
import os

#application factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['UPLOAD_DIRECTORY'] = "flaskr/uploads/"
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['ALLOWED_EXTENSIONS'] = ['.jpg','.jpeg','.png','.gif']

    app.config.from_mapping(SECRET_KEY='dev',
                DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
                )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')


    return app



