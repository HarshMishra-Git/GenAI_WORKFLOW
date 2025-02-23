# GenAI Workflow System

![GenAI Workflow System](https://user-images.githubusercontent.com/HarshMishra-Git/GenAI_WORKFLOW/main/assets/genai_workflow_banner.png)

## Introduction

The **GenAI Workflow System** is an advanced document processing and question-answering platform that leverages Retrieval-Augmented Generation (RAG) and AI capabilities to help users extract insights from uploaded documents.

## Live Demo

Check out the live demo of the GenAI Workflow System [here](https://genaiworkflow.streamlit.app/).

## Features

- **📄 Document Upload**: Easily upload and process multiple documents (text or PDF files).
- **🔍 Smart Search**: Uses RAG to find relevant information from your documents.
- **🤖 AI-Powered Answers**: Get intelligent responses based on your document context.
- **📊 Visual Analytics**: View confidence scores and result timelines.
- **📤 Export Capability**: Export results in various formats (CSV, JSON, Excel).

## How to Use

1. **Upload Documents**: Start by uploading your text or PDF files.
2. **Configure Settings**: Adjust RAG and AI settings in the sidebar.
3. **Ask Questions**: Enter your queries in the Query Interface.
4. **Analyze Results**: View answers, context, and visualizations.
5. **Export Data**: Export your results using the sidebar option.

## Installation

To run the GenAI Workflow System locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/HarshMishra-Git/GenAI_WORKFLOW.git
    cd GenAI_WORKFLOW
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```sh
    streamlit run src/main.py
    ```

## Project Structure

- **requirements.txt**: Lists all the dependencies required for the project.
- **src/components/**: Contains UI components and utility functions.
    - `__init__.py`
    - `document_upload.py`
    - `query_interface.py`
    - `sidebar.py`
    - `visualization.py`
- **src/main.py**: The main module that orchestrates the entire application.

## Technologies Used

- **Python**: The primary programming language.
- **Streamlit**: For creating the web application interface.
- **FAISS**: For efficient similarity search and clustering of dense vectors.
- **OpenAI**: For interacting with OpenAI models.
- **Plotly**: For creating interactive visualizations.
- **Pandas**: For data manipulation and analysis.
- **PyTorch**: For deep learning models.
- **Hugging Face Transformers**: For state-of-the-art natural language processing.

## Contribution

We welcome contributions to the GenAI Workflow System! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, please contact Harsh Mishra at [contact.me](mailto:harsmishra1132@gmail.com).
