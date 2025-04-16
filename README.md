# agent_sql_query_writer
# 🖥️ Langchain SQL Database Chat Agent

A Streamlit-based application that allows you to chat with SQL databases (SQLite or MySQL) using Langchain's SQL Agent powered by Groq's LLM (Gemma2-9b-It model).

## Features

- **Interactive Chat Interface**: Natural language interface to query your SQL databases
- **Multiple Database Support**:
  - Built-in SQLite3 database (`student.db`)
  - Connect to your own MySQL database
- **Powerful LLM Backend**: Uses Groq's fast LLM API with the Gemma2-9b-It model
- **Visual Query Execution**: See the agent's thought process as it generates SQL queries
- **Conversation History**: Maintains chat history during the session

## Prerequisites

- Python 3.7+
- Groq API key (get it from [Groq Cloud](https://console.groq.com/))
- For MySQL connections:
  - MySQL server credentials
  - `mysql-connector-python` package installed

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/langchain-sql-chat.git
   cd langchain-sql-chat
Install the required packages:

bash
Copy
pip install -r requirements.txt
Or install them manually:

bash
Copy
pip install streamlit langchain langchain-groq sqlalchemy mysql-connector-python
Usage
Run the application:

bash
Copy
streamlit run app.py
In the sidebar:

Select your database type (SQLite or MySQL)

If using MySQL, enter your connection details

Enter your Groq API key

Start chatting with your database in the main chat interface!

Database Setup
Using the included SQLite database
The app comes with a sample student.db SQLite database. Just select "Use SQLLite3 Database" in the sidebar.

Connecting to MySQL
Select "Connect to your MySQL Database" in the sidebar

Provide:

MySQL Host

MySQL User

MySQL Password

MySQL Database name

Configuration
You can modify the following aspects:

LLM model: Change model_name in the code (currently using "Gemma2-9b-It")

Cache duration: Adjust ttl in the @st.cache_resource decorator

Agent type: Modify AgentType in the create_sql_agent call

