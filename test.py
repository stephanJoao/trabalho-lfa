# from AFD import AFD
from AFN import AFN

if __name__ == "__main__":
    a = AFN.from_xml('../java/AFD.xml')
    input = "baba"
    is_valid = a.parse(input)

    print(f"Input `{input}` is {'' if is_valid else 'not '}valid")
