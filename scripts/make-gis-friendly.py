"""
This snippet demonstrates how to access and convert the buildings
data from .csv.gz to geojson for use in common GIS tools. You will
need to install pandas, geopandas, and shapely.
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import shape

def main():
    # this is the name of the geography you want to retrieve. update to meet your needs
    location = 'Greece'

    dataset_links = pd.read_csv("https://minedbuildings.blob.core.windows.net/global-buildings/dataset-links.csv")
    greece_links = dataset_links[dataset_links.Location == location]
    for _, row in greece_links.iterrows():
        df = pd.read_json(row.Url, lines=True)
        df['geometry'] = df['geometry'].apply(shape)
        gdf = gpd.GeoDataFrame(df, crs=4326)
        gdf.to_file(f"{row.QuadKey}.geojson", driver="GeoJSON")


if __name__ == "__main__":
    main()Turkey,120322312,https://minedbuildings.blob.core.windows.net/global-buildings/2022-11-15/global-buildings.geojsonl/RegionName%3DTurkey/quadkey%3D120322312/part-00120-2cb4a5ad-6652-48b0-a336-f09518f4c9e5.c000.csv.gz,70.4KB
        
