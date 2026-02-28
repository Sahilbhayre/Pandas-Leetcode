import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    combined = pd.concat([df1, df2], ignore_index = True)
    result = combined.groupby(['student_id','name', 'age']).sum().reset_index()
    return result 