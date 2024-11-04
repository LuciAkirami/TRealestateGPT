import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("arvanshul/gurgaon-real-estate-99acres-com", force_download=True)
df = pd.read_csv(path+"/hyderabad.csv")
df.to_csv("./data/hyderabad.csv", index=False)
