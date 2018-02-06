bill = float(input("Total bill amount? "))
service = input('good or fair or bad: ')
goodtip = float(.20 * bill)
fairtip = float(.15 * bill)
badtip = float(.1 * bill)

goodtotal = float(goodtip + bill)
fairtotal = float(fairtip + bill)
badtotal = float(badtip * bill)

if service == 'good':
    print('tip' + str(goodtip)) 
    print('grandtotal', goodtotal)
if service == 'fair':
    print('tip' + str(fairtip)) 
    print('grandtotal', fairtotal)
if service == 'bad':
    print('tip' + str(badtip)) 
    print('grandtotal', badtip)
