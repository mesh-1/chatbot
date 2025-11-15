from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

chat_history_ids = None

print("Chatbot Ready!")

for step in range(20):
    user_input = input("You: ")

    new_input_ids = tokenizer.encode(
        user_input + tokenizer.eos_token, return_tensors='pt'
    )

    if chat_history_ids is not None:
        input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
    else:
        input_ids = new_input_ids

    chat_history_ids = model.generate(
        input_ids,
        max_length=300,
        pad_token_id=tokenizer.eos_token_id,
        attention_mask=torch.ones_like(input_ids)
    )

    reply = tokenizer.decode(
        chat_history_ids[:, input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    print("Bot:", reply)
