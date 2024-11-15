import os

def chunker (filepath, start_id):
    chunks = {}

    with open (filepath) as filedata:
        documents = []
        metadatas = []
        chunk_ids = []
        chunk_id = start_id + 1
    
        while (chunk := filedata.read(500)) and (chunk_id < start_id + 200):
            print(chunk)
            print(chunk_id)
            documents.append(chunk)
            chunk_ids.append(str(chunk_id))
            metadatas.append({"temp": "temp"})
            chunk_id += 1

        chunks['documents'] = documents
        chunks['metadatas'] = metadatas
        chunks['ids'] = chunk_ids
    
    return chunks

def semantic_chunker (filepath, start_id):
    chunks = {}

    with open(filepath) as filedata:
        documents = []
        documents = []
        metadatas = []
        chunk_ids = []
        chunk_id = start_id + 1

        while (chunk := filedata.read(500)) and (chunk_id < start_id + 200):
            print(chunk)
            print(chunk_id)
            documents.append(chunk)
            chunk_ids.append(str(chunk_id))
            metadatas.append({"temp": "temp"})
            chunk_id += 1

        chunks['documents'] = documents
        chunks['metadatas'] = metadatas
        chunks['ids'] = chunk_ids
    
    return chunks