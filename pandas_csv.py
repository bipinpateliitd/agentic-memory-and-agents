from fastmcp import FastMCP
import os
import pandas as pd

# -------------------------------
# PandasCSVDatabase (SQLDatabase equivalent)
# -------------------------------
class PandasCSVDatabase:
    def __init__(self, base_dir: str):
        self.base_dir = os.path.abspath(base_dir)

        if not os.path.exists(self.base_dir):
            raise ValueError(f"Base directory does not exist: {self.base_dir}")

    def list_tables(self):
        return [f for f in os.listdir(self.base_dir) if f.endswith(".csv")]

    def get_path(self, csv_name: str):
        path = os.path.abspath(os.path.join(self.base_dir, csv_name))
        if not path.startswith(self.base_dir):
            raise ValueError("Access outside base directory is not allowed")
        return path


# -------------------------------
# Create DB instance (USER CONFIGURABLE)
# -------------------------------
BASE_DIR = "/home/bipin/Documents/genai/bot/learning/notebook/data"
db = PandasCSVDatabase(BASE_DIR)

# -------------------------------
# MCP Server
# -------------------------------
mcp = FastMCP("PandasCSV")


@mcp.tool()
def pd_list_tables():
    """List available CSV tables"""
    return db.list_tables()


@mcp.tool()
def pd_schema(csv_name: str):
    """Get schema and sample rows for a CSV table"""
    path = db.get_path(csv_name)
    df = pd.read_csv(path)

    return {
        "columns": df.dtypes.astype(str).to_dict(),
        "sample_rows": df.head(3).to_dict(orient="records"),
    }


@mcp.tool()
def pd_query(csv_name: str, pandas_query: str):
    """Run a pandas query on a CSV table"""
    path = db.get_path(csv_name)
    df = pd.read_csv(path)
    return df.query(pandas_query).to_dict(orient="records")


if __name__ == "__main__":
    mcp.run(transport="stdio")
