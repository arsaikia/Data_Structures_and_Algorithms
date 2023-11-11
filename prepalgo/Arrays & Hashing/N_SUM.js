// numbersToSum total = 11319
var numbersToSum = [276, 1872, 1345, 1355, 1400, 1300, 1200, 51, 1020, 500, 400, 300, 100, 100, 100];

// targetSums total = 11319
var targetSums = [1627];

// Build a "sum map" from a list of positive integers
// For each sum <= maxtarget, the returned map will provide
// the list of indexes that could be the last number in that sum
// From this map, the complete set of possible sums for any value
// can be easily determined.
function buildSumMap(nums, maxtarget)
{
    //all accessible sums <= maxtarget
    let sumList=[0];
    //for each accessible sum, the indexes of possible final numbers, in order
    let sumMap={
        0:[]
    }
    for (let i=0; i<nums.length; ++i) {
        for (let previ=sumList.length-1; previ>=0; --previ) {
            let newsum = sumList[previ]+nums[i];
            if (newsum <= maxtarget) {
                let list = sumMap[newsum];
                if (!list) {
                    //previously inaccessible sum
                    sumList.push(newsum);
                    list = [];
                    sumMap[newsum] = list; 
                }
                list.push(i);
            }
        }
    }
    return sumMap;
}

// Get all the derivations of a given target sum, using a sum map
// only indexes < indexLimit will be considered
function getSetsThatSum(nums, sumMap, target, indexLimit)
{
    if (target==0) {
        return [[]];
    }
    let list = sumMap[target];
    if (!(list && list.length)) {
        return [];
    }
    let ret=[];
    for (let i=0; i<list.length; i++) {
        let lastindex = list[i];
        if (lastindex >= indexLimit) {
            break;
        }
        let val = nums[lastindex];
        getSetsThatSum(nums, sumMap, target-val, lastindex).forEach(prevsum => {
            ret.push([...prevsum, val]);
        });
    }
    return ret;
}

let sumMap = buildSumMap(numbersToSum, 5000000);

// Store the solutions
var targetSumsSolutions = {};
for (let idx = 0; idx < targetSums.length; idx++) {
  targetSumsSolutions[targetSums[0]] = getSetsThatSum(numbersToSum, sumMap, targetSums[idx], numbersToSum.length)
  
}

console.log(targetSumsSolutions);