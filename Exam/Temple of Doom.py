def solve_temple_puzzle(a, b, c):
    while a and b and c:
        current_tool = a[0]
        current_substance = b[-1]
        challenge = current_tool * current_substance

        if challenge in c:
            a.remove(current_tool)
            b.pop()
            c.remove(challenge)
        else:
            a.append(a.pop(0) + 1)
            b[-1] -= 1
            if b[-1] == 0:
                b.pop()

    if not b or c or a:
        print("Harry is lost in the temple. Oblivion awaits him.")
        print("Tools:", ', '.join([str(tool) for tool in tools]))
        print("Challenges:", ', '.join([str(challenge) for challenge in challenges]))
        return
    else:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        print("Substances:", ', '.join([str(substance) for substance in substances]))
        return


tools = ([int(x) for x in input().split()])

substances = ([int(x) for x in input().split()])

challenges = ([int(x) for x in input().split()])

solve_temple_puzzle(tools, substances, challenges)
