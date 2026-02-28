import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    heavy_df = animals[animals['weight'] > 100]
    result = heavy_df.sort_values(by='weight',ascending=False)[['name']]
    return result