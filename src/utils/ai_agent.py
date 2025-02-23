from typing import Dict, List
from transformers import pipeline

class AIAgent:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def process_query(self, query: str, context: List[Dict]) -> Dict:
        """Process a query with context from RAG."""
        try:
            context_text = "\n".join([doc['content'] for doc in context])

            result = self.qa_pipeline(question=query, context=context_text)

            return {
                "answer": result['answer'],
                "context": context
            }
        except Exception as e:
            raise Exception(f"Error processing query: {str(e)}")

    def analyze_results(self, results: List[Dict]) -> Dict:
        """Analyze results and provide insights."""
        try:
            # Simple analysis without requiring API calls
            return {
                "summary": "Analysis completed successfully",
                "num_results": len(results),
                "average_score": sum(r.get('score', 0) for r in results) / len(results) if results else 0
            }
        except Exception as e:
            raise Exception(f"Error analyzing results: {str(e)}")