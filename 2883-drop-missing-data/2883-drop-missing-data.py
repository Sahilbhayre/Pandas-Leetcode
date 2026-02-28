import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    result = students[students['name'].notnull()]
    return result