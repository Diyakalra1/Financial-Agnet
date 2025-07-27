from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
import phi.api
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
import phi
from phi.playground import Playground, serve_playground_app

## load the environment variables from .env file
load_dotenv()
phi.api=os.getenv("PHI_API_KEY")

#web search Agent
web_search_agent=Agent(
  name='Web Search Agent',
  role='Search the web for updates',
  model=Groq(id='llama-3.3-70b-versatile'),
  tools=[DuckDuckGo()],
  instructions=['Always include resources'],
  show_tools_calls=True,
  markdown=True,

)

#Financial Agent
finance_agent=Agent(
name='Financial AI Agent',
model=Groq(id='llama-3.3-70b-versatile'),
  tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    
    instructions=["Use tables to display the data."],
    show_tool_calls=True,
    markdown=True,
)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
  serve_playground_app("playground:app",reload=True)