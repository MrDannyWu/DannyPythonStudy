for i in range(1,10):
    for j in range(1,i+1):
        result = '{}×{}='.format(j,i)
        if (j == 2 and i ==3) or (j == 2 and i ==4):
            print( result,i*j,end='  ')
        else:
            print( result,i*j,end=' ')
    print()
