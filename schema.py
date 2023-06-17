document_class = {
    "class": "Document",
    "description": "A class called document",
    "vectorizer": "text2vec-transformers",
    "properties":
    [
        {
            "name": "content",
            "description": "Content that will be vectorized",
            "dataType": ["text"]
               }

    ],

}

document_with_name_class = {
    "class": "Document_with_name",
    "description": "A class called document",
    "vectorizer": "text2vec-transformers",
    "properties":
    [
         {
            "name": "name",
            "description": "name that will be vectorized",
            "dataType": ["text"]
               },
        {
            "name": "abs",
            "description": "Content that will be vectorized",
            "dataType": ["text"]
               }

    ],

}
