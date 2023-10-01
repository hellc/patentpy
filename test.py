# import get_bulk_patent_data functionality
from patentpy.acquire import get_bulk_patent_data
from pandas import DataFrame


def rename(df: DataFrame):
    return df.rename(
        columns={
            "WKU": "WKU",
            "Title": "title",
            "Abstract": "abstract",
            "App_Date": "application_date",
            "Issue_Date": "publication_date",
            "Inventor": "inventor",
            "Assignee": "assignee",
            "ICL_Class": "icl",
            "References": "citations",
            "Claims": "claims",
        }
    )


patents_df = get_bulk_patent_data(year=2002, week=1)
patents_df.to_csv("test.csv")
patents_df = rename(patents_df)
patents = patents_df.to_dict("records")
print(patents[0])

patents_df.to_json(path_or_buf="test.json", orient="records")
