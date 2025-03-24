# Download model

# from transformers import AutoModelForSequenceClassification, AutoTokenizer

# model_name = "SamLowe/roberta-base-go_emotions"
# save_dir = "roberta-base-model"

# # Load model and tokenizer
# model = AutoModelForSequenceClassification.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# # Save model and tokenizer to local directory
# model.save_pretrained(save_dir)
# tokenizer.save_pretrained(save_dir)


# Implement model 

# from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# # Load model and tokenizer from the saved directory
# model_dir = "roberta-base-model"
# model = AutoModelForSequenceClassification.from_pretrained(model_dir)
# tokenizer = AutoTokenizer.from_pretrained(model_dir)

# # Create classifier pipeline
# classifier = pipeline(task="text-classification", model=model, tokenizer=tokenizer, top_k=None)

# # Sample input
# # sentences = ["I am not having a great day"]
# sentences = ["I am not having a great day"]

# # Perform classification
# model_outputs = classifier(sentences)
# print(model_outputs[0])




def mind_feelings(feelings):

    from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

    # Load model and tokenizer from the saved directory
    model_dir = "roberta-base-model"
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)

    # Create classifier pipeline
    classifier = pipeline(task="text-classification", model=model, tokenizer=tokenizer, top_k=None)

    # Sample input
    # sentences = ["I am not having a great day"]
    # sentences = ["I am not having a great day"]
    sentences = feelings

    # Perform classification
    model_outputs = classifier(sentences)
    # print(model_outputs[0])
    return model_outputs[0]
