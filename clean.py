import pandas as pd

def clean(input1, input2):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    df = pd.merge(df1, df2, left_on="respondent_id", right_on="id").drop("id", axis=1)
    df = df.dropna()
    df = df[df["job"].str.contains("insurance", case=False) == False]
    return df

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input1", help="Data file 1 (csv)")
    parser.add_argument("input2", help="Data file 2 (csv)")
    parser.add_argument("output", help="Cleaned data file (csv)")
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)

    cleaned.to_csv(args.output, index=False)

print(cleaned.shape)
