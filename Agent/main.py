# -*- coding: utf-8 -*-
from prompt import Defined_Prompt
from services import Agent

if __name__ == '__main__':
    print(
        "AI: 你好，我是一个选课助手，我可以帮助你进行选课，查询课程，删除课程的任务，或根据您的喜好帮助您推荐课程，请问您要做些什么呢？")
    agent = Agent()
    prompt_t = Defined_Prompt()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye', '退出', '再见']:
            break
        try:
            res = agent.agent.invoke(prompt_t.init_prompt().format(user_input=user_input, tools=agent.tools))
        except Exception as e:
            print("AI: ", "对不起，我不明白您的意思，请您再说一遍")
            print("Error: ", e)
            continue

        print("AI: ",res)
