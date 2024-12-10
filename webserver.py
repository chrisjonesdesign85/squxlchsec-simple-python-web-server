# SQUXLCH-SEC SIMPLE PYTHON WEB SERVER
# created by: Squxlch

from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the server address and port
host = "0.0.0.0"  # Bind to all interfaces
port = 1337         # Standard HTTP port

# Create a request handler and HTTP server
class MyRequestHandler(SimpleHTTPRequestHandler):
    # To-Do: override methods to customize responses
    pass

def run_server():
    try:
        server_address = (host, port)
        httpd = HTTPServer(server_address, MyRequestHandler)
        print(f"Serving HTTP on {host} port {port} (http://{host}:{port}/)...")
        httpd.serve_forever()
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
