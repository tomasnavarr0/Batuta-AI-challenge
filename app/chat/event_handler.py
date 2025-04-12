from typing import Any
import chainlit as cl
from openai import AsyncAssistantEventHandler
from literalai.helper import utc_now
from app.config import Settings


class EventHandler(AsyncAssistantEventHandler):
    def __init__(self, assistant_name: str) -> None:
        super().__init__()
        self.current_message: cl.Message = None
        self.current_step: cl.Step = None
        self.current_tool_call = None
        self.assistant_name = assistant_name

    async def on_text_created(self, *_: Any) -> None:
        self.current_message = await cl.Message(author=self.assistant_name, content="").send()

    async def on_text_delta(self, delta, *_: Any) -> None:
        await self.current_message.stream_token(delta.value)

    async def on_text_done(self, *_: Any) -> None:
        await self.current_message.update()
