import sys
import openai

model = "gpt-3.5-turbo"
max_tokens = 300
temperature = 0.7
top_p = 1
n = 1
stop_sequence = ""
presence_penalty = 0.0
frequency_penalty = 0.0

def execute_prompt_chat_completion_api(messages) -> str:
    result = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        n=n,
        stop=stop_sequence,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty
    )

    return result["choices"][0]["message"]["content"]

def execute_user_input(user_input: str) -> str:
    if user_input is None:
        raise Exception("User input is None")
        
    priming_chat_message = {"role": "system", "content": "You are a helpful assistant."}
    user_chat_message = {"role": "user", "content": user_input}
    messages = [priming_chat_message, user_chat_message]
    
    result = execute_prompt_chat_completion_api(messages)

    return result

if __name__ == "__main__":
    openai.api_key = ""

    if len(sys.argv) > 1:
        user_input : str = sys.argv[1]
        print(execute_user_input(user_input))
    else:
        print(execute_user_input("Where is New York?"))
