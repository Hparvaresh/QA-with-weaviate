from os import getenv, path
from pathlib import Path
from dotenv import load_dotenv

assert path.isfile("conf/env_example"), "couldn't find conf file"
dir_ = Path(__file__).resolve().parent
param_path = Path(__file__).resolve().parent.joinpath("env_example")
load_dotenv(param_path)

Weaviate_HOST = getenv("Weaviate_HOST", default=None)
