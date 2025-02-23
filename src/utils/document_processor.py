from typing import List, Dict
import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

class DocumentProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )

    def process_text(self, text: str) -> List[Document]:
        """Process raw text into chunks."""
        chunks = self.text_splitter.create_documents([text])
        return chunks

    def process_file(self, file) -> List[Document]:
        """Process uploaded file into chunks."""
        try:
            if file.type == "text/plain":
                text = str(file.read(), "utf-8")
                return self.process_text(text)
            elif file.type == "application/pdf":
                # Add PDF processing logic here
                raise NotImplementedError("PDF processing not implemented yet")
            else:
                raise ValueError(f"Unsupported file type: {file.type}")
        except Exception as e:
            raise Exception(f"Error processing file: {str(e)}")

    def export_results(self, results: List[Dict]) -> pd.DataFrame:
        """Export results to a pandas DataFrame."""
        return pd.DataFrame(results)