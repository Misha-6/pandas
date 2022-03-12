from flask import Flask

from src.ui.animal_info import *
from src.ui.save_file import save_blueprint
from src.ui.user_info import *

app = Flask(__name__)
app.register_blueprint(save_blueprint)
app.register_blueprint(info_blueprint)


@app.route("/")
def home():
    users = user_details()
    return render_template("index.html", users=users)


if __name__ == '__main__':
    app.run(debug=True)
