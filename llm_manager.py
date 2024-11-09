from langchain_google_genai import ChatGoogleGenerativeAI

# API setup
GEMINI_API_KEY = "AIzaSyADTuk6uZ7jI-ZcBL9DuwEUkv7sAJfRSOk"
gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1, api_key=GEMINI_API_KEY)

def get_llm_response_with_context(questions: str, answers: str, user_questions: str):
    prompt_template = f"""You are a Chatbot,
    Answer the question from the provided below context only, delimited by triple backslash \n\n
    Please provide the answer only, without explanation, in a single line.
    
    
Context:\n 
    Questions: {questions}\n
    Answers: {answers}\n


    Question: {user_questions}\n
    Answer:
    """
    result = gemini_llm.invoke(prompt_template)
    return result.content

def get_llm_response_without_context(user_questions: str):
    prompt_template = f"""You are a Chatbot,
    Answer the following User Question based on an Indian restaurant theme:\n\n
    Please give a concise answer without any explanation, in a two line.
    
    User Question: {user_questions}\n
    Answer:
    """
    result = gemini_llm.invoke(prompt_template)
    return result.content  