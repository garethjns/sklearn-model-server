import os


class Config:
    host: str = os.environ.get('MODEL_SERVER_REST_HOST', "0.0.0.0")
    port: str = "8000"
