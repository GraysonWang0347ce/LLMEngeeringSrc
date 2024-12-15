# -*- coding: utf-8 -*-
import os

from prompt import Defined_Prompt
from services import Agent
import json


class WorkMod():
    FILE = 0
    CHAT = 1


# FILE为回答questions.json中问题并记录在answer里，CHAT为与用户对话
_MOD_ = WorkMod.CHAT

if __name__ == '__main__':
    print(
        "AI: 你好,我是一个知识问答机器人,我会尝试解答您的任何问题!")
    agent = Agent()
    prompt_t = Defined_Prompt()

    if _MOD_ == WorkMod.FILE:
        questions = json.load(open("questions.json", "r", encoding='utf-8'))
        for question in questions:
            res = agent.agent.invoke(prompt_t.init_prompt().format(user_input=question['question'], tools=agent.tools))
            question['answer'] = res["output"] + agent.get_ref()
            json.dump(questions, open("questions.json", "w", encoding='utf-8'), indent=4, ensure_ascii=False)

        # change question.json's name into questions.json
        os.rename("questions.json", "answers.json")

    else:
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

            print("AI: ", res["output"])
            agent.print_ref()
