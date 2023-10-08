import os
# get string from preamble.sty
# prefix = open('preamble.sty').read()

# print(prefix[:100])
# # remove all \n
# prefix = prefix.replace("\n", "")
# prefix = "$" + prefix + "$"

# # prefix = r"""$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$"""

prefix = "\n"

# iterate over all files in directory
for subdir, dirs, files in os.walk('.'):
    for file in files:
        # print(os.path.join(subdir, file))
        if file.endswith(".md"):
            print("Prepending file: " + os.path.join(subdir, file))

            # Append prefix to front of file
            # with open(os.path.join(subdir, file), 'r') as f:
            #     text = f.read()
            #     text = prefix + text

            # # write file back
            # with open(os.path.join(subdir, file), 'w') as f:
            #     f.write(text)

            # if file ends with prefix, remove that prefix.
            with open(os.path.join(subdir, file), 'r') as f:
                text = f.read()
                if text.startswith(prefix):
                    print("Removing prefix from file: " +
                          os.path.join(subdir, file))
                    text = text[len(prefix):]

            # write file back
            with open(os.path.join(subdir, file), 'w') as f:
                f.write(text)
