from langchain_anthropic import ChatAnthropic

from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl

from _utils import read_text_dir


@cl.on_chat_start
async def on_chat_start():
    # model = ChatOpenAI(streaming=True)
    model = ChatAnthropic(model='claude-3-5-sonnet-20240620', stream=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "\n\n".join(read_text_dir("prompt").values()),
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)



@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Quick Start",
            message="How do I use you?",
            icon="/public/lightbulb.svg",
            ),

        cl.Starter(
            label="Ex: Mild Fatty Liver",
            message="Moderate fatty liver, CBD = 5 mm",
            icon="/public/pen.svg",
            ),
        
        cl.Starter(
            label="Ex: Moderate Fatty Liver + GS",
            message="- Severe fatty liver\n- A 2-cm GS",
            icon="/public/pen.svg",
            ),
        cl.Starter(
            label="Ex: Severe Fatty Liver + GS + Renal cyst",
            message="- Severe fatty liver, CBD = 6 mm\n- A few gallstone, size up to 1 cm\n- A 2-cm simple cyst at right kidney",
            icon="/public/pen.svg",
            ),
        ]
# ...


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
