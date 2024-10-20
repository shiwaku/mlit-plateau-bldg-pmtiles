import pandas as pd
import geopandas as gpd
from shapely import wkt

# 入力ファイルのパス
parquet_file_path = 'merged_building_lod0.parquet'

# parquetファイルをpandasで読み込む
df = pd.read_parquet(parquet_file_path)

# 出力したい属性のみを選択
selected_columns = [
    'source_filename', 'gml_id', 'building_id', 'prefecture', 'prefecture_code',
    'city', 'city_code', 'class', 'usage', 'measured_height'
]

# ジオメトリ列を除外し、指定された属性のみをCSVファイルに出力
output_csv_path = 'merged_building_lod0_attributes.csv'
df[selected_columns].to_csv(output_csv_path, index=False)

print(f"選択された属性データが '{output_csv_path}' に保存されました。")
