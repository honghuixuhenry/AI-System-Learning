from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer
)


model_name = "your-model"


tokenizer = (
    AutoTokenizer.from_pretrained(
        model_name
    )
)


model = (
    AutoModelForCausalLM
    .from_pretrained(
        model_name
    )
)


prompt = "Explain KV cache."


inputs = tokenizer(
    prompt,
    return_tensors="pt"
)


outputs = model.generate(
    **inputs,
    max_new_tokens=100
)


text = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)


print(text)