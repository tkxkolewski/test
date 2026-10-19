"""
Skrypt startowy serwera Polski Konwerter
Uruchomienie: py run_server.py
"""
import os
import sys
import uvicorn

if sys.platform == "win32":
    # Wymuszenie kodowania UTF-8 dla konsoli Windows
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    if sys.stderr.encoding != 'utf-8':
        sys.stderr.reconfigure(encoding='utf-8')

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    print(f"[*] Uruchamianie serwera Polski Konwerter pod adresem http://{host}:{port}")
    uvicorn.run("backend.app.main:app", host=host, port=port, reload=False)
