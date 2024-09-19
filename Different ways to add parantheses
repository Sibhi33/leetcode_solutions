/**
 * @param {string} expression
 * @return {number[]}
 */

const memo = {};

const OPERATIONS = {
  '-': (x, y) => x - y,
  '+': (x, y) => x + y,
  '*': (x, y) => x * y
};

var diffWaysToCompute = function(expression) {
  return dfs(expression);
};

// Recursive function to compute all possible results from the input expression.
function dfs(exp) {
  // If the result of this subexpression is already computed, return it.
  if (memo[exp]) {
    return memo[exp];
  }

  const results = [];

  // Check if the expression is a simple number.
  if (isNumber(exp)) {
    results.push(parseInt(exp));
    return results;
  }

  // Iterate over each character of the expression.
  for (let i = 0; i < exp.length; i++) {
    const c = exp[i];
    
    // Check if the current character is an operator.
    if (OPERATIONS[c]) {
      // Recursively solve the subexpression to the left of the operator.
      const leftResults = dfs(exp.substring(0, i));
      // Recursively solve the subexpression to the right of the operator.
      const rightResults = dfs(exp.substring(i + 1));

      // Combine the results from both subexpressions based on the operator.
      for (let a of leftResults) {
        for (let b of rightResults) {
          // Apply the corresponding function based on the operator.
          results.push(OPERATIONS[c](a, b));
        }
      }
    }
  }

  // Store the computed results in the memoization object before returning.
  memo[exp] = results;
  return results;
}

function isNumber(str) {
  return /^\d+$/.test(str);
}
