import pandas as pd
import os


csv_dir = "Entrega_2/data_set_videos_csv"
csv_files = [f for f in os.listdir(csv_dir) if f.endswith(".csv")]

dfs = []
for file in csv_files:
    df = pd.read_csv(os.path.join(csv_dir, file))
    dfs.append(df)

# Un solo DataFrame
df_total = pd.concat(dfs, ignore_index=True)

df_total.to_csv("./Entrega_3/data_set_videos/dataset_final.csv", index=False)
print("Dataset unificado guardado como 'dataset_final.csv'")
