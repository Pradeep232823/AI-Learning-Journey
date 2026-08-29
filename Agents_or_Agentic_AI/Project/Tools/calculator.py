import ast
import operator


def calculate(expression):

    try:
        tree = ast.parse(expression, mode="eval")

        return evaluate(tree.body)

    except ZeroDivisionError:
        return "Can't divide using 0"

    except (ValueError, TypeError, SyntaxError):
        return "Invalid mathematical expression"


def evaluate(node):

    if isinstance(node, ast.Constant):

        if isinstance(node.value, (int, float)):
            return float(node.value)

        raise ValueError

    if isinstance(node, ast.BinOp):

        left = evaluate(node.left)
        right = evaluate(node.right)

        operations = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv
        }

        operation = operations.get(type(node.op))

        if operation is None:
            raise ValueError

        return operation(left, right)

    raise ValueError