'reinit'
'c'
'open sst.ctl'

*i=1
*i=12419
i=13938
l=15196

nino34lati=-5
nino34latf=5
nino34loni=-170
nino34lonf=-120

nino4lati=-5
nino4latf=5
nino4loni=-160
nino4lonf=-150

nino3lati=-5
nino3latf=5
nino3loni=-150
nino3lonf=-90

nino12lati=-10
nino12latf=0
nino12loni=-90
nino12lonf=-80

write('./txt/sst_nino34_daily3.txt', 'dia anom34 anom4 anom3 anom12')

while i<=l

'set t 'i
'q time'
data=subwrd(result,3)
dia=substr(data,4,2)
hora=substr(data,1,2)
mes=substr(data,6,3)
ano=substr(data,9,4)
dia_fmt = dia'-'mes'-'ano

'define anom34 = aave(anom/100, lon='nino34loni', lon='nino34lonf', lat='nino34lati', lat='nino34latf')'
'define anom4 = aave(anom/100, lon='nino4loni', lon='nino4lonf', lat='nino4lati', lat='nino4latf')'
'define anom3 = aave(anom/100, lon='nino3loni', lon='nino3lonf', lat='nino3lati', lat='nino3latf')'
'define anom12 = aave(anom/100, lon='nino12loni', lon='nino12lonf', lat='nino12lati', lat='nino12latf')'

'set gxout print'
'set prnopts %6.5f 1 1' 

'd anom34'
tmp1=sublin(result,2)
tmp1=subwrd(tmp1,1)

'd anom4'
tmp2=sublin(result,2)
tmp2=subwrd(tmp2,1)

'd anom3'
tmp3=sublin(result,2)
tmp3=subwrd(tmp3,1)

'd anom12'
tmp4=sublin(result,2)
tmp4=subwrd(tmp4,1)

write('./txt/sst_nino34_daily3.txt', dia_fmt' 'tmp1' 'tmp2' 'tmp3' 'tmp4, append)

i = i + 1

endwhile

