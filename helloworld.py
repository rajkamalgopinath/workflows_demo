import sys

def main():
    print("Hello World! From Python: " + str(sys.version_info))
    if sys.version_info >= (3, 6) and sys.version_info < (3, 7):
        print("No exceptions raised")
if __name__ == "__main__":
    main()
