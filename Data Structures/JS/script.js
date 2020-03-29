// /*****************************Sock Merchant**************************/
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

// /*****************************JCounting Valleys**************************/
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

// /*****************************Jumping on the Clouds**************************/

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

// /*****************************Repeated Strings**************************/
// //// Approach 1: works with small size of strings
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

// // Approach 2: Efficient and works always (No heap out of memory error)
// function repeatedString (s, n) {
// 	const initialElements = [ ...s.slice(0, n % s.length) ].filter((el) => el == 'a').length;
// 	const repeat = [ ...s ].filter((el) => el == 'a').length * (s.length < n ? parseInt(n / s.length) : 0);
// 	return initialElements + repeat;
// }

// console.log(repeatedString('aba', 10));

// /*****************************Hour Glass**************************/
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

// const arr1 = [ 1, 2, 3, 4, 5 ];

// console.log(rotLeft(arr1, 4));

// /*****************************Minimum Bribes**************************/
// function minimumBribes (q) {
// 	let bribes = 0,
// 		i,
// 		j;

// 	for (let i = 0; i < q.length; i++) {
// 		const pos = q[i],
// 			at = i + 1;
// 		if (pos - at > 2) {
// 			return 'Too chaotic';
// 		}
// 		for (j = pos - 2; j < i; j++) {
// 			if (q[j] > pos) {
// 				bribes++;
// 			}
// 		}
// 	}
// 	return bribes;
// }

// console.log(minimumBribes([ 1, 2, 5, 3, 7, 8, 6, 4 ]));

// /*****************************Beautiful Days**************************/
// function beautifulDays (i, j, k) {
// 	let beautifulDaysCount = 0;

// 	for (let day = i; day < j + 1; day++) {
// 		Math.abs(day - day.toString(10).split('').reverse().join('')) % k === 0 ? (beautifulDaysCount += 1) : null;
// 	}

// 	return beautifulDaysCount;
// }

// console.log(beautifulDays(20, 23, 6));

// /*****************************Factorial**************************/
// const factorial = (n) => {
// 	if (n === 0 || n === 1) return 1;

// 	return n * factorial(n - 1);
// };

// console.log(factorial(3));

// /*****************************Vowels and Consonants**************************/
// function vowelsAndConsonants (s) {
// 	const vowels = [ 'a', 'e', 'i', 'o', 'u' ];
// 	let printVowels = [];
// 	let printConsts = [];

// 	[ ...s ].forEach((ch) => {
// 		vowels.includes(ch) ? printVowels.push(ch) : printConsts.push(ch);
// 	});

// 	[ ...printVowels, ...printConsts ].forEach((el) => console.log(el));
// }

// vowelsAndConsonants('abcdefgh');

// /*****************************MINIMUM SWAPS 2*********************************
// *   You are given an unordered array consisting of consecutive integers
// *   [1, 2, 3, ..., n] without any duplicates. You are allowed to swap
// *   any two elements. You need to find the minimum number of swaps required
// *   to sort the array in ascending order.
// ******************************************************************************/

// const array1 = [ 4, 3, 1, 2 ];
// const array2 = [ 1, 3, 5, 2, 4, 6, 7 ];

// function minimumSwaps (arr) {
// 	// Find the Min element
// 	let min = arr[0];
// 	arr.forEach((el) => (el < min ? (min = el) : null));
// 	// Logic starts here
// 	let swaps = 0;
// 	let toSwap = true;
// 	arr.forEach((el, i) => {
// 		let curr = el;
// 		while (curr !== i + min && toSwap) {
// 			//console.log(i + min, curr);
// 			[ arr[curr - min], arr[i] ] = [ arr[i], arr[curr - min] ];
// 			swaps += 1;
// 			curr = arr[i];
// 			curr === i + min ? !toSwap : null;
// 		}
// 	});

// 	return swaps;
// }

// console.log(minimumSwaps([ 1, 3, 5, 2, 4, 6, 7 ]));

/*****************************Ransom**************************/
// function checkMagazine (magazine, note) {
// 	const magWordsArr = magazine.split(' ');
// 	const ranWordsArr = note.split(' ');

// 	/* Initial Check*/
// 	if (magWordsArr.length < ranWordsArr.length) return 'No';

// 	/* Make Magazine words dict with count as Val and element as key*/
// 	const mDict = {};
// 	magWordsArr.forEach((el) => {
// 		if (mDict[el]) mDict[el] = mDict[el] + 1;
// 		else mDict[el] = 1;
// 	});

// 	/*Chech for words in ransonNote array*/
// 	for (let i = 0; i < ranWordsArr.length; i++) {
// 		const el = ranWordsArr[i];
// 		if (mDict[el] && mDict[el] !== 0) {
// 			mDict[el] = mDict[el] - 1;
// 		}
// 		else return 'No';
// 	}

// 	return 'Yes';
// }

// console.log(checkMagazine('two times three is not four', 'two times two is four'));
// console.log(checkMagazine('give me one grand today night', 'give one grand today'));

/*****************************Two Strings**************************/
//Approach-1
// function twoStrings (s1, s2) {
// 	let contains = 'No';
// 	for (const ch of s1) {
// 		s2.includes(ch) ? (contains = 'Yes') : null;
// 	}
// 	return contains;
// }
// console.log(twoStrings('hello', 'world'));

//Approach-2 : Using Sets
// function twoStrings (s1, s2) {
// 	return new Set([ ...s1 ].filter((el) => s2.includes(el))).size ? 'YES' : 'NO';
// }
// console.log(twoStrings('hello', 'world'));
// console.log(twoStrings('hi', 'world'));

/*******************************************************/
