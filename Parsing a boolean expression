class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> stk;  // Stack to hold characters and operators
        
        // Iterate over each character in the expression
        for (char c: expression) {
            // Push valid characters (non ')' and non ',') to the stack
            if (c != ')' && c != ',') stk.push(c);
            else if (c == ')') {  // When ')' is encountered, evaluate subexpression
                vector<bool> exp;  // Vector to hold boolean values of the current subexpression
                
                // Pop characters until '(' is found, collect 't' or 'f' values
                while (!stk.empty() && stk.top() != '(') {
                    char t = stk.top(); 
                    stk.pop();
                    if (t == 't') exp.push_back(true);
                    else exp.push_back(false);
                }
                
                stk.pop();  // Pop the '(' from the stack
                
                if (!stk.empty()) {
                    char t = stk.top();  // Get the operator before '('
                    stk.pop();
                    bool v = exp[0];  // Initialize result with the first value
                    
                    // Perform the corresponding logical operation
                    if (t == '&') {  // AND operation: all values must be true
                        for (bool b: exp) v &= b;
                    } else if (t == '|') {  // OR operation: at least one value is true
                        for (bool b: exp) v |= b;
                    } else {  // NOT operation: negate the first value
                        v = !v;
                    }
                    
                    // Push the result back to the stack as 't' or 'f'
                    if (v) stk.push('t');
                    else stk.push('f');
                }
            }
        }
        
        // Return the final result from the stack
        return stk.top() == 't' ? true : false;
    }
};
