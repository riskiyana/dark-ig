
#!/usr/bin/python

# -*- coding: utf-8 -*-

# WGen - Wordlist Generator (4 Jan 2018 (14:32))

# Author: DedSecTL/DTL/Gameye98

# Team: BlackHole Security

# Github: https://github.com/Gameye98

# Blog: http://droidsec9798-com.mwapblog.com

import os

import sys

import time


def jalankan_ulang_program():

	python = sys.executable

	os.execl(python, python, * sys.argv)

	curdir = os.getcwd()


def bersih_layar():

	if sys.platform == "linux2":

		os.system("clear")

	elif sys.platform == "win32":

		os.system("cls")

	else:

		os.system("clear")


wgen_banner="""\033[1;37m
================================================
* AUTHOR : MR_Y4ns
* IG     : riski_yans
* PESAN  : BUAT LAH PASSWORD YG KALIAN INGIN KAN
================================================
W O R D L I S T # G E N E R A T O R\033[0m

"""


bersih_layar()

print wgen_banner

print '\033[1;37mtekan "bantuan" untuk dapatkan menu bantuan\033[0m'

print


interpreter='*>'

if os.geteuid()==0:

	interpreter='#>'


bantuan="""\033[1;37m

Menu Bantuan WGen:

	Perintah Deskripsi

	-------- ----------

	bantuan dapatkan menu bantuan

	bersih bersihkan layar

	hasilkan hasilkan wordlist

	ulang jalankan ulang program

	keluar keluar dari program\033[0m

"""


opt=True

while opt:

	wgen=raw_input('\033[1;37mWGen' + interpreter + ' ')

	if wgen == 'bantuan':

		print bantuan

	elif wgen == 'bersih':

		bersih_layar()

	elif wgen == 'hasilkan':

		try:

			a=raw_input("\nWGen?> Nama Depan: ")

			file=open(""+a+".txt", 'w')

			b=raw_input("WGen?> Nama Tengah: ")

			c=raw_input("WGen?> Nama Belakang: ")

			d=raw_input("WGen?> Nama Panggilan: ")

			e=raw_input("WGen?> Tanggal Lahir (ex: DDMMYY): ")

			f=e[0:2]

			g=e[2:4]

			h=e[4:]

			i=raw_input("\nWGen?> Nama Pacar: ")

			j=raw_input("WGen?> Nama Panggilan Pacar: ")

			k=raw_input("WGen?> Tanggal Lahir Pacar (ex: DDMMYY): ")

			l=k[0:2]

			m=k[2:4]

			n=k[4:]

			file.write("%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % (a,c,a,b,b,a,b,c,c,a,c,b,a,a,b,b,c,c,a,d,b,d,c,d,d,d,d,a,d,b,d,c,a,e,a,f,a,g,a,h,b,e,b,f,b,g,b,h,c,e,c,f,c,g,c,h,d,e,d,f,d,g,d,h,e,a,f,a,g,a,h,a,e,b,f,b,g,b,h,b,e,c,f,c,g,c,h,c,e,d,f,d,g,d,h,d,d,d,a,f,g,a,g,h,f,g,f,h,f,f,g,f,g,h,g,g,h,f,h,g,h,h,h,g,f,a,g,h,b,f,g,b,g,h,c,f,g,c,g,h,d,f,g,d,g,h,a,i,a,j,a,k,i,e,i,j,i,k,b,i,b,j,b,k,c,i,c,j,c,k,e,k,j,a,j,b,j,c,j,d,j,j,k,a,k,b,k,c,k,d,k,k,i,l,i,m,i,n,j,l,j,m,j,n,j,k))

			wg = 0

			while (wg < 100):

				wg = wg + 1

				file.write(a + str(wg) + '\n')

			en = 0

			while (en < 100):

				en = en + 1

				file.write(i + str(en) + '\n')

			word = 0

			while (word < 100):

				word = word + 1

				file.write(d + str(word) + '\n')

			gen = 0

			while (gen < 100):

				gen = gen + 1

				file.write(j + str(gen) + '\n')

			file.close()

			time.sleep(1.5)

			print " \n[+] Selesai. Kumpulan kata disimpan sebagai %s.txt\n" %a

		except IOError, e:

			print(" \n[!] ERROR: %s\n" %e)

	elif wgen == 'ulang':

		jalankan_ulang_program()

	elif wgen == 'keluar':

		print "\033[0m"

		opt=False


