import re

print("=== Toxic Comment Classification Demo ===")

# Sample comments for demonstration
comments = [
    "This is a wonderful tutorial, thank you for sharing!",
    "You are completely stupid and your code is useless.",
    "I will destroy everything you built, get lost!"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Rule-based simple classifier demo for mobile
def classify_comment(text):
    cleaned = clean_text(text)
    severe_words = ['destroy', 'kill', 'die', 'ruin']
    toxic_words = ['stupid', 'idiot', 'useless', 'trash']
    
    if any(word in cleaned for word in severe_words):
        return "Severe Toxic (2)"
    elif any(word in cleaned for word in toxic_words):
        return "Toxic (1)"
    else:
        return "Non-Toxic (0)"

print("\nRunning Model Inference on Sample Comments:\n")
for i, c in enumerate(comments, 1):
    prediction = classify_comment(c)
    print(f"Comment {i}: '{c}'")
    print(f"Prediction: --> {prediction}\n")

print("Script executed successfully on mobile!")
