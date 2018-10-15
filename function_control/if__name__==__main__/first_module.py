# References https://www.youtube.com/watch?v=sugvnHA7ElY
# When Python runs a file, it first sets a few special variables
# When a file is run directly, __name__ is set to main
# When a file is imported, __name__ is set to the name of the file


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Print __name__ for first module")

# This prints as __name__ when first_module is run
# This prints as first_module when second_module is run
print(f"First Module's Name: {__name__}")

