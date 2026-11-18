from fastapi import FastAPI

from guardflow import __version__

app = FastAPI(title="GuardFlow", version=__version__)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": __version__}
