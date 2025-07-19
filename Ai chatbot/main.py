import openai
from openai import OpenAI

key ="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"

# messages = []

# client = OpenAI(
#     api_key=key, # this is the default that can be omitted
# )

# def completion(message):
#     global messages
#     messages.append(
#         {
#             "role": "assistant",
#             #"content": message
#             "content": chat_completion.choices[0].message.content
#         }
#     )
#     chat_completion = client.chat.completions.create(messages=messages,
#                         model="gpt-4o"
#                         )
#     #print(chat_completion)

# if __name__ == "__main__":
#     print(f"jarvis: Hi i am jarvis, how may i help you\n")
#     while True:
#         user_question = input()
#         print(f"user:{user_question}")
#         completion(user_question)

    #user_question = input("Hi i am jarvis,how may i help you")
    #completion(user_question)


messages = []

client = OpenAI(api_key=key)

def completion(user_input):
    global messages

    # Append user's message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Create completion
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    # Get assistant response
    assistant_reply = chat_completion.choices[0].message.content

    # Append assistant's reply
    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    print(f"jarvis: {assistant_reply}\n")

if __name__ == "__main__":
    print("jarvis: Hi I am Jarvis, how may I help you?\n")
    while True:
        user_question = input("you: ")
        completion(user_question)
