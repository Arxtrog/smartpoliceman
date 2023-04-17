from langchain.document_loaders import OnlinePDFLoader
from langchain.indexes import VectorstoreIndexCreator

query = input()

loader = OnlinePDFLoader("https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19970980602/U/D19970602Lj.pdf")
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))