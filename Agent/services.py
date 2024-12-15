from llmConnect import LLM
from database import Database
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool


class Agent:
    """
    定义了智能体类型
    """
    def __init__(self):
        self.db = Database()
        self.model = LLM()
        self.tools = [
            Tool.from_function(
                func=self.db.add_course,
                name="add_courses",
                description="Add a course",

            ),
            Tool.from_function(
                func=lambda _: self.db.get_selected_courses(),
                name="get_selected_courses",
                description="Get selected courses"
            ),
            Tool.from_function(
                func=lambda attribute: self.db.get_selected_conditional_courses(attribute),
                name="get_selected_conditional_courses",
                description="Get courses selected filtered by attribute, input like 必修 or 选修"
            ),
            Tool.from_function(
                func=lambda attribute: self.db.get_all_conditional_courses(attribute),
                name="get_all_conditional_courses",
                description="Get all courses filtered by attribute, input like 必修 or 选修"
            ),
            Tool.from_function(
                func=lambda name: self.db.remove_course(name),
                name="remove_course",
                description="Remove a course"
            ),
            # Tool.from_function(
            #     func=lambda _: self.db.show_selected_courses(),
            #     name="print_selected_courses",
            #     description="Show all selected courses"
            # ),
            # Tool.from_function(
            #     func=lambda _: self.db.show_all_courses(),
            #     name="print_all_courses",
            #     description="Show all courses"
            # ),
            # Tool.from_function(
            #     func=lambda attribute: self.db.show_selected_conditional_courses(attribute),
            #     name="print_selected_conditional_courses",
            #     description="Show courses selected filtered by attribute"
            # ),
            # Tool.from_function(
            #     func=lambda attribute: self.db.show_all_conditional_courses(attribute),
            #     name="print_all_conditional_courses",
            #     description="Show all courses filtered by attribute"
            # )
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
            stop=["\nObservation:"]  # stop when the model starts a new observation
        )

        self.tool_names = [tool.name for tool in self.tools]

