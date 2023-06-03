from conf.conf import (
    Weaviate_HOST
)
import weaviate
import os
import sys
sys.path.insert(0, '..')


class WeaviateConn():

    def __init__(self):
        self.host = Weaviate_HOST
        self.client = None

    def connect(self):
        self.client = weaviate.Client(
            self.host)

    def creat_schema(self, schema: dict):
        try:
            self.client.schema.create({"classes": [schema]})
        except Exception:
            print("Warning: schema is exist.")

    def get_schemas(self):
        return self.client.schema.get()

    def insert_custom(self, data, batch_size=100):
        with self.client.batch as batch:
            batch.batch_size = batch_size
            for i, d in enumerate(data['doc_data']):
                print(f"importing event: {i+1}")
                properties = {
                    "text": d["text"]
                }
                self.client.batch.add_data_object(properties, "Document")

    def check_batch_result(self, results: dict):
        if results is not None:
            for result in results:
                if (
                    'result' in result
                    and 'errors' in result['result']
                    and 'error' in result['result']['errors']
                ):
                    print(result['result']['errors']['error'])

    def delSchema(self, schema):
        self.client.schema.delete_class(schema)

    def search_question(self, class_name, ask_query):
        return (
            self.client.query
            .get(class_name, ["_additional {answer {result} }"])
            .with_ask(ask_query)
            .with_limit(1)
            .do()
        )
    def search_near_text(self, class_name, text):
        return (
            self.client.query
            .get(class_name, "text")
            .with_additional(["distance"])
            .with_near_text(
                {
                "concepts" : [text]
                }
            )
            .with_limit(1).do()
        )
    def get_all_data(self, class_name):
        return(
            
            self.client.query
            .get(class_name, ["text", "_additional {vector}"])
            .do()
        )
    
    def search_near_vector(self, class_name, vec, fileds, certainty=0.5):
        vec_content = {'vector':vec, 'certainty':certainty}
        return self.client.query.get(class_name,fileds).with_near_vector(vec_content).do()


class SingeltonWeaviateConn:
    instance = None

    def __init__(self):
        raise ValueError("cant initialize this class")

    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = WeaviateConn()
        return cls.instance


if __name__ == "__main__":
    conn = SingeltonWeaviateConn.get()

    print(conn.connect().is_live())
