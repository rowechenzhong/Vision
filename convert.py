def convert(FILE_IN, FILE_OUT):

    """
    This script will convert
    one of my LaTeX documents
    into an md file for Obsidian.
    """

    with open(FILE_IN, "r") as f:
        lines = f.readlines()

    # Trim all tabs from the beginning of each line
    lines = [line.lstrip() for line in lines]
    # Delete everything after % symbols
    lines = [line.split("%")[0] for line in lines]

    text = "".join(lines)

    # Delete everything before \begin{document}
    try:
        text = text[text.find(r"\begin{document}")+len(r"\begin{document}"):]
    except:
        pass
    text = text.replace(r"\[", r"$$")
    text = text.replace(r"\]", r"$$")
    text = text.replace(r"``", r"\"")
    text = text.replace(r"''", r"\"")
    text = text.replace(r"`", r"'")

    """
    I want to: replace all \textbf{} with ** **
    replace all \textit{} with * *
    replace all \emph{} with * *
    replace all \vocab{} with ==** **==

    remove all all \begin{enumerate} and \begin{itemize}
    change all \item to -
    remove all all \end{enumerate} and \end{itemize}
    """

    SEARCH = {
        r"\textbf{": ["}", "**", "**"],
        r"\textit{": ["}", "*", "*"],
        r"\emph{": ["}", "*", "*"],
        r"\vocab{": ["}", "==**", "**=="],
        r"\cond{"   : ["}", "==*", "*=="],
        r"\section{": ["}", "\n# ", "\n\n"],
        r"\subsection{": ["}", "\n## ", "\n\n"],
        r"\subsubsection{": ["}", "\n### ", "\n\n"],
        r"\begin{enumerate}": [r"\end{enumerate}", "\n", "\n"],
        r"\begin{itemize}": [r"\end{itemize}", "\n", "\n"],
        r"\item": ["", "\n\n- ", "", ""]
    }

    for key in SEARCH:
        i = 0
        while i < len(text):
            if(text[i:i+len(key)] == key):
                prefix = text[:i] + SEARCH[key][1]
                suffix = text[i+len(key):].replace(SEARCH[key][0], SEARCH[key][2], 1) # replace first instance of }
                text = prefix + suffix
            i += 1


    lines = text.split("\n")

    # Remove all \n from the end of each line, unless it is a blank line
    lines = [line.rstrip() + " " if line != "" else "\n" for line in lines]

    text = "".join(lines)


    """
    idea{} and todo{} are special.
    """
    SEARCH_SHORT_ENV = {
        "idea" : "idea",
        # "todo" : "todo"
    }
    for KEY in SEARCH_SHORT_ENV:

        # KEY = r"\idea{"
        RKEY = "\\" + KEY + "{"
        i = 0
        while i < len(text):
            if(text[i:i+len(RKEY)] == RKEY):
                prefix = text[:i] + "\n> [!" + KEY + "] \n"
                suffix = text[i+len(RKEY):]
                # parse to endkey while keeping track of brackets
                inside = ""
                brackets = 0
                for j in range(len(suffix)):
                    if(suffix[j] == "{"):
                        brackets += 1
                    elif(suffix[j] == "}"):
                        brackets -= 1
                    if(brackets == -1):
                        outside = suffix[j+1:]
                        break
                    inside += suffix[j]
                # Prefix all lines in inside with "> "
                inside = inside.replace("\n", "\n> ")
                # Add some newlines
                inside = inside + "\n\n"
                outside = outside + "\n\n"
                text = prefix + inside + outside
            i += 1

    """
    Environments are more difficult. They are of the form
    \begin{theorem}
        [Theorem name]
        Contents
    \end{theorem}

    And I want to change this to

    > [!theorem] Theorem name
    > Contents

    """
    SEARCH_ENV = {
        "defn" : "[!definition] ",
        "definition" : "[!definition] ",
        "thm" : "[!theorem] ",
        "theorem" : "[!theorem] ",
        "prob": "[!problem] ",
        "psec*": "[!part]- ",
        "psec": "[!part]- ",
        "problem": "[!problem] ",
        "hsolution": "[!solution]- ",
        "solution": "[!solution]- ",
        "proof": "[!proof]- ",
        "example": "[!example] ",
        "notation*": "[!notation] ",
        "notation": "[!notation] ",
    }

    for key in SEARCH_ENV:
        BEGINKEY = r"\begin{" + key + "}"
        ENDKEY = r"\end{" + key + "}"
        i = 0
        while i < len(text):
            if(text[i:i+len(BEGINKEY)] == BEGINKEY):
                prefix = text[:i] + "\n> " + SEARCH_ENV[key]
                suffix = text[i+len(BEGINKEY):]

                # Check if there is a [name] after the \begin{key}
                # Find first [
                try:
                    firstBracket = suffix.find("[")
                    beforeBracket = suffix[:firstBracket]
                    if(beforeBracket.strip() == ""):
                        suffix = suffix[firstBracket:]
                        # There is a [name]
                        # Find the next ]
                        firstBracket = suffix.find("]")
                        name = suffix[1:firstBracket]
                        # Remove the name from the suffix
                        suffix = suffix[firstBracket+1:]
                        # Add the name to the prefix
                        prefix = prefix[:-1] + " " + name
                except:
                    continue
                prefix += "\n"

                # Find all lines before the \end{key}
                inside = suffix[:suffix.find(ENDKEY)]
                outside = suffix[suffix.find(ENDKEY):]
                # Prefix all lines in inside with "> "
                inside = inside.replace("\n", "\n> ")
                # Add some newlines
                inside = inside + "\n\n"
                # Remove the \end{key}
                outside = outside[len(ENDKEY):] + "\n\n"
                text = prefix + inside + outside
            i += 1


    with open(FILE_OUT, "w") as f:
        f.write(text)

if __name__ == "__main__":
    files = [
        "integration",
        "Lp",
        "measure"
    ]
    for file in files:
        FILE_IN = r'C:\Users\rowec\Dropbox (MIT)\Notes\Math\Measure' + '\\' + file + ".tex"
        FILE_OUT = r'C:\Users\rowec\Documents\GitHub\Vision\measure' + '\\' + file + ".md"
        convert(FILE_IN, FILE_OUT)