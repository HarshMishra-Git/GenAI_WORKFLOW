from typing import Dict, List
import os
from openai import OpenAI

class AIAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        # the newest OpenAI model is "gpt-4o" which was released May 13, 2024
        self.model = "gpt-4o"

    def process_query(self, query: str, context: List[Dict]) -> Dict:
        """Process a query with context from RAG."""
        try:
            context_text = "\n".join([doc['content'] for doc in context])
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant with access to relevant context. "
                                                "Provide accurate answers based on the context provided."},
                    {"role": "user", "content": f"Context:\n{context_text}\n\nQuery: {query}"}
                ],
                response_format={"type": "json_object"},
            )
            
            return {
                "answer": response.choices[0].message.content,
                "context": context
            }
        except Exception as e:
            raise Exception(f"Error processing query: {str(e)}")

    def analyze_results(self, results: List[Dict]) -> Dict:
        """Analyze results and provide insights."""
        try:
            results_text = "\n".join([str(result) for result in results])
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Analyze the following results and provide insights in JSON format."},
                    {"role": "user", "content": results_text}
                ],
                response_format={"type": "json_object"},
            )
            
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error analyzing results: {str(e)}")
