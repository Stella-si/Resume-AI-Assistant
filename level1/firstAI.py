from openai import OpenAI

client = OpenAI(
    api_key="sk-1bcdaba142b34275856beba7020aa9c8",
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role":"user","content":"推荐一部纯爱番剧"}]
)
print(response.choices[0].message.content)