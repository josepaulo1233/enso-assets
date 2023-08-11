for file in *.nc; do

nino34lati=-5
nino34latf=5
nino34loni=-170
nino34lonf=-120

cdo -fldmean -sellonlatbox,${nino34loni},${nino34lonf},${nino34lati},${nino34latf} ${file} nino34_files/${file}.nino34

done
