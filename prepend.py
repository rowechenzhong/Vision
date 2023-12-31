import os
# get string from preamble.sty
prefix = open('preamble.sty').read()

print(prefix[:100])
# remove all \n
prefix = prefix.replace("\n", "")
prefix = "$" + prefix + "$\n"


# prefix = "\n"

# iterate over all files in directory
for subdir, dirs, files in os.walk('.'):
    for file in files:
        # print(os.path.join(subdir, file))
        if file.endswith(".md"):
            print("Prepending file: " + os.path.join(subdir, file))

            # # Append prefix to front of file
            # with open(os.path.join(subdir, file), 'r') as f:
            #     text = f.read()
            #     text = prefix + text

            # # write file back
            # with open(os.path.join(subdir, file), 'w') as f:
            #     f.write(text)

            # if file begins with prefix, remove that prefix.
            with open(os.path.join(subdir, file), 'r') as f:
                text = f.read()
                if text.startswith(prefix):
                    print("Removing prefix from file: " +
                          os.path.join(subdir, file))
                    text = text[len(prefix):]

            # write file back
            with open(os.path.join(subdir, file), 'w') as f:
                f.write(text)
