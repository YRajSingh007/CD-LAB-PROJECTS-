
def infix_2_postfix(Infix):
    Stack = []
    Postfix = []
    priority = {
        "^": 3,
        "*": 2,
        "/": 2,
        "%": 2,
        "+": 1,
        "-": 1,
    }
    print_width = len(Infix) if (len(Infix) > 7) else 7
    for x in Infix:
        if x.isalpha() or x.isdigit():
            Postfix.append(x)
        elif x == "(":
            Stack.append(x)
        elif x == ")":
            while Stack[-1] != "(":
                Postfix.append(Stack.pop())
            Stack.pop()
        else:
            if len(Stack) == 0:
                Stack.append(x)
            else:
                while (
                    len(Stack) > 0 and priority[x] <= priority[Stack[-1]]
                ):
                    Postfix.append(Stack.pop())
                Stack.append(x)

    while len(Stack) > 0:
        Postfix.append(Stack.pop())
    return "".join(Postfix)


def infix_2_prefix(Infix):
    Infix = list(Infix[::-1])

    for i in range(len(Infix)):
        if Infix[i] == "(":
            Infix[i] = ")"
        elif Infix[i] == ")":
            Infix[i] = "("

    return (infix_2_postfix("".join(Infix)))[
        ::-1
    ]
if __name__ == "__main__":
    print("INFIX TO PREFIX")
    Infix = input("\nEnter an Infix Equation = ")
    Infix = "".join(Infix.split())
    print("Prefix:", infix_2_prefix(Infix) )
