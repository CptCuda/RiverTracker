import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Set the directory to the current script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        print("Opening browser...")
        webbrowser.open(f"http://localhost:{PORT}/")
        httpd.serve_forever()
except OSError as e:
    if e.errno == 10048:
        print(f"Port {PORT} is already in use. Please close the other server or try a different port.")
    else:
        raise e
except KeyboardInterrupt:
    print("\nServer stopped.")
