import json
from schema import document_class
from utils.weaviate_conn import SingeltonWeaviateConn


weaviateConnection = SingeltonWeaviateConn.get()
weaviateConnection.connect()
# weaviateConnection.delSchema("Document")
weaviateConnection.creat_schema(document_class)


with open("./data.json") as f:
    data = json.load(f)

weaviateConnection.insert_custom(data)

# ask = {
#     "question": "سید روح‌الله خمینی  چه کسی است ؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " نخستین رهبر جمهوری اسلامی ایران چه کسی است ؟",
#     "properties": ["text"]
# }


# ask = {
#     "question": " سید روح‌الله خمینی چه نظریه را تدوین کرد؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " سید روح‌الله خمینی چه رکورد گینسی را ثبت کرد؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " خامنه کیست ؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " خامنه‌ای کیست ؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " خامنه ای متولد چه سالیست ؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " خامنه‌ای متولد چه سالی است ؟",
#     "properties": ["text"]
# }


# ask = {
#     "question": " سیاستمدار و دومین رهبر جمهوری اسلامی ایران متولد چه سالی است ؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " دومین رهبر جمهوری اسلامی ایران چه کسی است ؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " سیاستمدار و دومین رهبر جمهوری اسلامی ایران چه کسی است ؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " علی اردشیر لاریجانی متولد چه سالیست ؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " علی اردشیر لاریجانی چه سالی رئیس واحد مرکزی خبر بود ؟",
#     "properties": ["text"]
# }


ask = {
    "question": "محمود احمدی نژاد در چه سالی برای تحصیل در مهندسی راه و ساختمان وارد دانشگاه علم و صنعت ایران شد؟",
    "properties": ["text"]
}

# ask = {
#     "question": "احمدی نژاد متولد چه سالی است؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": "احمدی نژاد کیست؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": "محمود احمدی نژاد کیست؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": "احمدی نژاد چندمین رئیس‌جمهور ایران بود؟",
#     "properties": ["text"]
# }

# ask = {
#     "question": " ششمین رئیس‌جمهور ایران زاده چه سالی است ؟",
#     "properties": ["text"]
# }




result = weaviateConnection.search_question("Document", ask)
# print(result)
print(result["data"]["Get"]["Document"][0]["_additional"]["answer"]["result"])
