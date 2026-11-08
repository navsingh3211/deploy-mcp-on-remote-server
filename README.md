python -m streamlit run streamlit_frontend_database.py
sqlite3 chatbot.db --> in terminal

Action-->	Command
Create venv	--> python3 -m venv venv
Activate-->	source .venv/bin/activate

pip install -r requirements.txt

# test mcp server
uv run fastmcp dev inspector main.py 

# run the server
uv run fastmcp run main.py

# How to add server to claud desktop
uv run fastmcp install claude-desktop main.py