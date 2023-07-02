import os
import json
import contextlib
from .schema import document
from .utils.weaviate_conn import SingeltonWeaviateConn


class WeaviateManager():
    def __init__(self):
        self.weaviateConnection = SingeltonWeaviateConn.get()
        self.weaviateConnection.connect()
        script_directory = os.path.dirname(os.path.abspath(__file__))
        self.data_directory = f'{script_directory}/data/'
        self.schema_name = "Document"
        self.delete_schema()
        self.make_schema()
        self.import_wiki_text()

    def delete_schema(self):
        self.weaviateConnection.delSchema(self.schema_name)

    def make_schema(self):
        self.weaviateConnection.creat_schema(document)

    def question(self, ask_question):
        try:
            ask = {
                "question": ask_question,
                "properties": ["abstract"]
            }
            print("ask question:", ask)
            result = self.weaviateConnection.search_question(
                self.schema_name, ask)
            print("result question:", result)
            return result, []
        except Exception as e:
            return [], json.dumps({"Error :": str(e)})

    def import_wiki_text(self):
        docs = []

        if os.path.exists(self.data_directory):
            for file in os.listdir(self.data_directory):
                with open(f'{self.data_directory}/{file}', 'r') as file:
                    data = file.read()
                docs.extend(data.split('\n\n\n'))
        else:
            print(f"Directory '{self.data_directory}' does not exist.")
            return

        json_list = []

        for doc in docs:
            if not doc:
                continue

            while doc.startswith('\n'):
                doc = doc[1:]

            with contextlib.suppress(Exception):
                name = doc.split('\n\n')[0]
                abstract = doc.split('\n\n')[1]

                if "عنوان مقاله" not in name:
                    continue

                name = name.replace('عنوان مقاله:', '')

                json_list.append(
                    {"name": name.strip(), "abstract": abstract.strip()})

        self.weaviateConnection.insert_custom_with_name(
            self.schema_name, json_list)

    def text_search(self, text):
        result = self.weaviateConnection.search_near_text(
            self.schema_name, "abstract", text)
        return result["data"]["Get"][self.schema_name]
