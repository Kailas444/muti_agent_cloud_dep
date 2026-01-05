
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class RAGAgent:
    def __init__(self, persist_dir="vector_db"):
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        self.persist_dir = persist_dir

    def ingest(self, text):
        docs = [Document(page_content=text)]
        splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        self.vdb = Chroma.from_documents(chunks, self.embeddings, persist_directory=self.persist_dir)

    def retrieve(self, query):
        results = self.vdb.similarity_search(query, k=2)
        if not results:
            return "NO_CONTEXT"
        return "\n".join([r.page_content for r in results])
