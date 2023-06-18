from os import getenv, path
from pathlib import Path
from dotenv import load_dotenv


dir_ = Path(__file__).resolve().parent
param_path = Path(__file__).resolve().parent.joinpath("env_example")
assert path.isfile(param_path), "couldn't find env file"
load_dotenv(param_path)

Weaviate_HOST = getenv("Weaviate_HOST", default=None)
