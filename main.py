import os
from dotenv import load_dotenv
from agents import Runner, Agent, AsyncOpenAI, OpenAIChatCompletionsModel,RunResult,set_tracing_disabled

load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
base_url=os.getenv("base_url")
gemini_client=AsyncOpenAI(api_key=GEMINI_API_KEY,base_url=base_url)

shopping_agent=Agent(
    name="shopping_agent",
    instructions="You assist user to finding products and making purchase decisions.",
     model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client),
     handoff_description="A shoppping agent to help user in shopping"
)
support_agent=Agent(
    name="support_agent",
    instructions="You help use with post-purchase and returns.",
     model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client),
     handoff_description="a support agent to help user in post-purchse queries."
)

triage_agent=Agent(
    name="triage_agent",
    instructions=(
        "you are a triage agent,you delagate task to appropriate agent"
        "when user asked for shopping related query,you always use given tools"
        "you never reply on our own, ALways use given tool to reply user"
    
    ),
    model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client),
    tools=[
        shopping_agent.as_tool(
            tool_name="transfer_to_shopping-agent",
            tool_description="you assist user to finding products and making purchase decisions.always add this 😍 emojisi your reply, start with this 😍 emoji",
        ),
        support_agent.as_tool(
            tool_name="transfer_to_support-agent",
            tool_description="you help user with post-purchase support and returns.always add this ✔ emojisi your reply, start with this ✔ emoji",
        )
    ]
)
result: RunResult =Runner.run_sync(starting_agent=triage_agent, input="I want to purchase clothing and want to return a purchsed cap")
print(result.final_output)