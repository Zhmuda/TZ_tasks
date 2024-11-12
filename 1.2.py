import uvicorn
from fastapi import FastAPI, HTTPException
from typing import Dict
import hashlib

app = FastAPI()

url_store: Dict[str, str] = {}

def generate_short_url(original_url: str) -> str:
    return hashlib.md5(original_url.encode()).hexdigest()[:6]

@app.post("/shorten")
def shorten_url(original_url: str):
    short_url = generate_short_url(original_url)
    if short_url not in url_store:
        url_store[short_url] = original_url
    return {"short_url": short_url}

@app.get("/{short_url}")
def redirect_to_original(short_url: str):
    original_url = url_store.get(short_url)
    if original_url:
        return {"original_url": original_url}
    else:
        raise HTTPException(status_code=404, detail="URL not found")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
