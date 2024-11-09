
# South Indian Food QA System 🍛

### Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Dataset](#dataset)
4. [Technologies Used](#technologies-used)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Testing](#testing)
8. [Future Enhancements](#future-enhancements)
9. [Contributing](#contributing)


## Introduction
This project is an AI-powered Question-Answering (QA) system that focuses on South Indian cuisine. Using a pre-defined dataset of questions and answers related to South Indian food, this system utilizes free Large Language Models (LLMs) along with sentence embeddings to accurately respond to user queries. This is especially useful as users may not always ask questions in the exact format found in the dataset.


## Project Overview
The system is designed to:
- Accept user queries related to South Indian food.
- Embed both the dataset questions and user input using sentence transformers.
- Use a similarity search to find the most relevant answer.
- Utilize a free LLM for generating contextually accurate responses.

### Key Features
- **Pre-trained Sentence Embeddings**: Uses `sentence-transformers` for vectorization.
- **Free LLM Integration**: Supports free LLM models (like GPT-2) for response generation.
- **Web Interface**: Built with Flask for a simple and user-friendly web interface.
- **Extensible Architecture**: Modular design to easily integrate other LLMs or additional data.


## Dataset
The dataset (`south_indian_food.csv`) consists of questions and answers specific to South Indian cuisine. The CSV file is structured as follows:
- **Question**: The query related to South Indian food.
- **Answer**: The corresponding answer to the question.

Ensure your CSV file is formatted correctly before using it with the system.


## Technologies Used
- **Python** 🐍
- **Flask** (for web server)
- **Sentence Transformers** (for text embeddings)
- **OpenAI API** (for LLM capabilities)
- **scikit-learn** (for similarity search)
- **Pandas** (for data handling)
- **Hugging Face Transformers** (for LLM support)

### Python Libraries
Here's a list of the Python libraries used in this project (as specified in `requirements.txt`):
```
Flask==2.3.2
sentence-transformers==2.2.2
openai==0.27.0
scikit-learn==1.3.0
numpy==1.24.3
pandas==2.0.3
transformers==4.30.2
huggingface_hub==0.16.4
```


## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- An OpenAI API key (if using OpenAI's GPT models)
- Git (for version control)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/south-indian-food-qa.git
cd south-indian-food-qa
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory and add your GEMINI API key:
```
GEMINI_API_KEY = "YOUR_API_KEY"
```

### Step 5: Prepare the Dataset
Ensure your dataset (`south_indian_food.csv`) is in the correct format and located in the project directory.


## Usage

### Running the Application
1. **Start the Flask Server**:
   ```bash
   python app.py
   ```
2. **Access the Web Interface**:
   - Open your browser and go to [http://localhost:5000](http://localhost:5000).

### Example Query
- Input: *"What is a traditional South Indian breakfast?"*
- Output: *"Idli, Dosa, and Vada are popular South Indian breakfast items."*


## Testing

You can run tests to ensure the functionality of the LLM manager using the provided test file:

```bash
python -m unittest test_llm_manager.py
```

Ensure all test cases pass for a stable deployment.

## Future Enhancements
- **Voice Input Support**: Enable users to ask questions using voice commands.
- **Additional Datasets**: Expand the system to include other types of Indian cuisine.
- **Advanced LLMs**: Integrate with newer models like LLaMA 2 or Falcon for improved accuracy.
- **Deployment on Cloud**: Deploy the system on cloud platforms like AWS or Google Cloud.


## Contributing
We welcome contributions! If you have any ideas or improvements, feel free to fork the project and submit a pull request.

### How to Contribute
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Open a pull request.


