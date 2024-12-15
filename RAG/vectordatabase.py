from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Milvus


class VectorDatabase:
    """
    处理向量数据库
    """

    def __init__(self):
        self.embedding = (
            HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L12-v2"))

        self.db = Milvus(
            embedding_function=self.embedding,
            collection_name="arXiv",
            connection_args={"host": "10.58.0.2", "port": "19530"})




if __name__ == '__main__':
    vdb = VectorDatabase()
    res = vdb.db.similarity_search_with_score("什么是大语言模型？")
    print(res[0])