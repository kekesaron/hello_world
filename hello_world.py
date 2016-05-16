import sys

def main(argv):
	if (len(argv)>0):
		print("Hello "+' '.join(argv)+"!")
	else:
		print("Hello world!")

if __name__ == "__main__":
    main(sys.argv[1:])
