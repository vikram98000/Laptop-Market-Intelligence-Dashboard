import pandas as pd
df = pd.read_csv("laptop_dataset_final.csv", low_memory=False)
df.head()
df.info()
df.shape
df.columns
df.describe(include='all')
print('missing values' , df.isnull().sum())
df.duplicated().sum()
df.drop_duplicates(inplace=True)
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(","",regex=False)
    .str.replace(")","",regex=False)
    .str.replace("/","_")
)
df['price_rs'] = (
    df['price_rs']
      .replace("₹","",regex=True)
      .replace(",","",regex=True)
      .replace("nan", None)   # turn string "nan" back into None
)

df['price_rs'] = pd.to_numeric(df['price_rs'], errors="coerce")



df['capacity'] = (
    df['capacity']
      .astype(str)
      .str.replace("GB","",regex=False)
      .str.strip()
)

df['capacity'] = pd.to_numeric(df['capacity'])

df['ssd_capacity'] = (
    df['ssd_capacity']
      .astype(str)
      .str.replace("GB","",regex=False)
      .str.replace("TB","000",regex=False)
      .str.strip()
)
df['ssd_capacity'] = pd.to_numeric(df['ssd_capacity'], errors='coerce')

df['weight'] = (
    df['weight']
      .astype(str)
      .str.replace("kg","",regex=False)
      .str.strip()
)
df['weight'] = (
    df['weight']
      .astype(str)
      .str.extract(r'(\d+\.?\d*)')[0]
)

df['weight'] = pd.to_numeric(df['weight'], errors="coerce")


df['battery_life'] = (
    df['battery_life']
      .astype(str)
      .str.extract(r'(\d+\.?\d*)')[0]
)

df['battery_life'] = pd.to_numeric(df['battery_life'], errors="coerce")


df['refresh_rate'] = (
    df['refresh_rate']
      .astype(str)
      .str.extract(r'(\d+\.?\d*)')[0]   # extract digits and decimals
)


df['brightness'] = (
    df['brightness'].astype(str).str.extract(r'(\d+)')[0]
)
df['brightness'] = pd.to_numeric(df['brightness'], errors="coerce")

df['battery_capacity'] = (
    df['battery_capacity'].astype(str).str.extract(r'(\d+)')[0]
)
df['battery_capacity'] = pd.to_numeric(df['battery_capacity'], errors="coerce")

df.nunique().sort_values()

df.to_csv("cleaned_laptop_dataset.csv", index=False)
