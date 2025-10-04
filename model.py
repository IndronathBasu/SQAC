from transformers import MarianMTModel, MarianTokenizer

# Load English → Hindi model
en_to_hi_model_name = "Helsinki-NLP/opus-mt-en-hi"
tokenizer_en_hi = MarianTokenizer.from_pretrained(en_to_hi_model_name)
model_en_hi = MarianMTModel.from_pretrained(en_to_hi_model_name)

# Load Hindi → English model
hi_to_en_model_name = "Helsinki-NLP/opus-mt-hi-en"
tokenizer_hi_en = MarianTokenizer.from_pretrained(hi_to_en_model_name)
model_hi_en = MarianMTModel.from_pretrained(hi_to_en_model_name)

def translate(text, direction):
    """sssssssssssssss
    Translates text based on the selected direction.
    direction: 'en-hi' or 'hi-en'
    """
    if direction == "en-hi":
        tokenizer, model = tokenizer_en_hi, model_en_hi
    elif direction == "hi-en":
        tokenizer, model = tokenizer_hi_en, model_hi_en
    else:
        raise ValueError("Invalid translation direction. Use 'en-hi' or 'hi-en'.")

    # Tokenize and translate
    inputs = tokenizer([text], return_tensors="pt", padding=True)
    outputs = model.generate(**inputs)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translated_text
