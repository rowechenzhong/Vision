import os
# get string from preamble.sty
prefix = open('preamble.sty').read()

print(prefix[:100])
prefix = "$$\n" + prefix + "\n$$\n"

# iterate over all files in directory
for subdir, dirs, files in os.walk('.'):
    for file in files:
        # print(os.path.join(subdir, file))
        # append prefix to the beginning of each file
        if file.endswith(".md"):
            with open(os.path.join(subdir, file), 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(prefix + content)
