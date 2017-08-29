


def devide(k):
    while True:
        for i in range(2,k):
            value=k/i
            if value.is_integer():
                print(value)
                break

    return [devide(value),devide(i)]



if __name__=='__main__':
    print(devide(int(input('What do you want to find'))))