import json
from schema import document_class
from utils.weaviate_conn import SingeltonWeaviateConn


weaviateConnection = SingeltonWeaviateConn.get()
weaviateConnection.connect()
# weaviateConnection.delSchema("Document")
# weaviateConnection.creat_schema(document_class)


# with open("./data.json") as f:
#     data = json.load(f)

# weaviateConnection.insert_custom(data)

ask = {
    "question": "when is iran president birthday?",
    "properties": ["text"]
}

result = weaviateConnection.get_all_data("Document")
specific_result_vector = result["data"]["Get"]["Document"][3]["_additional"]["vector"]
result_near = weaviateConnection.search_near_vector("Document", specific_result_vector,
                                                    "text")
print(result_near["data"]["Get"]["Document"][0])
