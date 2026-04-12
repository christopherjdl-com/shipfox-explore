import base64
import os
from typing import Optional

from flask import Flask, request

APP_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(APP_DIR, "figure.png")
TEMPLATE_PATH = os.path.join(APP_DIR, "index.html")


def get_greeting(guest: Optional[str]) -> str:
    if guest is None:
        return ""
    cleaned = guest.strip()
    if not cleaned:
        return ""
    return f"Welcome {cleaned}"


def _load_image_data_uri() -> str:
    with open(IMAGE_PATH, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def _load_template() -> str:
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def create_app() -> Flask:
    app = Flask(__name__)
    image_data_uri = _load_image_data_uri()
    template = _load_template()

    @app.get("/")
    def index() -> str:
        guest = request.args.get("guest")
        greeting = get_greeting(guest)
        greeting_style = "" if greeting else 'style="display:none;"'
        return (
            template.replace("{{greeting}}", greeting)
            .replace("{{greeting_style}}", greeting_style)
            .replace("{{image_data_uri}}", image_data_uri)
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
