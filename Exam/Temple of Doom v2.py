def solve_temple_puzzle(tools, substances, challenges):
    while tools and substances and challenges:
        tool = tools[0]
        substance = substances[-1]
        result = tool * substance

        if result in challenges:
            tools.remove(tool)
            substances.remove(substance)
            challenges.remove(result)
        else:
            tools.append(tools.pop(0) + 1)
            substances[-1] -= 1
            if substances[-1] == 0:
                substances.pop()

    if not substances or challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        print("Substances:", ", ".join(str(substance) for substance in substances))
    else:
        print("Harry is lost in the temple. Oblivion awaits him.")
        print("Tools:", ", ".join(str(tool) for tool in tools))
        print("Challenges:", ", ".join(str(challenge) for challenge in challenges))


tools = ([int(x) for x in input().split()])
substances = ([int(x) for x in input().split()])
challenges = ([int(x) for x in input().split()])
solve_temple_puzzle(tools, substances, challenges)
