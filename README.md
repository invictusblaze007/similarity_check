# LangChain Similarity Checker

Welcome to the LangChain Similarity Checker! 🐱‍👤 This tool allows you to check the similarity score and discover similar chunks within your English or Urdu data using LangChain.

## Prerequisites

Before getting started, ensure you have the required packages installed and you have the Pinecone API key (one index is freely available until 28-12-2023).

- Put your Pinecone API key in `.streamlit/secrets.toml`.
- Open your terminal and run the following command:

  ```bash
  pip install unstructured[pdf] chardet langchain streamlit pinecone sentence_transformers
  ```
  **Note:** It's crucial to have the following dependencies installed to ensure smooth execution:
### Step 1: Upload Your Data

◍. Place your English or Urdu data files in the `data` folder.
◍. Ensure your files are in a compatible format for analysis.

### Step 2: Run "chunks_store_embedding.py"

◍. Execute the following command in your terminal to store embeddings of language chunks:

```bash
echo "python chunks_store_embedding.py"
```
 **Note:**This step is critical as it prepares the necessary embeddings for further analysis.

###Step 3: Run "main.py"
◍Launch the Streamlit UI to explore similarity scores and discover similar chunks.Execute the following command in your terminal:
```bash
echo "streamlit run main.py"
```
◍. Your default web browser will open, revealing the user interface for LangChain Similarity Checker.

## Customization and Enhancement

Your default web browser will open, revealing the user interface for LangChain Similarity Checker.
Feel free to customize and enhance this tool according to your specific requirements. Happy exploring! 🎉


