
import google.generativeai as genai

class SynthesizerAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def synthesize(self, context, query):
        prompt = f"""Answer using context only.
Context:
{context}

Question:
{query}
"""
        return self.model.generate_content(prompt).text
