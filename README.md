# mlit-plateau-bldg-pmtiles
## 3D都市モデル（Project PLATEAU）建築物モデル（2022年）PMTiles
### データの出典
- [法務省地図XMLアダプトプロジェクト](https://github.com/amx-project)にて公開されている、[3D都市モデル（Project PLATEAU）建築物モデルLOD1のPMTiles](https://github.com/amx-project/apb)をリネームしたもの
- 対象都市：日本全国123都市（2022年公開時点）
### タイルデータURL
```
https://shiworks.xsrv.jp/pmtiles-data/plateau/PLATEAU_2022_LOD1.pmtiles
```
- ライセンス：-

## 3D都市モデル（Project PLATEAU）建築物モデル（2023年）PMTiles
### データの出典
- [Pacific Spatial Solutions株式会社](https://pacificspatial.com/)が作成した、[3D都市モデル（Project PLATEAU）建築物モデルLOD0のGeoParquet](https://beta.source.coop/repositories/pacificspatial/flateau/description/)（CC BY 4.0ライセンス）
- 対象都市：日本全国211都市（2023年公開時点）
### データの作成方法
- GDAL/OGRでGeoParquetを一旦GeoJSONに変換後、felt/tippecanoeでPMTilesを生成
```
ogr2ogr -f "GeoJSON" PLATEAU_2023_LOD0.geojson merged_building_lod0.parquet
tippecanoe -o PLATEAU_2023_LOD0.pmtiles PLATEAU_2023_LOD0.geojson -Z16 -z16 -pf -pk
```
### タイルデータURL
```
https://shiworks.xsrv.jp/pmtiles-data/plateau/PLATEAU_2023_LOD0.pmtiles
```
- ライセンス：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
