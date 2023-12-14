import pysolr
from sentence_transformers import SentenceTransformer

solr = pysolr.Solr('http://localhost:8983/solr/news')
model = SentenceTransformer('all-MiniLM-L6-v2')


def semantic_search(query):
    print(f"************ Semantic search for {query}")
    embedding = model.encode([query])
    solr_response=solr.search(fl=['id', 'title'],
                  q="{!knn f=vector topK=10}"+str([float(w) for w in embedding[0]]),
                  rq='{!rerank reRankQuery=$rqq reRankDocs=50 reRankWeight=3}',
                  rqq="{!edismax qf='title^5 content^2'}"+query,
                  rows = 30)
    print(f"found {len(solr_response)} results")
    for item in solr_response:
        print(item["title"])

semantic_search("Trump speaking on immigration")