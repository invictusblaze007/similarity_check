from sentence_transformers import SentenceTransformer
import pinecone
import streamlit as st

# Initialize Pinecone
pinecone.init(api_key=st.secrets["PINECONE_API"], environment='gcp-starter')
index = pinecone.Index('') #put here your index name

# Initialize Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

query = st.text_input("Write something")

if query:
    with st.spinner("Calculating Similarity..."):
        # Properly handle exceptions for Pinecone queries or model encoding
        try:
            # Encode user input
            input_embedding = model.encode(query).tolist()

            # Use Pinecone to find similar contexts
            result = index.query(input_embedding, top_k=2, includeMetadata=True)

            # Extract the similarity scores and similar chunks
            similarity1 = result['matches'][0]['score']
            similarity2 = result['matches'][1]['score']
            similar_chunk1 = result['matches'][0]['metadata']['text']
            similar_chunk2 = result['matches'][1]['metadata']['text']

            st.write(f"Similarity Rate with Context 1: {similarity1:.4f}")
            st.write(f"Similar Chunk 1:")
            st.write(similar_chunk1)
            st.write("\n---\n")
            st.write(f"Similarity Rate with Context 2: {similarity2:.4f}")
            st.write(f"Similar Chunk 2:")
            st.write(similar_chunk2)

        except Exception as e:
            st.error(f"An error occurred: {e}")
