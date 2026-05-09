# ---------------------------------------------------------
# The Data Ghost Protocol: Project #3
# Goal: Quantify "Voice" complexity for Ghostwriting clients.
# ---------------------------------------------------------

# The text we want to analyze (this could be a blog post or an email)
text = """Ghostwriting is the art of invisible architecture. 
We build the structure so the client can live in the house."""

# 1. Split the text into a list of words
words = text.split()
word_count = len(words)

# 2. Calculate the total number of characters (excluding spaces)
# We loop through each word and add its length to the total
char_count = sum(len(word) for word in words)

# 3. Calculate Average Word Length (Complexity Score)
# We use a float here to get a precise decimal
avg_word_length = char_count / word_count

# 4. Output the Data Breakdown
print("--- Data Ghost: Voice Analysis Report ---")
print(f"Total Word Count: {word_count}")
print(f"Complexity Score: {avg_word_length:.2f} chars/word")

# 5. Logical Analysis: Identify the "Tone" based on complexity
# Professional writing usually averages > 5 characters per word.
if avg_word_length > 5:
    print("Detected Tone: Professional / Corporate / Academic")
else:
    print("Detected Tone: Conversational / Direct / Punchy")

print("--- Analysis Complete ---")
<<<<<<< HEAD

=======
>>>>>>> 4d1b962 (Migration complete: Environment cleaned and files secured)
