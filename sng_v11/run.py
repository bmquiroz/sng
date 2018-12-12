# This runs a local test instance

from app import app


if __name__ == "__main__":
   app.run(host='10.0.0.102', port=5067, debug=False)
