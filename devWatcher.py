# simple dev server that causes served files to reload every 5 seconds

from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser

PORT = 8000

class LiveReloadHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()
        if self.path.endswith('.html'):
            self.wfile.write(b"""
                <script>
                    setTimeout(() => window.location.reload(), 5000);
                </script>
            """)

def start_server():
    server = HTTPServer(('', PORT), LiveReloadHandler)
    print(f'Serving at http://localhost:{PORT}')
    webbrowser.open(f'http://localhost:{PORT}')
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped')

if __name__ == '__main__':
    start_server()
