from openai import ChatCompletion

from llegos.asyncio import AsyncAgent
from llegos.ephemeral import EphemeralAgent, EphemeralCognition, EphemeralMessage, Field
from llegos.messages import Ack


class ChatMessage(EphemeralMessage):
    body: str


class MockCognition(EphemeralCognition):
    language: ChatCompletion = Field(default_factory=ChatCompletion)
    working_memory: list[EphemeralMessage] = Field(default_factory=list)
    short_term_memory: list[EphemeralMessage] = Field(default_factory=list)
    long_term_memory: list[EphemeralMessage] = Field(default_factory=list)


class MockAgent(EphemeralAgent):
    cognition: MockCognition = Field(default_factory=MockCognition)
    receivable_messages: set[type[EphemeralMessage]] = {Ack}

    def ack(self, message: Ack):
        return Ack.reply_to(message)


class MockAsyncAgent(AsyncAgent):
    cognition: MockCognition = Field(default_factory=MockCognition)
    receivable_messages: set[type[EphemeralMessage]] = {Ack}

    async def ack(self, message: Ack):
        return Ack.reply_to(message)
