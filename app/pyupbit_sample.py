import os

import openai
import pyupbit
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()


def get_tickers():
    return pyupbit.get_tickers()


def get_ohlcv(ticker="KRW-BTC", interval="day", count=30):
    return pyupbit.get_ohlcv(ticker, interval, count)


def response_create(model, input_text):
    response = client.responses.create(
        model=model,
        instructions="Talk like a pirate.",
        input=input_text,
    )
    return response.output_text


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


def receive_a_structured_response() -> CalendarEvent:
    """구조화된 응답 수신"""
    response = client.responses.parse(
        model="gpt-5.1",
        # reasoning={"effort": "low"}, # low, medium, high
        instructions="Extract the event information.",
        input="Alice and Bob are going to a science fair on Friday.",
        text_format=CalendarEvent,
    )

    event = response.output_parsed
    if event is None:
        raise ValueError("Failed to parse calendar event from response")
    return event


if __name__ == "__main__":
    # print(get_tickers())
    # print(get_ohlcv())
    # print(response_create("gpt-5.1", "Hello, how are you?"))
    print(receive_a_structured_response().model_dump_json())
