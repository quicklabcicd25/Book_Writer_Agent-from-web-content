import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(anonymized_telemetry=False))
collection = client.get_or_create_collection("book_versions")

def store_version(version_id: str, content: str):
    collection.add(documents=[content], ids=[version_id])
    print(f"💾 Stored version: {version_id}")

def retrieve_version(version_id: str) -> str:
    result = collection.get(ids=[version_id])
    return result['documents'][0] if result['documents'] else "Version not found"

