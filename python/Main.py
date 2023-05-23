from AFD import AFD
from AFN import AFN

class Main:
    def main(self):
        t = Main()
        t.faca1("ababa")
        # t.faca2()

    def faca1(self, w):
        a = AFD()
        try:
            a.ler("../java/AFD.xml")
            print("AFD M =", a)
            if a.aceita(w):
                print("Aceitou", w)
            print("Pe(q0, {}):".format(w), a.pe(a.getEstadoInicial(), w))
        except Exception as e:
            print(e)

    def faca2(self):
        a = AFN()
        try:
            a.ler("../java/AFN01.xml")
            print("AFN M =", a)
            print(("AFD M' =", a.toAFD()).toString())
        except Exception as e:
            print(e)


if __name__ == "__main__":
    # print(AFN.AFN())
	t = Main()
	t.main()