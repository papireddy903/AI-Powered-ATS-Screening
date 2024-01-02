#find ats score 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.feature_extraction import _stop_words 
from convert import ExtractPDFText

def calculateATSscore(pdf_path, job_description):
    resume_data = ExtractPDFText("My Resume.pdf")
    job_description = "Data scientist role. need fresher . skills python, SQL"
    stopwords = list(_stop_words.ENGLISH_STOP_WORDS) 
    vectorizer = TfidfVectorizer(stop_words=stopwords) 
    vectors = vectorizer.fit_transform([job_description, resume_data])
    similarity_value = cosine_similarity(vectors)
    print(similarity_value)
    # return similarity_value[0,1]
    return similarity_value[0,1]



