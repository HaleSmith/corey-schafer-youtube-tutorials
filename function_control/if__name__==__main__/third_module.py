# References https://www.youtube.com/watch?v=sugvnHA7ElY


# Will only print if this .py file is run directly
def main():
    print(f"Third Module's Name: {__name__}, run directly")


print("\n --- {Print __name__ for third module} ---\n")
if __name__ == '__main__':
    main()
else:
    print(f"Third Module's Name: {__name__}, imported")