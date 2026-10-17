# Gmail MCP Server & AI Agent

A secure, modular Model Context Protocol (MCP) server connecting local AI agents directly to the official Gmail API.

---

## 🏗️ System Architecture

```mermaid
graph TD
    User([User Prompt]) --> Agent[src/agent.py <br/> Google Gemini LLM]
    
    subgraph Local MCP Project
        Agent -->|Tool Call: send_email| Server[src/server.py <br/> FastMCP Server]
        Server --> Client[src/gmail_client.py <br/> OAuth & MIME Wrapper]
        Client --> Config[src/config.py <br/> Pydantic Validator]
        Env[(.env File)] -.->|Loaded by| Config
    end

    Client -->|HTTPS / OAuth 2.0| GmailAPI[Google Gmail API]
    GmailAPI --> Recipient([Recipient Inbox])