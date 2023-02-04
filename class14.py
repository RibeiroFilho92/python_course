verify_nine_numb_cpf = "746.824.890-7"
multipliers_per_digit = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

verify_nine_numb_cpf_has_dot = verify_nine_numb_cpf.find(".") or verify_nine_numb_cpf.find("-")

if verify_nine_numb_cpf_has_dot:
    verify_nine_numb_cpf = verify_nine_numb_cpf.replace(".", "")
    verify_nine_numb_cpf = verify_nine_numb_cpf.replace("-", "")

for ind, val in enumerate(verify_nine_numb_cpf):
    multipliers_per_digit[ind] = int(val) * multipliers_per_digit[ind]

sum_of_multipliers_per_digit = 0

for value in multipliers_per_digit:
    sum_of_multipliers_per_digit += value

sum_of_multipliers_per_digit *= 10
sum_of_multipliers_per_digit %= 11

second_digit_cpf = sum_of_multipliers_per_digit > 9 if 0 else sum_of_multipliers_per_digit

print(second_digit_cpf)