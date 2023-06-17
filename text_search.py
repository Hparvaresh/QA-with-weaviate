import json
from schema import document_class
from utils.weaviate_conn import SingeltonWeaviateConn


weaviateConnection = SingeltonWeaviateConn.get()
weaviateConnection.connect() 

result = weaviateConnection.search_near_text("Document_with_name","abs", "سعدی کیست")
for item in result["data"]["Get"]["Document_with_name"]:
    print("*"*30, "\n", item, "\n\n","*"*30,)
