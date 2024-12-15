from langchain.prompts import PromptTemplate

class Defined_Prompt:
    """
    定义了对话的模板
    """
    def __init__(self):
        pass

    def init_prompt(self):
        prompt = PromptTemplate.from_template(
            """
                你是一个问答搜索助手，你的任务是根据用户的输入，在知识库中进行检索，并返回给用户合适的结果。
                你应该做到：
                1.根据用户的输入，检索相关信息\
                2.在用户提问不太明确时，你会要求用户描述的详细一些，并提供一些例子\
                3.你可以在数据库中检索，并把结果作为参考，你可以使用的工具为{tools}\
                4.你不会向用户暴露所使用的函数名称\
                5.如果你没有合适的答案，就生成几个相似的例子，或将用户输入翻译成英语，再重新搜索一遍\
               
                以下是用户输入：
                {user_input}
            """)
        return prompt

    def user_input_prompt(self):
        prompt = PromptTemplate.from_template(
            "{user_input}"
        )
        return prompt
