from pathlib import Path

import tomli
from pydantic import BaseModel


class ConfigDatabase(BaseModel):
    CONNECTION_STRING: str


class ConfigApp(BaseModel):
    ADDRESS: str
    PORT: int


class ConfigFile(BaseModel):
    DATABASE: ConfigDatabase
    APP: ConfigApp


config = ConfigFile.parse_obj(
    tomli.loads((Path(__file__).parent / "config.toml").read_text())
)
