#!/usr/bin/env python3
from fastmcp import FastMCP
import json, pathlib

app = FastMCP(name="profile")

PROFILE = json.load(open(pathlib.Path(__file__).with_name("profile.json"), encoding="utf-8"))

@app.resource("data://profile/basic",
              name="BasicProfile",
              mime_type="application/json")
def get_profile():
    return PROFILE

if __name__ == "__main__":
    app.run(transport="streamable-http", bind="0.0.0.0:7789")
