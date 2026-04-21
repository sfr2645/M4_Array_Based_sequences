from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter

def main():
    postfix = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -"
    ]

    infix = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A * B + C / D",
        "( A + B ) * ( C - D )",
        "A + B * C - D / E",
        "A * ( B + C ) / D",
        "( A + B * C ) / ( D - E )",
        "A + ( B - C ) * D",
        "( A + B * ( C - D ) ) / E"
    ]

    print("----- Postfix Evaluator -----")
    for expr in postfix:
        evaluator = PostfixEvaluator(expr)
        result = evaluator.evaluate()
        print(f"[{expr}] = {result}")

    print("\n----- Infix to Postfix Converter -----")
    for expr in infix:
        converter = InfixToPostfixConverter(expr)
        result = converter.convert()
        print(f"[{expr}] -> [{result}]")

if __name__ == "__main__":
    main()