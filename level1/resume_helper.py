from openai import OpenAI
import os

client= OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

#关键：用列表保存历史对话

# 初始化对话
messages=[
    {"role":"system","content":"""
     你是一个专业的简历优化顾问。
    当用户粘贴简历内容时，你需要：
    1. 指出3个最大的问题
    2. 给出具体的改进建议
    3. 提供优化后的表达方式
    用中文回答，语气专业但友好。
    """}
]

file_path="个人简历-司缘锐 -QA.txt"

print(f"简历优化助手已上线（读取文件：{file_path}）---")
while True:
    command=input("\n>>> 输入 'go' 开始分析文件，输入 'quit' 退出:").strip().lower()
    if command=="quit":
        break
    if command=="go":
        #检查文件是否存在
        if not os.path.exists(file_path):
            print(f"文件不存在：{file_path}")
            continue
        #读取文件内容
        with open(file_path,"r",encoding="utf-8") as f:
            user_input=f.read()

        if user_input.strip():
            print("正在分析简历...")

            #把文件内容塞进对话历史
            messages.append({"role":"user","content":f"这是我的简历内容：\n{user_input}"})

            #调用AI
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages
            )

            reply=response.choices[0].message.content
            print(f"\n[AI 优化建议]:\n\n{reply}")

            # 存入助手回复，方便下次追问
            messages.append({"role": "assistant", "content": reply})

            print("\n--- 分析完毕！你可以修改 resume.txt 后再次输入 'go' ---")

        else:
            print("简历内容为空")
    else:
        print("无效的命令")


#--------------------------------------------------------------------------
#从剪切板读取简历
# from openai import OpenAI
# import os
# import pyperclip
#
# client= OpenAI(
#     api_key=os.environ.get("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com"
# )
#
# messages=[
#     {"role":"system","content":"""
#      你是一个专业的简历优化顾问。
#     当用户粘贴简历内容时，你需要：
#     1. 指出3个最大的问题
#     2. 给出具体的改进建议
#     3. 提供优化后的表达方式
#     用中文回答，语气专业但友好。
#     """}
# ]
#
# while True:
#     #停下来等命令
#     command = input("请先复制您的简历，然后按回车键开始优化,输入quit退出")
#     if command.lower()=="quit": #去空格 变小写 判断是不是quit
#         break
#     user_input = pyperclip.paste() #从剪切板读取简历
#     if not user_input.strip():
#         print("剪贴板为空，请先复制简历")
#         continue
#     print("正在分析简历...")
#     messages.append({"role": "user", "content": user_input})
#
#     response = client.chat.completions.create(
#         model="deepseek-chat",
#         messages=messages
#     )
#
#     reply = response.choices[0].message.content
#     messages.append({"role": "assistant", "content": reply})
#     print(f"AI:{reply}")

