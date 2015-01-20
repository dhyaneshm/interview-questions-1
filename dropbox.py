# Given a valid expression as a string, parse and evaluate it

validOperators = ['+', '-', '*', '/', ')']
def performOperation(operator, a, b):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/float(b)
        
# eval('1+2*3') == 7
# returns a list of operators and operands
def parseExpression(expression):
    expressionList = []
    numSoFar = ""
    for val in expression:
        if val == '(':
            expressionList.append(val)
            continue
        if val in validOperators:
            if len(numSoFar) != 0:
                expressionList.append(int(numSoFar))
            expressionList.append(val)
            numSoFar = ""
        else:
            numSoFar+=val
    if len(numSoFar) != 0:
        expressionList.append(int(numSoFar))
    return expressionList

def evalHelper(expression, operators):
    newExpression  = []
    i = 0
    while i < len(expression):
        val = expression[i]
        if (val in operators):
            result = performOperation(val, newExpression.pop(), expression[i+1])
            i+=1
            newExpression.append(result)
        else:
            newExpression.append(val)
        i+=1
    return newExpression

def replace(expression, start, end, result):
    for _ in range(end-start):
        expression.pop(start)
    expression.insert(start, result)


def removeParen(expression):
    newExpression = []
    startIndicies = []
    i = 0
    for val in expression:
        if val == '(': startIndicies.insert(0,i)
        elif val == ')': 
            start = startIndicies.pop(0)
            result = evaluate(newExpression[start:i])
            replace(newExpression, start, i, result)
            i-=(i-start+1)
        else:
            newExpression.append(val)
            i+=1
    return newExpression

def evaluate(expression):
    expression = evalHelper(expression, ["*", "/"])
    expression = evalHelper(expression, ["+", "-"])
    return expression[0]

testExpression = '(2*(4-(3-(4+2))))'
expression = parseExpression(testExpression)
expression = removeParen(expression)
print evaluate(expression)