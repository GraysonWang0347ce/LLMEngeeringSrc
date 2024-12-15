from llmConnect import LLM
from vectordatabase import VectorDatabase
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain.retrievers import MultiQueryRetriever


class Agent:
    """
    定义了智能体类型
    """

    def __init__(self):
        self.db = VectorDatabase()
        self.model = LLM()
        self.res_list = []
        self.tools = [
            Tool.from_function(
                func=self.get_vdb_contents,
                name="get_vdb_contents",
                description="根据用户输入，返回数据库中的内容",
            )
        ]
        self.memory = ConversationBufferMemory(
            memory_key='course_selection',
            memory_size=10,
        )
        self.agent = initialize_agent(
            llm=self.model.get_model(),
            # memory=self.memory,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            # verbose=True,
            tools=self.tools,
            handle_errors=True,
            handle_parsing_errors=True,
        )

        self.tool_names = [tool.name for tool in self.tools]

        # 检索器，其会自动生成几个类似的query一并检索
        self.retriever_from_llm = MultiQueryRetriever.from_llm(
            llm=self.model.get_model(),
            retriever=self.db.db.as_retriever()
        )

    def get_vdb_contents(self, query):
        res = self.retriever_from_llm.invoke(query)
        res_list = [{"content": r.page_content,
                     "access_id": r.metadata['access_id'],
                     "title": r.metadata['title'],
                     "authors": r.metadata['authors']}
                    for r in res]
        self.res_list = res_list
        return res

    def print_ref(self):
        '''
        将所有的参考文献print出来
        '''
        if self.res_list == []:
            return
        print("Reference: ")
        for i in self.res_list:
            print('\'', i["title"], '\'', " \n\tACCESS_ID: ", i["access_id"], ' AUTHORS: ', i["authors"])
        self.res_list = []

    def get_ref(self) -> str:
        '''
        将所有的参考文献以str返回
        '''
        if self.res_list == []:
            return ""
        ref = ""
        for i in self.res_list:
            ref += i["title"] + " \n\tACCESS_ID: " + i["access_id"] + ' AUTHORS: ' + i["authors"] + "\n"
        self.res_list = []
        return ref


if __name__ == '__main__':
    a = Agent()
    print(a.get_vdb_contents("什么是大语言模型？"))
