def Kiemtraso():
    a,b = input("Nhap hai so cach khoang trang:").split(' ')
    sobatdau=int(a)
    soketthuc=int(b)
    print(str(a))
    print(str(b))
    if soketthuc<sobatdau:
        print('số kết thúc cần lớn hơn số bắt đầu')
    elif sobatdau<=soketthuc:
        for i in range (sobatdau,soketthuc+1):
            if (sobatdau and soketthuc)%3==0 and (sobatdau and soketthuc)%5==0:
                print('FizzBuzz')
            elif (sobatdau and soketthuc)%3==0:
                print('Fizz')
            elif (sobatdau and soketthuc)%5==0:
                print ('Buzz')
            
if __name__ == "__main__":
    Kiemtraso()
