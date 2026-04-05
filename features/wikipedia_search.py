import wikipedia

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        return f"According to Wikipedia: {results}"
    except Exception as e:
        return "I couldn't find anything on Wikipedia for that."
