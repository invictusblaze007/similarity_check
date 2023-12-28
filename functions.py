from sentence_transformers import SentenceTransformer
import pinecone
import streamlit as st

# openai.api_key =st.secrets["GPT_API_KEY"] ## find at platform.openai.com
model = SentenceTransformer('all-MiniLM-L6-v2')

pinecone.init(api_key=st.secrets["PINECONE_API"], # find at app.pinecone.io
              environment='gcp-starter' # next to api key in console
             )
index = pinecone.Index('') # index name from pinecone


# def find_match(input):
#     input_em = model.encode(input).tolist()
#     result = index.query(input_em, top_k=2, includeMetadata=True)
#     return result['matches'][0]['metadata']['text'] + "\n" + result['matches'][1]['metadata']['text']


# def get_conversation_string(requests, responses):
#     conversation_string = ""
#     for i in range(len(responses) - 1):
#         conversation_string += f"Human: {requests[i]}\n"
#         conversation_string += f"Invictus Blaze: {responses[i + 1]}\n"
#     return conversation_string



