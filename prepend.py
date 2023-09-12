import os
# get string from preamble.sty
suffix = open('preamble.sty').read()

print(suffix[:100])
suffix = "\n$$\n" + suffix + "\n$$\n"

# iterate over all files in directory
for subdir, dirs, files in os.walk('.'):
    for file in files:
        # print(os.path.join(subdir, file))
        if file.endswith(".md"):

            # Append suffix to END of file
            with open(os.path.join(subdir, file), 'r') as f:
                text = f.read()
                text = text + suffix

            # write file back
            with open(os.path.join(subdir, file), 'w') as f:
                f.write(text)

            # # if file ends with suffix, remove that suffix.
            # with open(os.path.join(subdir, file), 'r') as f:
            #     text = f.read()
            #     if text.endswith(suffix):
            #         text = text[:-len(suffix)]

            # # write file back
            # with open(os.path.join(subdir, file), 'w') as f:
            #     f.write(text)
