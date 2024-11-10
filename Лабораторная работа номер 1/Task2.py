disk_Mb = 1.44
kol_st = 100
str_st = 50
kol_sim = 25
sim_bit = 4

dis_bit = disk_Mb * 1024 * 1024
ob_kn = sim_bit * kol_sim * str_st * kol_st
dis_kn = int( dis_bit / ob_kn )
print( "Количество книг, помещающихся на дискету:", dis_kn )
