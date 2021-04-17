n = 0
s = 0
while (n < 1001):
    x = n/3
    if isinstance(x, (int, long)):
        print 'Multiple of 3!'
        s = s + n
    if False:
        y = n/5
        if isinstance(y, (int, long)):
            s = s + n
    print 'Number: '
    print n
    print 'Sum:'
    print s
    n = n + 1