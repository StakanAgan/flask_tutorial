#!.venv/bin/python
from microblog import app as application

if __name__ == '__main__':
    application.run(host='0', port=5000, debug=True)