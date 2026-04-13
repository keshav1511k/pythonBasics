# indexing t = accessing the elements of the sequence using [] (indexing operator)
#                 [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[:4]) # till 4th index and start from 0 we also write it as [0:4]
print(credit_number[5:9])
print(credit_number[5:]) # till end from index 5
print(credit_number[-1]) # from last 
print(credit_number[::3]) # from 3 steps 


# exercise 1

credit_number = "1234-5678-9012-3456"

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")


# exercise 2 

credit_number = "1234-5678-9012-3456"
credit_number = credit_number[::-1] # reverse the number
print(credit_number)
