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

/*********************< InCorrect -> Below Problem : Sherlock and Anagrams>***********************/

// function sherlockAndAnagrams (s) {
// 	// For strlen 0 or 1 -> No Anaram
// 	const strLen = s.length;
// 	const revStr = s.split('').reverse().join('');
// 	if (strLen < 2) return 0;
// 	let anagram = 0;
// 	const strDict = {};
// 	for (let i = 0; i < strLen; i++) {
// 		if (strDict[s[i]]) {
// 			strDict[s[i]] += 1;
// 		}
// 		else strDict[s[i]] = 1;

// 		let counter = i;
// 		while (counter !== 0) {
// 			if (revStr.includes(s.slice(0, counter + 1))) {
// 				if (strDict[s.slice(0, counter + 1)]) {
// 					strDict[s.slice(0, counter + 1)] += 1;
// 				}
// 				else strDict[s.slice(0, counter + 1)] = 1;
// 				//anagram += 1;
// 				console.log(anagram, strDict, s.slice(0, counter + 1));
// 			}
// 			counter -= 1;
// 		}
// 	}

// 	[ ...Object.keys(strDict) ].forEach((el) => {
// 		anagram += strDict[el] - 1;
// 	});

// 	return anagram;
// }

// console.log(sherlockAndAnagrams('ifailuhkqq'));

/*****************************TBubble Sort**************************/

// function countSwaps (a) {
// 	const bubbleSort = (arr) => {
// 		let swapCounter = 0;
// 		for (let i = 0; i < arr.length; i++) {
// 			for (let j = 0; j < arr.length - i - 1; j++) {
// 				if (arr[j] > arr[j + 1]) {
// 					[ arr[j], arr[j + 1] ] = [ arr[j + 1], arr[j] ];
// 					swapCounter += 1;
// 				}
// 			}
// 		}
// 		return swapCounter;
// 	};

// 	console.log(`Array is sorted in ${bubbleSort(a)} swaps.`);
// 	console.log(`First Element: ${a[0]}`);
// 	console.log(`Last Element: ${a[a.length - 1]}`);
// }

// countSwaps([ 3, 2, 1 ]);

/*****************************Greedy Method**************************/

// function maximumToys (prices, k) {
// 	let currentSpend = 0;
// 	let items = 0;
// 	prices.sort((a, b) => a - b);

// 	for (let i = 0; i < prices.length; i++) {
// 		if (currentSpend + prices[i] <= k) {
// 			currentSpend += prices[i];
// 			items += 1;
// 		}
// 	}

// 	return items;
// }

// console.log(maximumToys([ 1, 12, 5, 111, 200, 1000, 10 ], 50));

/*****************************10 Days of JS**************************/

// function getGrade (score) {
// 	let grade;

// 	if (25 < score && score <= 30) grade = 'A';
// 	if (20 < score && score <= 25) grade = 'B';
// 	if (15 < score && score <= 20) grade = 'C';
// 	if (10 < score && score <= 15) grade = 'D';
// 	if (5 < score && score <= 10) grade = 'E';
// 	if (0 < score && score <= 5) grade = 'F';

// 	return grade;
// }

// console.log(getGrade(29));

/*****************************Dynamic ProgrammingP**************************
*   Given an arry with Integer values and a Target value, find the total 
*   number of digit sum combinations that can result in the Target value
*   E.g.: arr = [1, 2, 4, 6, 9, 10] Target = 16
*   There are 3 ways we can ge 16 => (1+2+4+9), (2+4+10), (6+10)
****************************************************************************/

/*******************Naive Recursion***********************************/
// const twoSumDP = (arr, toIndex, target) => {
//     // Variable to store count
//     let count = 0;
// 	// Return Condition
// 	if (arr[toIndex] === undefined) return 0;
// 	// Increment Count Condition
// 	if (arr[toIndex] === target) return 1;
// 	// Recursve Calls
// 	count += twoSumDP(arr, toIndex - 1, target); // The current element is NOT considered
// 	count += twoSumDP(arr, toIndex - 1, target - arr[toIndex]); // The current element is Considered

// 	return count;
// };

// // Main Execution Context:
// const arr = [ 1, 2, 4, 6, 9, 10 ];
// console.log(twoSumDP(arr, arr.length - 1, 16));

/*******************N MEMOIZATION ***********************************
*   Till a certain toIndex save the count for the Target
*   Use a Dictonary => KEY as  `toIndex : Target`
******************************** ***********************************/

// const twoSumMEMO = (arr, toIndex, target, memoDict) => {
// 	// Variable to store count
// 	let count = 0;
// 	// Return Condition
// 	if (toIndex < 0) return 0;
// 	// Check in Memo
// 	if (memoDict[`${toIndex} : ${target}`]) return memoDict[`${toIndex} : ${target}`];

// 	// Increment Count Condition
// 	if (arr[toIndex] === target) return 1;
// 	// Recursve Calls
// 	count += twoSumMEMO(arr, toIndex - 1, target, memoDict); // The current element is NOT considered
// 	count += twoSumMEMO(arr, toIndex - 1, target - arr[toIndex], memoDict); // The current element is Considered

// 	count ? (memoDict[`${toIndex} : ${target}`] = count) : null;
// 	return count;
// };

// // Main Execution Context:
// const memoDict = {};
// const arr = [ 1, 2, 4, 6, 9, 10 ];
// console.log(twoSumMEMO(arr, arr.length - 1, 16, memoDict));

/*--------------------------------------------------------------------------------------------------------------------------*/
/*   									Sorts -> Bubble, Selection , Insertion												*/
/*--------------------------------------------------------------------------------------------------------------------------*/
/*randomly generated N = 40 length array 0 <= A[N] <= 39*/
// const arr = Array.from({ length: 40 }, () => Math.floor((Math.random() < 0.5 ? -Math.random() : Math.random()) * 50));

/*							Bubble Sort						*/
// const bubbleSort = (array) => {
// 	for (let i = 0; i < array.length; i++) {
// 		for (let j = 1; j < array.length - i; j++) {
// 			array[j - 1] > array[j] ? ([ array[j - 1], array[j] ] = [ array[j], array[j - 1] ]) : null;
// 		}
// 	}

// 	return array;
// };

// console.log(bubbleSort(arr));

/*--------------------------------------------------------------------------------------------------------------------------*/
/*													Selection Sort															*/
// const selectionSort = (array) => {
// 	for (let i = array.length - 1; i > 0; i--) {
// 		let maxIndex = 0;
// 		for (let j = 1; j < i; j++) {
// 			array[maxIndex] < array[j] ? (maxIndex = j) : null;
// 		}

// 		[ array[maxIndex], array[i] ] = [ array[i], array[maxIndex] ];
// 	}

// 	return array;
// };

// let arr = Array.from({ length: 40 }, () => Math.floor((Math.random() < 0.5 ? -Math.random() : Math.random()) * 50));
// console.log(selectionSort(arr));
/*--------------------------------------------------------------------------------------------------------------------------*/

/*--------------------------------------------------------------------------------------------------------------------------*/
/*													Insertion Sort															*/
// const insertionSort = (array) => {
// 	for (let i = 1; i < array.length; i++) {
// 		let maxValue;
// 		let j = i - 1;
// 		while (array[j] > array[i] && j > -1) {
// 			maxValue = array[i];
// 			array[i] = array[j];
// 			j -= 1;
// 		}
// 		array[i] == maxValue;
// 	}

// 	return array;
// };

// let arr = Array.from({ length: 40 }, () => Math.floor((Math.random() < 0.5 ? -Math.random() : Math.random()) * 50));
// console.log(insertionSort(arr));
/*--------------------------------------------------------------------------------------------------------------------------*/

/*--------- 10 Days for JS ------------*/

// function getLetter (s) {
// 	let letter = s.split('')[0];
// 	let ret = null;

// 	if ('aeiou'.includes(letter)) return 'A';
// 	if ('bcdfg'.includes(letter)) return 'B';
// 	if ('hjklm'.includes(letter)) return 'C';
// 	if ('npqrstuvwxyz'.includes(letter)) return 'D';

// 	return ret;
// }

// console.log(getLetter('adfgt'));

/*--------- 2nd Largest Array Element ------------*/

/*--------- O(n ln n) Time ------------*/
// function getSecondLargest (nums) {
// 	nums.sort((a, b) => a - b);
// 	let i = 1;
// 	while (nums[nums.length - i] === nums[nums.length - i - 1]) i += 1;
// 	return nums[nums.length - i - 1];
// }

// console.log(getSecondLargest([ 2, 3, 6, 6, 5, 5, 6, 6, 7, 7 ]));

/*--------- O(n) Time ------------*/
// function getSecondLargest (nums) {
// 	let largest = 0;
// 	let secondLargest = 0;

// 	for (let i = 0; i < nums.length; i++) {
// 		if (nums[i] > largest) {
// 			secondLargest = largest;
// 			largest = nums[i];
// 		}
// 		else if (nums[i] < largest && nums[i] > secondLargest) secondLargest = nums[i];
// 	}

// 	return secondLargest;
// }

// console.log(getSecondLargest([ 2, 3, 6, 6 , 5]));

/*--------- Try Catch ------------*/

// function reverseString (s) {
// 	try {
// 		s = s.split('').reverse().join('');
// 	} catch (error) {
// 		console.log('s.split is not a function');
// 	} finally {
// 		console.log(s);
// 	}
// }

// reverseString('asddasd');
// reverseString(123);

// function simpleArraySum (ar) {
// 	let sum = 0;
// 	ar.forEach((element) => {
// 		sum += element;
// 	});

// 	return sum;
// }

// console.log(simpleArraySum([ 1, 2, 3, 4 ]));

// function compareTriplets (a, b) {
// 	let alice =  0;
// 	let	bob = 0;

// 	for (let i = 0; i < Math.max(a.length, b.length); i++) {
// 		a[i] > b[i] ? (alice += 1) : a[i] < b[i] ? (bob += 1) : null;
// 	}

// 	return [alice, bob];
// }
// console.log(compareTriplets([5,6,7], [3,6,10]));

/*--------- Diagonal Difference ------------*/
// function diagonalDifference (arr) {
// 	let PdiagSum = 0;
// 	let SdiagSum = 0;

// 	for (let i = 0; i < arr.length; i++) {
// 		PdiagSum += arr[i][i];
// 		SdiagSum += arr[i][arr.length - 1 - i];
// 	}

// 	return Math.abs(PdiagSum - SdiagSum);
// }

// console.log(diagonalDifference([ [ 11, 2, 4 ], [ 4, 5, 6 ], [ 10, 8, -12 ] ]));

/*--------- Plus Minus ------------*/

// function plusMinus (arr) {
// 	const myDict = { zero: 0, positive: 0, negative: 0 };

// 	for (let i = 0; i < arr.length; i++) {
// 		if (arr[i] === 0) {
// 			myDict.zero = myDict.zero + 1;
// 		}
// 		else if (arr[i] > 0) {
// 			myDict.positive = myDict.positive + 1;
// 		}
// 		else {
// 			myDict.negative = myDict.negative + 1;
// 		}
// 	}
// 	console.log(parseFloat(myDict.positive / parseFloat(arr.length)).toPrecision(12));
// 	console.log(parseFloat(myDict.negative / parseFloat(arr.length)).toPrecision(12));
// 	console.log(parseFloat(myDict.zero / parseFloat(arr.length)).toPrecision(12));

// }

// plusMinus([ -4, 3, -9, 0, 4, 1 ]);

/*--------- Staircase ------------*/

// function staircase (n) {
// 	for (let i = 1; i < n+1; i++) {
// 		let stairs = '';
// 		let j = i;
// 		let k = i;
// 		while (j !== n) {
// 			stairs += ' ';
// 			j++;
// 		}
// 		while (k !== 0) {
// 			stairs += '#';
// 			k--;
// 		}

// 		console.log(`${stairs}`);
// 	}
// }

// staircase(6);

/*--------- Min-Max Score ------------*/
// function miniMaxSum (arr) {
// 	const myDict = { sum: 0, maxVal: 0, minVal: arr[0] };
// 	arr.forEach((el) => {
// 		myDict.sum += el;
// 		if (el < myDict.minVal) myDict.minVal = el;
// 		if (el > myDict.maxVal) myDict.maxVal = el;
// 	});
// 	console.log(myDict.sum - myDict.maxVal, myDict.sum - myDict.minVal);
// }

// miniMaxSum([ 1, 2, 3, 4, 5 ]);

/*--------- Birthday Cake Candles ------------*/

// function birthdayCakeCandles (arr) {
// 	const myDict = { maxVal: arr[0], count: 0 };

// 	arr.forEach((el) => {
// 		if (el > myDict.maxVal) {
// 			myDict.maxVal = el;
// 			myDict.count = 1;
// 		}
// 		else if (el === myDict.maxVal) myDict.count += 1;
// 	});

// 	return myDict.count;
// }

// console.log(birthdayCakeCandles([ 3, 2, 1, 3 ]));

/*--------- Time Conversion ------------*/
// function timeConversion (s) {
// 	const x = s.includes('PM') ? s.split('PM')[0].split(':') : s.split('AM')[0].split(':');
// 	s.includes('PM') ? x[0]==='12' ? x[0]='12' : (x[0] = parseInt(x[0]) + 12) : null;
// 	s.includes('AM') ? (x[0] === '12' ? (x[0] = '00') : null):null;

// 	return x.join(':');
// }

// console.log(timeConversion('12:45:54PM'));

/*---------  Insertion Sort ------------*/
// function insertionSort1 (n, arr) {
// 	for (let i = 1; i < n; i++) {
// 		let j = i;
// 		let curr = arr[j];
// 		let flag = false;
// 		while (j > 0) {
// 			if (arr[j - 1] > curr) {
// 				arr[j] = arr[j - 1];
// 				flag = true;
// 			}
// 			else flag = false;
// 			j -= 1;

// 			if (flag) {
// 				arr[j] = curr;
// 			}
// 		}
// 		console.log(...arr);
// 	}
// }
// insertionSort1(6, [ 1, 4, 3, 5, 6, 2 ]);

/*---------  Lily's Homework ------------*/
// //          [ 1, 4, 3, 5, 6, 2 ]
// function lilysHomework (arr) {
// 	const ascending = (arr) => {
// 		let ascSwapCounts = 0;

// 		for (let i = 0; i < arr.length; i++) {
// 			let max = 0;
// 			let initVal = arr[0];

// 			for (let j = 1; j < arr.length - i; j++) {
// 				if (arr[j] > arr[max]) {
// 					max = j;
// 				}
// 			}

// 			[ arr[max], arr[arr.length - 1 - i] ] = [ arr[arr.length - 1 - i], arr[max] ];

// 			initVal !== arr[max] ? (ascSwapCounts += 1) : null;
// 		}
// 		return ascSwapCounts;
// 	};

// 	const descending = (arr) => {
// 		let descSwapCounts = 0;

// 		for (let i = 0; i < arr.length; i++) {
// 			let min = 0;
// 			let initVal = arr[arr.length - i - 1];

// 			for (let j = 1; j < arr.length - i; j++) {
// 				if (arr[j] < arr[min]) {
// 					min = j;
// 				}
// 			}

// 			[ arr[min], arr[arr.length - 1 - i] ] = [ arr[arr.length - 1 - i], arr[min] ];
// 			if (initVal !== arr[arr.length - 1 - i]) {
// 				descSwapCounts += 1;
// 			}
// 		}

// 		return descSwapCounts;
// 	};
// 	let arr1 = arr;
// 	const ascSwapCounts = ascending(arr);
// 	const descSwapCounts = descending(arr1);
// 	return Math.min(ascSwapCounts, descSwapCounts);
// }

// console.log(lilysHomework([ 3, 4, 2, 5, 1 ]));

/*
 * Complete the Rectangle function
 */
// function Rectangle(a, b) {
//     const myDict ={};
//     myDict.length = (a);
//     myDict.width = (b);
//     myDict.perimeter = (2*(a+b));
//     myDict.area = (a*b);

//     return myDict;
// }

// let x = Rectangle(4, 5);
// console.log(x);


/*
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 * 
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
// function getCount(objects) {

//     let count =0;

//     objects.forEach( (el) => {
//         if(el.x === el.y) count += 1;
//     })

//     return count;
    
// }

/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */
// function modifyArray(nums) {
//     let n = [];
//     nums.forEach( (el) => {
//         el%2 === 0 ? n.push(el*2) : n.push(el*3);
//     })
//     return n;
// }



/*
 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 * 
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
 */
// function sides(literals, ...expressions) {

//     const x= ( (expressions[1] + Math.sqrt( (expressions[1]*expressions[1]) - (16*expressions[0]))) /4 );
//     const y = ( (expressions[1] - Math.sqrt( (expressions[1]*expressions[1]) - (16*expressions[0]))) /4 );
    
//    return [Math.min(x,y), Math.max(x,y)]
// }
