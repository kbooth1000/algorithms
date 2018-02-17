###  Find the largest palindromic number 
###  made from the product of two 3-digit numbers.


# multiply 999 by 999 -=1...0, then 998 by 998 -=1...0, etc.
# eval if list(str(product)) = reverse(list(str(product)))

finish = False
palindromic_num = 0
palindromic_factor_1 = 0
palindromic_factor_2 = 0
for factor_1 in range(999, 99, -1):
    for factor_2 in range (999, 99, -1):
        num = factor_1 * factor_2
        num_str = str(num)
        if num_str == num_str[ : : -1]:
            if num > palindromic_num:
                palindromic_num = num
                palindromic_factor_1 = factor_1
                palindromic_factor_2 = factor_2
print '*****  %d * %d = %d' % (palindromic_factor_1, palindromic_factor_2, palindromic_num)