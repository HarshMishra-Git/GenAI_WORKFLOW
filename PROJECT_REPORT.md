# GenAI Workflow System Project Report

## Table of Contents

1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Why This Project](#why-this-project)
4. [How This Project Works](#how-this-project-works)
5. [Detailed Explanation](#detailed-explanation)
   - [requirements.txt](#requirementstxt)
   - [src/components/\_\_init\_\_.py](#srccomponents__init__py)
   - [src/components/document_upload.py](#srccomponentsdocument_uploadpy)
   - [src/components/query_interface.py](#srccomponentsquery_interfacepy)
   - [src/components/sidebar.py](#srccomponentssidebarpy)
   - [src/components/visualization.py](#srccomponentsvisualizationpy)
   - [src/main.py](#srcmainpy)
6. [Pipelining](#pipelining)
7. [Conclusion](#conclusion)

## Introduction

The **GenAI Workflow System** is an advanced document processing and question-answering platform that leverages Retrieval-Augmented Generation (RAG) and AI capabilities to help users extract insights from uploaded documents. This report will delve into the purpose, functionality, and detailed implementation of the project.

## Project Overview

The **GenAI Workflow System** is designed to allow users to upload documents, process them, ask questions, and receive intelligent answers based on the document context. It also provides visualization tools to help users better understand the results and export capabilities for further analysis.

## Why This Project

In today's data-driven world, the ability to quickly and accurately extract information from large volumes of documents is crucial. Traditional search methods are often insufficient for complex queries that require understanding the context. The **GenAI Workflow System** addresses this challenge by integrating advanced AI techniques to provide meaningful and context-aware answers.

## How This Project Works

The system works in the following steps:
1. **Upload Documents**: Users upload text or PDF files.
2. **Document Processing**: The system processes the documents and stores them in a vector store.
3. **Query Interface**: Users enter their queries, which are processed using AI to retrieve relevant documents and generate answers.
4. **Visualization**: The system provides visual representations of the results, including confidence scores and timelines.
5. **Export**: Users can export the results in various formats for further analysis.

## Detailed Explanation

### requirements.txt

The `requirements.txt` file lists all the dependencies required for the project. These dependencies include libraries for natural language processing, data handling, AI model interaction, and visualization. The major dependencies are:

- **sentence-transformers**: Used for embedding sentences for semantic search.
- **streamlit**: A web application framework used to create the user interface.
- **faiss-cpu**: A library for efficient similarity search and clustering of dense vectors.
- **openai**: OpenAI's Python client library for interacting with OpenAI models.
- **plotly**: A library for creating interactive visualizations.
- **pandas**: A data manipulation and analysis library.
- **langchain**: Libraries for building language models and integrating with other AI tools.
- **PyPDF2**: A library for reading PDF files.
- **tiktoken**: A library for tokenizing text.
- **transformers**: Hugging Face's library for state-of-the-art natural language processing.
- **torch**: PyTorch, a deep learning framework.

### src/components/\_\_init\_\_.py

The `__init__.py` file initializes the `components` package, making the modules within it accessible when the package is imported. This package includes various UI components required for the application such as document upload, query interface, sidebar, and visualization components.

### src/components/document_upload.py

This module handles the document upload functionality. It provides a user interface for uploading text or PDF files, processes the uploaded documents using a `DocumentProcessor`, and stores the processed documents in a `VectorStore`. The processed documents are then used for query processing.

### src/components/query_interface.py

This module handles the query interface functionality. It provides a text area for users to enter their queries and processes these queries using an `AIAgent`. The agent retrieves relevant documents from the `VectorStore` and generates answers based on the document context. The results are then displayed to the user.

### src/components/sidebar.py

This module handles the configuration options in the sidebar. It allows users to configure settings for document retrieval, AI agent response type, and export format. Users can also export the results in various formats such as CSV, JSON, or Excel.

### src/components/visualization.py

This module handles the visualization of results. It provides visual representations of the results, including confidence scores and result timelines. These visualizations help users understand the results better and assess the confidence of the generated answers.

### src/main.py

This is the main module that orchestrates the entire application. It initializes the Streamlit session state, sets up the page configuration, renders the sidebar, and integrates the various components such as document upload, query interface, and visualization. It also provides settings for theme selection (Light, Dark, System).

## Pipelining

The pipelining of the project can be broken down into the following steps:

1. **Initialization**: The `main.py` module initializes the Streamlit session state and sets up the page configuration.
2. **Sidebar Configuration**: The `render_sidebar` function in `sidebar.py` renders the sidebar with configuration options for RAG settings, AI agent settings, and export settings.
3. **Document Upload**: The `render_document_upload` function in `document_upload.py` handles the document upload process, processes the documents, and stores them in a vector store.
4. **Query Interface**: The `render_query_interface` function in `query_interface.py` allows users to enter queries, which are processed by the AI agent to retrieve relevant documents and generate answers.
5. **Visualization**: The `render_visualization` function in `visualization.py` visualizes the results, including confidence scores and timelines.
6. **Export**: The export functionality in `sidebar.py` allows users to export the results in various formats (CSV, JSON, Excel).

## Conclusion

The **GenAI Workflow System** is a comprehensive solution for document processing and question-answering. By leveraging advanced AI techniques and providing a user-friendly interface, it enables users to efficiently extract insights from their documents. The detailed explanation of the code and pipelining demonstrates the robust architecture and functionality of the system.
