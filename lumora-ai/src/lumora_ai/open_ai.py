import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)


# TEST PROMPT -> TEST RESPONSE
def test_prompt_test_response(openai_client: OpenAI):
    response = openai_client.responses.create(
        model="gpt-5",
        input="Write a short 2 liner Joke."
    )

    return response.output_text


print(test_prompt_test_response(client))
