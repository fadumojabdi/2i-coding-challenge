from find_max_sum import finding_max_digit_sum

def test_happy_path():
    inputs = ["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]
    output_is = finding_max_digit_sum(inputs)
    assert output_is == 13
    print(f"Passed! Your maximum sum is: {output_is}")


def test_negative_case():
    inputs = ["rgf", "fjghgvgh", "aaaaa"]
    output_is = finding_max_digit_sum(inputs)
    assert output_is == 0
    print("negative test pass!")



print("we are running your tests...")
test_happy_path()
test_negative_case()
print("All your tests passed!")
