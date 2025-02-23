from typing import List, Dict
import pandas as pd
import PyPDF2
import io
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class DocumentProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )

    def process_text(self, text: str) -> List[Document]:
        """Process raw text into chunks."""
        try:
            documents = [Document(page_content=text)]
            chunks = self.text_splitter.split_documents(documents)
            return chunks
        except Exception as e:
            raise Exception(f"Error processing text: {str(e)}")

    def process_file(self, file) -> List[Document]:
        """Process uploaded file into chunks."""
        try:
            if file.type == "text/plain":
                text = str(file.read(), "utf-8")
                return self.process_text(text)
            elif file.type == "application/pdf":
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return self.process_text(text)
            else:
                raise ValueError(f"Unsupported file type: {file.type}")
        except Exception as e:
            raise Exception(f"Error processing file: {str(e)}")

    def export_results(self, results: List[Dict]) -> pd.DataFrame:
        """Export results to a pandas DataFrame."""
        return pd.DataFrame(results)