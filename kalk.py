#!/usr/bin/python
#-*- coding:utf -8-*-
'-===================-'
from glob import color
from glob import benner
import sys, subprocess as sub, readline
'-===================-'
'''TOOLS PENDIDIKANS:V
'''
class kalkulator:
    def __init__(self, pertama, kedua):
        self.pertambahan = pertama + kedua
        self.pengurangan = pertama - kedua
        self.perpangkatan = pertama ** kedua
        self.pembagian = pertama / kedua
        self.modulus = pertama % kedua
    def info(self, pesan):
        print (pesan)

class show(kalkulator):
    def __init__(self):
        sub.call('clear', shell=True)
        benner.rand()
        super().info('\tif your want exit in program KalkulatorTools please type "exit" in KalkukatorTools\n\n1. pertambahan\n2. pengurangan\n3. perpangkatan\n4. pembagian\n5. modulus\n')

show()

if __name__=='__main__':
    while True:
        ask = input(color.Color.red+'KalkulatorTools'+color.Color.green+':'+color.Color.whiteNormal+' ')
        
        if ask == '1':
            print (color.Color.red+'KalkulatorTools'+color.Color.purple+'/'+color.Color.blue+'pertambahan')
            while True:
                try:
                    bwb = int(input(color.Color.cyan+'bilangan_pertama'+color.Color.green+':'+color.Color.whiteNormal+' '))
                    bbb = int(input(color.Color.cyan+'bilangan_kedua'+color.Color.green+':'+color.Color.whiteNormal+' '))
                except:
                    print (color.Color.red+'Masukkan Angka!!')
                    sys.exit()
                    
                print (color.Color.white+'Hasilnya:'+color.Color.red+' %d'%(kalkulator(bwb, bbb).pertambahan))
        elif ask == '2':
            print (color.Color.red+'KalkulatorTools'+color.Color.purple+'/'+color.Color.blue+'pengurangan')
            while True:
                try:
                    m = int(input(color.Color.cyan+'bilangan_pertama'+color.Color.green+':'+color.Color.whiteNormal+' ')) 
                    i = int(input(color.Color.cyan+'bilangan_kedua'+color.Color.green+':'+color.Color.whiteNormal+' '))
                except:
                    print (color.Color.red+'Masukkan Angka!!')
                    sys.exit()
                print (color.Color.white+'Hasilnya:'+color.Color.red
+' %d'%(kalkulator(m, i).pengurangan))
        
        elif ask == '3':
            print (color.Color.red+'KalkulatorTools'+color.Color.purple+'/'+color.Color.blue+'perpangkatan')
            while True:
                try:
                    a = int(input(color.Color.cyan+'bilangan_pertama'+color.Color.green+':'+color.Color.whiteNormal+' '))
                    b = int(input(color.Color.cyan+'bilangan_kedua'+color.Color.green+':'+color.Color.whiteNormal+' '))
                except:
                    print (color.Color.red+'Masukkan Angka!!')
                    sys.exit()
                print (color.Color.white+'Hasilnya:'+color.Color.red+' %d'%(kalkulator(a, b).perpangkatan))
        elif ask == '4':
            print (color.Color.red+'KalkulatorTools'+color.Color.purple+'/'+color.Color.blue+'pembagian')
            while True:
                try:
                    z = int(input(color.Color.cyan+'bilangan_pertama'+color.Color.green+':'+color.Color.whiteNormal+' '))
                    y = int(input(color.Color.cyan+'bilangan_kedua'+color.Color.green+':'+color.Color.whiteNormal+' '))
                except:
                    print (color.Color.red+'Masukkan Angka!!')
                    sys.exit()
                print (color.Color.white+'Hasilnya:'+color.Color.red
+' %d'%(kalkulator(z, y).pembagian))

        elif '5' == ask:
            print (color.Color.red+'KalkulatorTools'+color.Color.purple+'/'+color.Color.blue+'modulus')
            while True:
                try:
                    gg = int(input(color.Color.cyan+'bilangan_pertama'+color.Color.green+':'+color.Color.whiteNormal+' '))
                    ii = int(input(color.Color.cyan+'bilangan_kedua'+color.Color.green+':'+color.Color.whiteNormal+' '))
                except:
                    print (color.Color.red+'Masukkan Angka!!')
                    sys.exit()
                print (color.Color.white+'Hasilnya:'+color.Color.red                                                            +' %d'%(kalkulator(gg, ii).modulus))

        elif ask == 'exit':
            sys.exit('Program Finished!!!')

        else:
            next        
