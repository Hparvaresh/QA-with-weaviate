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



result = weaviateConnection.get_all_data("Document")
# print(result)
for item in result["data"]["Get"]["Document"]:
    print("*"*30, "\n", item, "\n\n","*"*30,)
# specific_result_vector = result["data"]["Get"]["Document"][0]["_additional"]["vector"]
# result_near = weaviateConnection.search_near_vector("Document", specific_result_vector,
#                                                     "text")
# print(result_near["data"]["Get"]["Document"][0])
