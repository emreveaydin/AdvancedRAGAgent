from dotenv import load_dotenv
from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering"
]

# Her URL için ayrı bir loader oluşturup, load() metodunu çağırıyoruz
docs = []
for url in urls:
    loader = WebBaseLoader(url)
    docs.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=0)
split_docs = text_splitter.split_documents(docs)

# Vectorstore'u oluştur
vectorstore = Qdrant.from_documents(
    documents=split_docs,
    embedding=OpenAIEmbeddings(),
    url="http://localhost:6333",
    collection_name="rag-collection",
)

# Var olan vectorstore'dan retriever oluştur
retriever = vectorstore.as_retriever()

"""
Vector Database Setup and Configuration

Implements the vector store setup using Qdrant for document storage and retrieval.
This module handles:
1. Document loading from specified URLs
2. Text splitting for optimal chunk size
3. Vector store initialization with OpenAI embeddings
4. Retriever configuration for document lookup

The vector store serves as the primary knowledge base for the RAG system,
storing pre-processed documents that can be semantically searched.

Configuration:
- Uses RecursiveCharacterTextSplitter with 250 token chunks
- Implements OpenAI embeddings for vector representation
- Connects to a local Qdrant instance on port 6333
"""





