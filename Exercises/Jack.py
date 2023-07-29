Sample_String = "1234abcd"
def reverse_strings():
    ns = ""
    nsa = len(Sample_String)
    for n in range(nsa):
        ns += Sample_String[nsa -1]
        nsa = nsa - 1
    return ns

print(reverse_strings())