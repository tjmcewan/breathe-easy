import os
from breathe_easy import app


if __name__ == '__main__':
    if os.environ.get('PYTHON_ENV', '') == 'development':
        app.debug = True
    port = int(os.environ.get('PORT', 3000))
    app.run('0.0.0.0', port)
