
def mmc(x,y):
    """Função que acha o minimo multiplo
    comum de 2 numeros"""
    mmc = x
    while mmc%y!=0:
        mmc=mmc+x
    return mmc
def main():        
    num1 = 37
    num2 = 49
    num3 = 2

    valor_base = mmc(num1,mmc(num2,num3))
    i=1
    while valor_base<5000000:
        valor_base=valor_base/i
        i=i+1
        valor_base = valor_base*i

    print(i-1,"numeros")
main()