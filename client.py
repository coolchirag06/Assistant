from openai import OpenAI

client = OpenAI(
    api_key="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",
)


completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "assistant", "content": "you are a virtual assistant that is tasked to answer the queries of user"}
    ]
)
print(completion.choices[0].message.content)