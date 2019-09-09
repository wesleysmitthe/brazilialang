#!/usr/bin/python3
#--*-- encoding: utf-8 --*--

import sys

reservedWordsBLToPy = {
    "desviaGrana":"if",
    "superFaturamento":"elif",
    "caixa2":"else",
    "novaPolitica":"True",
    "enganeiOBoboNaCascaDoOvo":"False",
    "funcionarioFantasma":"None",
    "naCueca":"in",
    "souHonesto":"is",
    "nepotismoDeBoas":"and",
    "aGenteVerOQueFaz":"not",
    "nepotismoCruzado":"or",
    "lavaTudoPaNois":"for",
    "peloPovoBrasileiro":"while",
    "vamoPraBangu":"break",
    "abreMaisUmaLicitacao":"continue",
    "elegeOutroPraGente":"def",
    "Laranja":"return",
    "distribuiSantin": "print",
    "doacaoAnonima": "input",
    "partido": "from",
    "doPovo": "import",
    "globalismo": "global",
    "sucatiar": "try",
    "tudo": "except"}

if len(sys.argv) == 2 or (len(sys.argv) == 3 and sys.argv[2] == "-o"):
    BraziliaLangFile = open(sys.argv[1], "r")

    codePyToExec = "#!/usr/bin/python3\n"
    codePyToExec += "#--*-- coding: utf-8 --*--\n\n"

    for line in BraziliaLangFile.readlines():
        for brasiliaWord in reservedWordsBLToPy.keys():
            if brasiliaWord in line:
                line = str(line).replace(brasiliaWord, reservedWordsBLToPy[brasiliaWord])

        codePyToExec += line

    if "-o" in sys.argv: 
        with open("saidaBrasiliaLangToPython.py",
         "w") as out:
            out.writelines(codePyToExec)
    
    exec(codePyToExec)
    