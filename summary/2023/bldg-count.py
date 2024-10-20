import pandas as pd

# CSVファイルの読み込み（city_codeを文字列として扱う）
input_file = 'merged_building_lod0_attributes.csv'
df = pd.read_csv(input_file, dtype={'city_code': str})

# city、city_codeごとに高さ情報の有無を集計
result = df.groupby(['city', 'city_code']).apply(lambda x: pd.Series({
    '建築物高さ情報有り件数': x['measured_height'].notna().sum(),
    '建築物高さ情報無し件数': x['measured_height'].isna().sum(),
    '合計件数': len(x)
})).reset_index()

# 割合を計算して列を挿入
result['建築物高さ情報有り割合'] = result['建築物高さ情報有り件数'] / result['合計件数']
result['建築物高さ情報無し割合'] = result['建築物高さ情報無し件数'] / result['合計件数']

# 列の順序を調整（割合を合計件数の前に挿入）
result = result[['city', 'city_code', 
                 '建築物高さ情報有り件数', '建築物高さ情報有り割合', 
                 '建築物高さ情報無し件数', '建築物高さ情報無し割合', 
                 '合計件数']]

# city_codeでソート
result = result.sort_values(by='city_code')

# CSVに出力
output_file = 'plateau_2023_lod0_height_summary.csv'
result.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f'結果が {output_file} に保存されました。')
