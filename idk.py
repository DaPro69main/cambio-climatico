from smth import transfer
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from collections import Counter

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# --- W.I.P past this point ---
article_text = transfer()
def summarize_text(text, num_sentences=10):
    sentences = sent_tokenize(text)  # Tokenize into sentences
    words = word_tokenize(text.lower())  # Tokenize into words (lowercased)
    
    # Compute word frequencies (excluding common stopwords)
    word_freq = Counter(words)

    # Score sentences based on word importance
    sentence_scores = {sent: sum(word_freq[word] for word in word_tokenize(sent.lower()) if word in word_freq) for sent in sentences}

    # Select top-ranked sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(summary_sentences)

# Generate summary
if article_text:
    summary = summarize_text(article_text)
    print(summary)
else:
    print("Failed to extract article text.")


def transfer2():
    summary2 = summarize_text(article_text)
    return summary2
