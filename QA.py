import json
from schema import document_class
from utils.weaviate_conn import SingeltonWeaviateConn


weaviateConnection = SingeltonWeaviateConn.get()
weaviateConnection.connect() 
weaviateConnection.creat_schema(document_class)


with open("./data.json") as f:
    data = json.load(f)
    
weaviateConnection.insert_custom(data)
    
ask = {
    "question": "when iran president born?",
    "properties": ["text"]
}

result = weaviateConnection.search_question("Document", ask)

print(result["data"]["Get"]["Document"][0]["_additional"]["answer"]["result"])
