#USD to MXN,Eruo Conveter
#welcome screen with usd and mxn or eruo converter 
#options usd to mxn.eruo to mexican,eruo to usd,usd to eruo,mxn to eruo and have an exit option
#which ever option chosen show screen of input ex amount _ to ex
#converting...
#shoots out in ex: amount
#loop back to to options
def welcome_menu():
	print()
	print("Welcome to my USD,MXN,Eruo Converter")
	print()
def currenncy_menu():
	print("Choose your Currenny:")
	print("1. USD")
	print("2. Euro")
	print("3. MXN")
	print("4.Exit")

def USD_MXN_cnvrt(n1):
	print("MXN:")
	print(20.1125 * n1)

def USD_Euro_cnvrt(n1):
	print("Euro:")
	print(0.961544 * n1)

def MXN_USD_cnvrt(n1):
	print("USD:")
	print(0.0497162 * n1)

def MXN_Euro_cnvrt(n1):
	print("Euro:")
	print(0.0477963 * n1)

def Euro_USD_cnvrt(n1):
	print("USD:")
	print(1.03993  * n1)

def Euro_MXN_cnvrt(n1):
	print("MXN:")
	print(20.9230 * n1)	

def USD_opt(): 
	usd_ans=input("USD to ")
	if usd_ans== "MXN":
		USD_MXN_cnvrt(int(input("USD:$")))
	elif usd_ans == "Euro":
		USD_Euro_cnvrt(int(input("USD:$")))
	else:
		print("Invalid answer words only")



def MXN_opt():
	mxn_ans=input("MXN to ")
	if mxn_ans == "USD":
		MXN_USD_cnvrt(int(input("MXN:")))
	elif mxn_ans == "Euro":
		MXN_Euro_cnvrt(int(input("MXN:"))) 
	else:
		print("Invalid answer words only")

def Euro_opt():
	eruo_ans=input("Euro to ")
	if eruo_ans == "MXN":
		Euro_MXN_cnvrt(int(input("Euro:")))
	elif eruo_ans == "USD":
		Euro_USD_cnvrt(int(input("Euro:")))
	else:
		print("Invalid answer words only")



def Exit_opt():
	print("Have a nice day")
	exit()


if __name__ == "__main__":
	welcome_menu()
while True:
	currenncy_menu()
	currency_answer=input(":")
	if currency_answer == "1":	
		USD_opt()
	elif currency_answer == "2":
		Euro_opt()
	elif currency_answer == "3":
		MXN_opt()
	elif currency_answer == "4":
		Exit_opt()
	else:
		print("Invalid answer only numbers show on the screen")







