"""Optional Python static server for VYRO Studio. No dependencies required."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)

class Handler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map,
                      ".js": "text/javascript", ".webmanifest": "application/manifest+json"}

if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    print(f"VYRO Studio running at http://{address[0]}:{address[1]}")
    print("Press Ctrl+C to stop.")
    ThreadingHTTPServer(address, Handler).serve_forever()
