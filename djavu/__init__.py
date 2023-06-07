from flask import Flask
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True )

    app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, "images")   

    from djavu.controllers import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
