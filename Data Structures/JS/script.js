// function sockMerchant (arr) {
// 	let pairs = 0;
// 	const myDict = {};

// 	arr.forEach((el) => {
// 		if (myDict[el]) {
// 			if (myDict[el] === 1) {
// 				pairs += 1;
// 				myDict[el] = 0;
// 			}
// 			else {
// 				myDict[el] = 1;
// 			}
// 		}
// 		else {
// 			myDict[el] = 1;
// 		}
// 	});

// 	return pairs;
// }

// console.log(sockMerchant([ 10, 20, 20, 10, 10, 30, 50, 10, 20 ]));

// function countingValleys (n, s) {
// 	let currValue = 0;
// 	let valleyCount = 0;

// 	for (const el of s) {
// 		if (el === 'D' && currValue === 0) {
// 			valleyCount += 1;
// 			currValue -= 1;
// 		}
// 		else if (el === 'U') currValue += 1;
// 		else currValue -= 1;
// 	}

// 	return valleyCount;
// }

// console.log(countingValleys(8, 'UDDDUUDUDUU'));

// // // // Jumping on the Clouds

// function jumpingOnClouds (cloudsArray) {
// 	let steps = 0;

// 	for (let index = 0; index < cloudsArray.length; index++) {
// 		if (cloudsArray[index + 2] === 0) {
// 			index = index + 1;
// 			steps += 1;
// 		}
// 		else if (cloudsArray[index + 1] === 0) {
// 			steps += 1;
// 		}
// 	}

// 	return steps;
// }

// console.log(jumpingOnClouds([ 0, 0, 1, 0, 0, 1, 0 ]));

// Approach 1: works with small size of strings
// function repeatedString (s, n) {
// 	const initialStr = s;
// 	let aCount = 0;

// 	while (s.length < n) s += initialStr;
// 	s = s.slice(0, n + 1);
// 	for (const c of s) {
// 		c === 'a' ? (aCount += 1) : null;
// 	}
// 	return aCount;
// }

// console.log(repeatedString('aba', 10));

// Approach 2: Efficient and works always (No heap out of memory error)
// function repeatedString (s, n) {
// 	const initialElements = [ ...s.slice(0, n % s.length) ].filter((el) => el == 'a').length;
// 	const repeat = [ ...s ].filter((el) => el == 'a').length * (s.length < n ? parseInt(n / s.length) : 0);
// 	return initialElements + repeat;
// }

// console.log(repeatedString('aba', 10));

// function hourglassSum (arr) {
// 	let max = -99;
// 	for (let i = 0; i < Math.ceil(arr.length / 2) + 1; i++) {
// 		for (let j = 0; j < Math.ceil(arr.length / 2) + 1; j++) {
// 			const hourGlass =
// 				arr[i][j] +
// 				arr[i][j + 1] +
// 				arr[i][j + 2] +
// 				arr[i + 1][j + 1] +
// 				arr[i + 2][j] +
// 				arr[i + 2][j + 1] +
// 				arr[i + 2][j + 2];
// 			hourGlass > max ? (max = hourGlass) : null;
// 		}
// 	}
// 	return max;
// }

// const arr = [
// 	[ -9, -9, -9, 1, 1, 1 ],
// 	[ 0, -9, 0, 4, 3, 2 ],
// 	[ -9, -9, -9, 1, 2, 3 ],
// 	[ 0, 0, 8, 6, 6, 0 ],
// 	[ 0, 0, 0, -2, 0, 0 ],
// 	[ 0, 0, 1, 2, 4, 0 ]
// ];
// console.log(hourglassSum(arr));

// function rotLeft (arr, d) {
// 	const shifts = d % arr.length;
// 	shifts !== 0 ? arr.push(...arr.splice(0, shifts)) : null;

// 	return arr;
// }

// const arr = [ 1, 2, 3, 4, 5 ];

// console.log(rotLeft(arr, 4));

// function minimumBribes(q) {

//     let bribes = 0, i, j;

//     for (let i = 0; i < q.length; i++) {
//         const pos = q[i], at = i + 1;
//         if (pos - at > 2) { return "Too chaotic" }
//         for (j = pos - 2; j < i; j++) {
//             if (q[j] > pos) { bribes++ }
//         }
//     }
//     return bribes;
// }

// console.log(minimumBribes([ 1, 2, 5, 3, 7, 8, 6, 4 ]));

//-------------Day 2----------------------------.to

// Complete the beautifulDays function below.
// function beautifulDays (i, j, k) {

//     let beautifulDaysCount = 0;
    
// 	for (let day = i; day < j + 1; day++) {
        
//         (Math.abs(day - day.toString(10).split('').reverse().join('')) % k) === 0 ? beautifulDaysCount+=1 : null;
        
// 	}

// 	return (beautifulDaysCount);
// }

// console.log(beautifulDays(20, 23, 6));


const factorial = (n) => {

    if(n===0 || n===1) return 1

    return n*(factorial(n-1))
}

console.log(factorial(3))
