expen=int(input('Total amount for cloths and FA purchased....\n'))

if expen>25000:
    disc=(expen*20)/100
else:
    disc=(expen*5)/100

billing_amount=expen-disc

print('the final bill1 is '+str(billing_amount))
print('the final bill2 is ',billing_amount)

print('the final bill amount is {} and discount is {} '.format(billing_amount,disc))





