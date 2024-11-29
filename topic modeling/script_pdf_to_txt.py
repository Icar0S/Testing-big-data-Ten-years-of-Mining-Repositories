import aspose.words as aw


pdf = aw.Document(
    "./docs/data/articles_test/2-The_Framework_of_Extracting_Unstructured_Usage_for_Big_Data_Platform.pdf"
)

pdf.save("docs/data/articles_test/test.txt")
