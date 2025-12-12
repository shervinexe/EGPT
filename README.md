<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>E GPT</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        code {
            background-color: #e8e8e8;
            padding: 2px 5px;
            border-radius: 3px;
        }
        pre {
            background-color: #e8e8e8;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .section {
            margin-bottom: 30px;
        }
    </style>
</head>
<body>

    <h1>E GPT</h1>
    <p>
        <strong>E GPT</strong> is a personal, fully self-made chatbot that runs locally on your computer. 
        It allows interactive conversation directly in the terminal and maintains context across multiple turns. 
        Every part of E GPT—from conversation handling to response generation—was created independently, 
        making it a unique AI project built entirely from scratch.
    </p>

    <div class="section">
        <h2>Features</h2>
        <ul>
            <li>Interactive terminal-based chat interface</li>
            <li>Maintains conversation context for multiple turns</li>
            <li>Fully developed and implemented independently</li>
            <li>Lightweight and easy to run on most computers</li>
            <li>No external service, API, or registration required</li>
        </ul>
    </div>

    <div class="section">
        <h2>Requirements</h2>
        <ul>
            <li>Python 3.8 or higher</li>
        </ul>
        <p>Install required Python packages:</p>
        <pre><code>pip install torch transformers</code></pre>
    </div>

    <div class="section">
        <h2>Usage</h2>
        <p>Run the chatbot script in your terminal:</p>
        <pre><code>python main.py</code></pre>

        <p>Example interaction:</p>
        <pre><code>
You: Hello!
AI: Hi! How are you today?
You: Tell me something interesting.
AI: Did you know that honey never spoils? Ancient honey is still edible!
        </code></pre>

        <p>Type <code>exit</code> to end the chat.</p>
    </div>

    <div class="section">
        <h2>How it Works</h2>
        <p>
            E GPT encodes user input, generates a response based on the conversation history, 
            and outputs it to the terminal. It maintains conversation context to provide coherent 
            and relevant responses. Configurable parameters allow control over response length, 
            creativity, and selection strategy to make interactions engaging.
        </p>
    </div>

    <div class="section">
        <h2>Code Example</h2>
        <pre><code>import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Initialize model and tokenizer
model_name = "your-local-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chat_with_ai():
    print("E GPT is ready! Type 'exit' to stop.")
    history = ""

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        prompt = f"{history}\nUser: {user_input}\nAssistant:"
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        output = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            top_p=0.9
        )

        response = tokenizer.decode(
            output[0][inputs["input_ids"].shape[-1]:],
            skip_special_tokens=True
        )

        print("AI:", response)
        history += f"\nUser: {user_input}\nAssistant: {response}"

chat_with_ai()</code></pre>
    </div>

    <div class="section">
        <h2>License</h2>
        <p>MIT License. You are free to use and modify this project.</p>
    </div>

</body>
</html>

