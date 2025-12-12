from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chat_with_ai():
    chat_history_ids = None
    print("Chatbot is ready! Type 'exit' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

        output = model.generate(
            new_input_ids, 
            max_length=100,
            temperature=0.3,
            top_p=0.7,
            num_beams=5,
            early_stopping=True,
            pad_token_id=tokenizer.eos_token_id
        )

        response = tokenizer.decode(output[:, new_input_ids.shape[-1]:][0], skip_special_tokens=True)
        print(f"AI: {response}")

chat_with_ai()
