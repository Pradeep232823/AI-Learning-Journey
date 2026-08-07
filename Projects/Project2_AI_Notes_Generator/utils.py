def character_count(text):
    return len(text)

def word_count(text):
    lines = text.split("\n")
    words = []
    
    for line in lines:
        words.extend(line.split())
    return len(words)

def line_count(text):
    lines = text.split("\n")
    return len(lines)

def display_statistics(text):
    print(f"""
======== Statistics ========

Characters : {character_count(text)}
Words      : {word_count(text)}
Lines      : {line_count(text)}
""")