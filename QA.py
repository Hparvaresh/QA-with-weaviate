from schema import document_class
from utils.weaviate_conn import SingeltonWeaviateConn


weaviateConnection = SingeltonWeaviateConn.get()
weaviateConnection.connect()


# ask = {
#     "question": "ابوالفضل بلعمی پدر چه کسی است؟",
#     "properties": ["abs"]
# }

# ask = {
#     "question": "افغانستان در کجا واقع شده است",
#     "properties": ["abs"]
# }


# ask = {
#     "question": "حزب کمونیست کوبا بر چه مدلی برپا شده است؟",
#     "properties": ["abs"]
# }

ask = {
    "question": "تنها حزب قانونی کشور کوبا چیست ؟",
    "properties": ["abs"]
}

result = weaviateConnection.search_question("Document_with_name", ask)
# print(result)
print(result["data"]["Get"]["Document_with_name"][0]["_additional"]["answer"]["result"])
