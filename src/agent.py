from langchain.agents import initialize_agent, AgentType
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from .model import get_model


def build_agent(retriever):
    model = get_model()

    @tool
    def search_mortgage_doc(query: str) -> str:
        docs = retriever.invoke(query)
        return "\n\n".join(d.page_content for d in docs)

    @tool
    def calculate(expression: str) -> str:
        try:
            return str(eval(expression, {"__builtins__": {}}))
        except Exception as e:
            return f"Error: {e}"

    @tool
    def web_search(query: str) -> str:
        return DuckDuckGoSearchRun().run(query)

    tools = [search_mortgage_doc, calculate, web_search]

    agent = initialize_agent(
        tools=tools,
        llm=model,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
