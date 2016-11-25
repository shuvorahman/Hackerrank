# day 8 : Dictonaries and Map

# Enter your code here. Read input from STDIN. Print output to STDOUT

entry = int(raw_input().strip())
phone_book = dict()
for i in range(entry):
    data = raw_input().strip().split(' ')
    if data:
        phone_book[data[0]] = data[1]
while True:
    try:
        data = raw_input().strip()
        if data in phone_book:
            print data + '=' + phone_book[data]
        else:
            print 'Not found'
    except EOFError:
        break