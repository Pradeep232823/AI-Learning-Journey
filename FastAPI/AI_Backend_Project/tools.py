import ast
import operator

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}


def calculator(expression):
    try:
        tree = ast.parse(expression, mode="eval")

        def evaluate(node):

            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value
                raise ValueError("Invalid value")

            if isinstance(node, ast.BinOp):
                operation = operators.get(type(node.op))

                if operation is None:
                    raise ValueError("Unsupported operator")

                left = evaluate(node.left)
                right = evaluate(node.right)

                return operation(left, right)

            raise ValueError("Invalid expression")

        return evaluate(tree.body)

    except ZeroDivisionError:
        return "Cannot divide by zero"

    except Exception:
        return "Invalid expression"