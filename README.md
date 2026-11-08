python -m streamlit run streamlit_frontend_database.py
sqlite3 chatbot.db --> in terminal

Action-->	Command
Create venv	--> python3 -m .venv venv
Activate-->	source .venv/bin/activate

pip install -r requirements.txt

# test mcp server
uv run fastmcp dev inspector main.py 

# Run mcp server
uv run main.py

<!-- # How to add server to claud desktop
uv run fastmcp install claude-desktop main.py -->

<!-- my final mcp server: https://navsingh3211-calculator.fastmcp.app/mcp -->



<!-- import asyncio
from fastmcp import Client


async def main():

    server_url = "https://navsingh3211-calculator.fastmcp.app/mcp"

    async with Client(server_url, auth="oauth") as client:

        print("\nConnected to remote MCP server!")

        # Step 1: Get available tools
        tools = await client.list_tools()

        print("\nAvailable Tools:")

        for tool in tools:
            print(f"- {tool.name}: {tool.description}")

        # Step 2: Test addition tool
        print("\nTesting add tool...")

        result = await client.call_tool(
            "add",
            {
                "a": 10,
                "b": 20
            }
        )

        print("Addition Result:", result)

        # Step 3: Test random number tool
        print("\nTesting random_number tool...")

        random_result = await client.call_tool(
            "random_number",
            {
                "min_val": 1,
                "max_val": 100
            }
        )

        print("Random Number Result:", random_result)

        # Step 4: Read server information resource
        print("\nReading server information...")

        resource = await client.read_resource("info://server")

        print("Server Information:", resource)


if __name__ == "__main__":
    asyncio.run(main()) -->
