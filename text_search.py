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

result = weaviateConnection.search_near_text("Document", "او در انتخابات ریاست جمهوری ۱۳۹۶ و ۱۴۰۰ نامزد شد اما صلاحیتش مورد تأیید شورای نگهبان قرار نگرفت")
# print(result)
for item in result["data"]["Get"]["Document"]:
    print("*"*30, "\n", item, "\n\n","*"*30,)
 