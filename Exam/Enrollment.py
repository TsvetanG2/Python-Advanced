def gather_credits(credits_needed, *courses):
    enrolled_courses = set()
    gathered_credits = 0

    for course in courses:
        course_name, course_credits = course

        if gathered_credits >= credits_needed:
            break

        if course_name in enrolled_courses:
            continue

        gathered_credits += course_credits
        enrolled_courses.add(course_name)

    enrolled_courses = sorted(enrolled_courses)

    if gathered_credits >= credits_needed:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(enrolled_courses)}"
    else:
        credits_shortage = credits_needed - gathered_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."
