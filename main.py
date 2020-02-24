def FizzBuzz():
    list_of_answers = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            list_of_answers.append('FizzBuzz')
        elif num % 3 == 0:
            list_of_answers.append('Fizz')
        elif num % 5 == 0:
            list_of_answers.append('Buzz')
        else:
            list_of_answers.append(num)

    return list_of_answers
    
print(FizzBuzz())