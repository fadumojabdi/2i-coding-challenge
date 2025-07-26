def finding_max_digit_sum(inputs):
    max_sum = 0
    for text in inputs:
        current_sum = 0
# adding up all the digits in the string
        for char in text:
            if char.isdigit():
                current_sum += int(char)

#keeing track of the maximum sum
        if current_sum > max_sum:            
            max_sum = current_sum
    
    return max_sum   

#run and can adjust inputs as required
inputs = [ "dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw" ]
output_is = finding_max_digit_sum(inputs)
print(f"The maximum digit sum is: {output_is}")