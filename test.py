# import get_bulk_patent_data functionality
from patentpy.acquire import get_bulk_patent_data

patents_df = get_bulk_patent_data(year=1995, week=1)
print(patents_df)
patents_df.to_csv("test.csv")
