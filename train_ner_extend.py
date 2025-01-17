import spacy
from spacy.training.example import Example
from train_data import TRAIN_DATA  # Import your custom training data

# Load the pre-trained SpaCy model
nlp = spacy.load("en_core_web_sm")

# Get the Named Entity Recognizer (NER) component
ner = nlp.get_pipe("ner")

# Add custom labels to the NER component
labels = ["TOOL", "TECHNOLOGY", "LANGUAGE", "PROGRAMMING_LANGUAGE"]
for label in labels:
    if label not in ner.labels:
        ner.add_label(label)

# Disable other components in the pipeline during training
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

# Fine-tune the model
with nlp.disable_pipes(*unaffected_pipes):  # Train only the NER component
    optimizer = nlp.resume_training()
    for epoch in range(20):  # Number of iterations
        for text, annotations in TRAIN_DATA:
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.35, sgd=optimizer)

# Save the fine-tuned model
output_dir = "en_core_web_sm_extended"
nlp.to_disk(output_dir)
print(f"Fine-tuned model saved to '{output_dir}'")
