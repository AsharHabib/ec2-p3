# routes need to be touched by import once to proc the app import/setup
from route import caliber, compare_batch

from config.flask_config import app

# from dotenv import dotenv_values


if __name__ == "__main__":
    # dotenv_values("../.env")
    app.run(debug=True, host='0.0.0.0', port=6500)