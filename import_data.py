import json
from rdflib import Graph
from schema import document_with_name_class
from utils.weaviate_conn import SingeltonWeaviateConn



################################################################
#read ttl files
################################################################
# weaviateConnection = SingeltonWeaviateConn.get()
# weaviateConnection.connect()
# weaviateConnection.delSchema("Document")
# weaviateConnection.creat_schema(document_class)

# # Load the TTL file into an RDF graph
# graph = Graph().parse('./ttls/triples_49.ttl', format='turtle')

# # Serialize the RDF graph to JSON-LD format
# json_ld = graph.serialize(format='json-ld', indent=4)

# # Load the JSON-LD data into a Python object
# data = json.loads(json_ld)

# with open("data.json", "w") as outfile:
#     json.dump(data, outfile)
    

# weaviateConnection.insert_custom(data)

################################################################
#read fawiki files
################################################################

weaviateConnection = SingeltonWeaviateConn.get()
weaviateConnection.connect()
weaviateConnection.delSchema("Document_with_name")
weaviateConnection.creat_schema(document_with_name_class)


with open('./data/Persian_WikiText_1.txt', 'r') as file :
    data = file.read()
docs = data.split('\n\n\n\n')
json_list = []
for doc in docs :
    if not doc:
        continue
    while doc.startswith('\n'):
        doc = doc[1:]
    try:
        name  =  doc.split('\n\n')[0]
        abs = doc.split('\n\n')[1]
        if "عنوان مقاله" not in name:
            continue
        name = name.replace('عنوان مقاله:', '')
        json_list.append({"name" : name.strip(), "abs" : abs.strip()})
    except:
        pass

weaviateConnection.insert_custom_with_name("Document_with_name", json_list)

print("wa")