import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = [
    [11, 12, 13],
    [21, 2, 20],
    [1, 44, 15]
    ]

data = pd.DataFrame(df)
Selected_features=[0,1,2]
# Просмотр корреляции
def CorrPlt(data,Selected_features):
  X = data[Selected_features]
  plt.subplots(figsize=(8, 5))
  sns.heatmap(X.corr(), annot=True, cmap="RdYlGn",vmin=-1, vmax=1)
  plt.show()
CorrPlt(data,Selected_features)
print(data.isna().sum())
print(data.shape[0])
