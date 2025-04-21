
from app import create_app
from waitress import serve
import os

if __name__ == '__main__':
    port = os.environ.get('PORT', 8000)
    app = create_app()
    url_scheme = os.environ.get('URL_SCHEME', 'http')
    serve(app,host='0.0.0.0', port=port, url_scheme = url_scheme)