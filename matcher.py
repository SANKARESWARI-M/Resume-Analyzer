import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')  

def extract_keywords(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())

    keywords = [
        word for word in words
        if word.isalnum() and word not in stop_words
    ]

    return set(keywords)


def match_resume(resume_text, job_text):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    matched = resume_keywords.intersection(job_keywords)
    missing = job_keywords.difference(resume_keywords)

    score = (len(matched) / len(job_keywords)) * 100 if job_keywords else 0

    return score, matched, missing