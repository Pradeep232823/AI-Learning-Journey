def clean_text(text):
    if not text:
        return ""
    lines = text.split("\n")

    clean_lines = []
    for line in lines:
        words = line.split()
        if not words:
            continue
        clean_lines.append(" ".join(word for word in words))

    text = "\n".join(line for line in clean_lines)
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