dictA={'nama1':'jane doe','nama2':'jhon smith','nama3':'bob stone','telp1':'+27 555 5367',
       'telp2':'+27 555 6254','telp3':'+27 555 5689'}
print('Data Nomor Telpon')
print('------------------------------------')
print('|     Name    | Telepon Number     |')
print('|----------------------------------|')
print('|',dictA['nama1'],'|'  ,dictA['telp1'],'|','\n','|',dictA['nama2'],'|',dictA['telp2'],'|','\n' ,'|',dictA['nama3'],'|',dictA['telp3'],'|')
print('------------------------------------')

dictA['telp1']='+27 555 1024'
print('\n\tUbah No telepon jane')
print('------------------------------')
print('|    Name     | telepon number |')
print('--------------------------------')
print('|',dictA['nama1'],'|',dictA['telp1'],'|','\n','|',dictA['nama2'],'|',dictA['telp2'],'|','\n','|',dictA['nama3'],'|',dictA['telp3'],'|')
print('--------------------------------')

dictA['nama4']='Anna Cooper'
dictA['telp4']='+27 555 3237'
print('\n      Menambah Data Baru          ')
print('------------------------------------')
print('|     Name    | Telepon Number     |')
print('-----------------------------------|')
print('|',dictA['nama1'],'|',dictA['telp1'],'|','\n','|',dictA['nama2'],'|',dictA['telp2'],'|','\n','|',dictA['nama3'],'|',dictA['telp3'],'|','\n','|',dictA['nama4'],'|',dictA['telp4'],'|')
print('-------------------------------------')
print('\nCetak Nomer Telepon Bob stone =',dictA['telp3'])
