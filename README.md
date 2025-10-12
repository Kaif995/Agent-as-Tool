# 🧠 Multi-Agent Shopping & Support System    

This project defines a triage-based multi-agent architecture powered by **Gemini 2.5 Flash** models. It helps users with shopping decisions and post-purchase support by intelligently routing queries to the right agent.

---
 
## 📦 Project Overview      

The system includes three specialized agents:

- **Triage Agent**: Routes user queries to the correct agent. It never responds directly and always delegates.
- **Shopping Agent**: Assists users in finding products and making purchase decisions.
- **Support Agent**: Handles post-purchase issues, returns, and customer support.

--- 

## 🧩 Agent Roles 

### 🔁 Triage Agent

- Acts as a dispatcher.
- Delegates all queries to either the shopping or support agent.
- Does not reply directly to users.
- Uses tools to invoke other agents.

### 🛍️ Shopping Agent

- Helps users discover products and make informed buying decisions.
- Replies always start with the 😍 emoji.
- Designed to be friendly and enthusiastic about shopping.

### 🛠️ Support Agent

- Assists users with post-purchase concerns like returns or complaints.
- Replies always start with the ✔ emoji.
- Focused on resolving issues efficiently and empathetically.

---

## 🛠 Features

- **Delegation Logic**: Queries are automatically routed based on intent (shopping vs. support).
- **Emoji Branding**: Each agent uses a unique emoji to signal its role.
- **Modular Design**: Agents are defined independently and can be extended or replaced easily.

---

## 🌐 Environment Configuration

The system relies on environment variables for secure access:

- `GEMINI_API_KEY`: API key for Gemini model access.
- `base_url`: Endpoint for Gemini API.

These should be stored in a `.env` file for local development.

---

## ✅ Usage

Once initialized, the triage agent listens for user queries and routes them accordingly:

- **Shopping-related queries** → Shopping Agent 😍  
- **Post-purchase queries** → Support Agent ✔

---

## 📚 Documentation Goals

This README is designed to:

- Explain the agent architecture.
- Clarify each agent’s role.
- Provide setup and usage guidance.
- Be ready for GitHub publishing.












