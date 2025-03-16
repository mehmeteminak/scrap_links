from langchain.schema import HumanMessage

class UrlSelector:
    def __init__(self, model):
        self.model = model


    def set_model(self, model):
        self.model = model

        # --- Use LangChain LLM to select the most appropriate URL ---
    def select_best_url(self,urls, search_text):

        prompt = f"""
        You are an AI assistant that selects the most relevant URL based on the search text '{search_text}'.
        Given the following URLs, return ONLY the most appropriate one. If none are relevant, return nothing.

        URLs:
        {urls}

        IMPORTANT: Respond with only the chosen URL, nothing else.
        """

        response = self.model.invoke([HumanMessage(content=prompt)])
        return response
