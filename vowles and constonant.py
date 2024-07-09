def count_vowels_and_consonants(input_string):
   
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0
    for char in input_string:
        if char.isalpha():
            
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    
    return num_vowels, num_consonants

input_statement = "Hello World"
vowels_count, consonants_count = count_vowels_and_consonants(input_statement)
print(f"Number of vowels: {vowels_count}")
print(f"Number of consonants: {consonants_count}")

