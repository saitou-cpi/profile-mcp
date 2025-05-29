# profile-mcp
python -m venv .venv
source .venv/bin/activate

# FastMCP と実行に必要なランタイムをインストール
uv pip install -U fastmcp "uvicorn[standard]"


python server.py

sudo systemctl daemon-reload
sudo systemctl enable --now profile-mcp
sudo journalctl -u profile-mcp -f
