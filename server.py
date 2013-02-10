import os
from breathe_easy import app

port = int(os.environ.get('PORT', 3000))
app.debug = True
app.run('127.0.0.1', port)
