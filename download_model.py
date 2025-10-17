from sentence_transformers import SentenceTransformer

print("Downloading and caching the embedding model...")

# This line will trigger the download and save the model to a local cache.
model = SentenceTransformer('all-MiniLM-L-6-v2')

print("Model downloaded and cached successfully!")