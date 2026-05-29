import chromadb

c = chromadb.PersistentClient() #if persistent client is used, the data will be stored in the local directory. if not used, the data will be stored in memory and will be lost when the program is terminated.

collection = c.get_or_create_collection(name="my_collection")

# collection.add(
#     documents = ["This is a test document." , "This is another test document." ] ,
#     ids = [ "doc1", "doc2" ]
# )
query = input("Enter a word ")


results = collection.query(
    query_texts=[query],
    n_results=1
)
print("\nClosest match:")
print(results)
print()