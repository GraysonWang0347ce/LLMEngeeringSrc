from langchain_openai import OpenAI

class LLM:
    """
    连接到LLM模型的类
    """
    def __init__(self):
        self.model = OpenAI(model="Qwen2.5-14B",
                            base_url="http://10.58.0.2:8000/v1/",
                            api_key="None",
                            temperature=0,)

    def invoke(self, prompt):
        return self.model.invoke(prompt)

    def get_model(self):
        return self.model