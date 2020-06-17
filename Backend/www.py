from application import app
from pages.api import api

app.register_blueprint(api, url_prefix="/api")
# app.register_blueprint(get_data, url_prefix="/get_data")
