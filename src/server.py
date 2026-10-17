import logging
from fastmcp import FastMCP
from src.gmail_client import send_real_email

# Initialize server
mcp = FastMCP("Secure Gmail MCP Server")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp_server")

@mcp.tool()
def send_email(recipient: str, message: str) -> str:
    """Send an email message to a specified recipient (e.g., 'nicole').
    
    Args:
        recipient: The email address or name of the person receiving the message.
        message: The plain text content of the email body.
    """
    logger.info(f"Tool invoked: send_email -> recipient: {recipient}")
    return send_real_email(recipient=recipient, message=message)

if __name__ == "__main__":
    mcp.run()