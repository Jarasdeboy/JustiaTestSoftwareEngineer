## Question 7: Big O notation

Do you know what is the Big O notation for this function?

```javascript
function pairMultiplications(numbers) {
    console.log('these are the numbers: ')
    numbers.forEach(function (number) {
        console.log(number);
    });

    console.log('and these are their multiplications: ')
    numbers.forEach(function (firstNumber) {
        numbers.forEach(function (secondNumber) {
            console.log(firstNumber * secondNumber);
        });
    });
}

pairMultiplications([1,2,3,4,5]);
```

### Answer

  

