from backend.app import app
from gevent import monkey
monkey.patch_all()

if __name__ == "__main__":
    app.run(debug=True)