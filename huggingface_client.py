from huggingface_hub import InferenceClient

class HuggingFaceClient:
    def __init__(self):
        api_key = "YOUR_API_KEY"
        model = "mistralai/Mistral-7B-Instruct-v0.3"
        self.client = InferenceClient(model=model, token=api_key)

    def generate_response(self, csv_text: str, query: str):
        prompt = f"""
        You are an expert data analyst. Here is a CSV dataset:

        ```
        {csv_text}
        ```

        The user has asked: "{query}"
        Provide a clear and concise answer based only on the given data.
        """
        return self.client.text_generation(prompt, max_new_tokens=200).strip()
