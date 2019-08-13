import os, sys


username = 'Contoh'      

password = 'Tutorial'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mLogin Sukses", 

			sys.exit()



		else:

			print "\033[1;32mPassword Salah"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;32mUsername Salah"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()