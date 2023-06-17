def resolve_temple():
    tools = ([int(x) for x in input().split()])
    substances = ([int(x) for x in input().split()])
    challenges = ([int(x) for x in input().split()])

    while tools and substances:
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

    if challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
        print(f"Tools: {', '.join(map(str, tools))}")
        print(f"Challenges: {', '.join(map(str, challenges))}")
    else:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        print(f"Substances: {', '.join(map(str, substances))}")


resolve_temple()
