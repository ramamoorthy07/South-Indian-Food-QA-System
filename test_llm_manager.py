from llm_manager import get_llm_response_with_context
from llm_manager import get_llm_response_without_context

def test_from_db():
    questions = "What is a famous rice-based dish from Tamil Nadu known for its tangy flavor?"
    answers = "Lentils, tamarind, and vegetables"
    user_questions  = "What is a famous rice-based dish from Tamil Nadu?"

    result = get_llm_response_with_context(questions = questions,
                                           answers = answers,                             
                                           user_questions = user_questions)
    print(result)

def test_general_questions():
    user_questions  = "What is a famous rice-based dish from Tamil Nadu?"

    result = get_llm_response_without_context(user_questions = user_questions)
    print(result)

if __name__ == "__main__":
#    test_general_questions()
    test_from_db()