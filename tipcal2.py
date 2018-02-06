bill = float(input("Total bill amount? "))
service = input('good or fair or bad: ')
goodtip = float(.20 * bill)
fairtip = float(.15 * bill)
badtip = float(.1 * bill)
people = int(input("Split how many ways? "))

goodtotal = float(goodtip + bill)
fairtotal = float(fairtip + bill)
badtotal = float(badtip + bill)

if service == 'good':
    print('tip', (goodtip))
    print('grandtotal', goodtotal)
    print('gandtotal', people)
    print('Amount per person:', goodtotal/people)
if service == 'fair':
    print('tip', (fairtip))
    print('grandtotal', fairtotal)
    print('grandtotal', people)
    print('Amount per person:', fairtotal/people)
if service == 'bad':
    print('tip', (badtip))
    print('grandtotal', badtotal)
    print('grandtotal', people)
    print('Amount per person:', badtotal/people)
