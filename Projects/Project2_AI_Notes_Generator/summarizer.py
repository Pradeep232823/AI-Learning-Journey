import helpers
from itertools import islice
stop_words = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "is", 
    "am", "been", "being", "can", "could", "should", "would", "has", "had", "hadn't"
}

def clean_text(text):
    if not text:
        return ""
    lines = text.split("\n")

    clean_lines = []
    for line in lines:
        words = line.split()
        if not words:
            continue
        clean_lines.append(" ".join(words))

    text = "\n".join(clean_lines)
    return text

def split_sentences(text):
    
    if not text:
        return ""
    clean_sentence = clean_text(text)

    split_res = []
    start = 0

    for i in range(len(clean_sentence)):
        if clean_sentence[i] in "!.?":
            
            split_res.append(clean_sentence[start:i+1].strip())
            start = i + 1

    if start < len(clean_sentence):
        split_res.append(clean_sentence[start:].strip())

    return split_res

def word_frequency(text):

    clean_sent = helpers.remove_punctuation(clean_text(text).lower())

    word_freq = {}

    for word in clean_sent.split():
        if word in stop_words:
            continue
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def sentence_scoring(text):
    original_sentences = split_sentences(text)
    sentences = original_sentences.copy()

    for i in range(len(sentences)):
        sentences[i] = helpers.remove_punctuation(sentences[i].lower())

    freq = word_frequency(text)

    sentences_freq = {}

    for i in range(len(sentences)):
        words = sentences[i].split()
        sentence_total_freq = 0
        for word in words:
            if word not in stop_words:
                sentence_total_freq += freq.get(word, 0)
        sentences_freq[original_sentences[i]] = sentence_total_freq
    return sentences_freq

def generate_summary(text):
    sentenses_score = sentence_scoring(text)

    sorted_sentence_score = dict(sorted(sentenses_score.items(), key=lambda item: item[1], reverse = True))

    n = max(1, int(0.3 * len(sentenses_score)))

    topN_score = dict(islice(sorted_sentence_score.items(), 0, n))

    topN_score_original_order = {}

    for sentence in sentenses_score:
        if sentence in topN_score:
            topN_score_original_order[sentence] = sentenses_score[sentence]

    topN_sentences_text = "\n\n".join(topN_score_original_order.keys())
    return topN_sentences_text