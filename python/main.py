from AFD import AFD
# from AFN import AFN

# def processamento_por_afn():
#     a = AFN()
#     try:
#         a.ler("../java/AFN01.xml")
#         print("AFN M =", a)
#         print(("AFD M' =", a.toAFD()).toString())
#     except Exception as e:
#         print(e)

def processamento_por_afd(w):
    afd = AFD()
    try:
        afd.ler("../java/AFD.xml")
        print("AFD M =", afd)
        if afd.aceita(w):
            print("Aceitou", w)
        print(f"Pe(q0, {w}):", afd.pe(afd.getEstadoInicial(), w))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    processamento_por_afd('ababa')
