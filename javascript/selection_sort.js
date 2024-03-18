function selectionSort(arr) {
  let sortedArr = arr.sort((a, b) => a - b)
  return sortedArr
}

if (require.main === module) {
  // add your own tests in here
  console.log("Expecting: [-1, 2, 3, 5]");
  console.log("=>", selectionSort([3, -1, 5, 2]));

  console.log("");

  console.log('Expecting: [-12, -10, -5, 0 , 1 , 10 , 345')
  console.log('=>', selectionSort([10, 345, -12, 1, -5, 0, -10]))

  // BENCHMARK HERE, and print the average runtime
  let startTime = Date.now();
  const longInput = [];

  for (let i = 0; i < 100; ++i) {
    longInput.push(Math.floor(Math.random() * 100));
  }

  
  // Run the sort 1000 times for both a small and a large input
  for (let i = 0; i < 1000; ++i) {
    selectionSort([3, -1, 5, 2]);
    selectionSort(longInput);
  }

  let endTime = Date.now();
  let averageRuntime = (endTime - startTime) / 2000; // Divide by 2000 because we ran it 1000 times for 2 inputs
  console.log("Average Runtime: ", averageRuntime, "ms");
}

module.exports = selectionSort;

// Please add your pseudocode to this file
// And a written explanation of your solution

// Function selectionSort takes an array 'arr' of integers:
//   1. Use the 'arr.sort()' method with a compare function:
//      - The compare function takes two arguments 'a' and 'b'
//      - Return 'a - b' to ensure numerical ascending order sorting
//   2. Return the sorted array 'arr'

// BenchMark psuedocode

// 1. Initialize 'startTime' with the current time
// 2. Create an empty array named 'longInput'

// 3. Loop 100 times to fill 'longInput':
//    a. Generate a random number using 'Math.random()', multiply by 100
//    b. Round the generated number to the nearest whole number using 'Math.floor()'
//    c. Add the rounded number to 'longInput'

// 4. Loop 1000 times to perform sorting:
//    a. Sort a small static array (e.g., [3, -1, 5, 2]) using the selectionSort function
//    b. Sort 'longInput' using the selectionSort function

// 5. Initialize 'endTime' with the current time after the loop ends

// 6. Calculate 'averageRuntime':
//    a. Subtract 'startTime' from 'endTime' to find the total elapsed time
//    b. Divide the total elapsed time by 2000 (since we performed 2000 sorts in total, 1000 on a small array and 1000 on 'longInput')

// 7. Print 'averageRuntime' to the console
