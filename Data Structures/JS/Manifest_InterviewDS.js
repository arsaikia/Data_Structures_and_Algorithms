/*---------  Manifest Interview ------------*/
function isValid (str) {
	let given = str.split('');

	if (given[0] === ')') return false;

	let stackVar = [];

	for (let i = 0; i < given.length; i++) {
		if (given[i] === '(') {
			stackVar.push('(');
		}
		if (given[i] === ')') stackVar.pop();
	}

	return stackVar.length !== 0 ? false : true;
}

console.log(isValid('(())'));
