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
    print('Tip Amount: ', (goodtip))
    print('Grand Total: ', goodtotal)
    print('People in party: ', people)
    print('Amount per person:', goodtotal/people)
if service == 'fair':
    print('Tip Amount: ', (fairtip))
    print('Grand Total: ', fairtotal)
    print('People in party: ', people)
    print('Amount per person:', fairtotal/people)
if service == 'bad':
    print('Tip: ', (badtip))
    print('Grand Total: ', badtotal)
    print('People in party: ', people)
    print('Amount per person:', badtotal/people)
