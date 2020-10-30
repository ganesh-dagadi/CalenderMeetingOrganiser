# Includes the start and end time boundaries
def Include_boundaries(schedule, available):
    for slot in available:
        startList = [slot[0], slot[0]]
        schedule.insert(0, startList)
        endList = [slot[1], slot[1]]
        schedule.append(endList)
    return schedule


def to_Minutes(slot):
    slot_list = slot.split(':')
    for i in range(len(slot_list)):
        slot_list[i] = int(slot_list[i])
    hour = slot_list[0]
    minute = slot_list[1]
    total = (hour * 60) + minute
    return total


# Returns the free slots for each person

def Find_free_slots(busy_list, meeting_duration):
    free_slots = []
    for i in range(len(busy_list) - 1):  # -1 because range will be out of list's order
        slot1 = busy_list[i]
        slot2 = busy_list[i + 1]
        start = slot1[1]  # refers to start and end of free time
        end = slot2[0]
        start_list = start.split(':')  # start_list[0] refers to hour and start_list[1] refers to minute
        end_list = end.split(':')  # Same with end list

        def to_int(in_list):  # converting strings to integers
            for j in range(len(in_list)):
                in_list[j] = int(in_list[j])

        to_int(start_list)
        to_int(end_list)

        # finding time difference between two slots
        hour_diff = end_list[0] - start_list[0]
        minute_diff = end_list[1] - start_list[1]

        time_difference = (hour_diff * 60) + minute_diff
        if time_difference >= meeting_duration:
            free_slots.append([start, end])

    return free_slots


def Find_common_slots(person1, person2, meeting_duration):
    result = []
    # loops through each slot in person1 free time comparing every slot in person1 to every slot in person 2
    for slot_person1 in person1:
        for slot_person2 in person2:
            # if the start of a slot of person 1 lies between any slot of person 2
            if slot_person2[0] < slot_person1[0] < slot_person2[1]:
                # start refers to start of common slot as it lies between the free slot of person 2 and it is common
                # to both person 1 and person 2
                start = slot_person1[0]
                end = slot_person2[1]
                other_end = slot_person1[1]
                # end and other end are the two possible ends that the common slot can have

                start_minutes = [to_Minutes(start), start]
                other_end_minutes = [to_Minutes(other_end), other_end]
                end_minutes = [to_Minutes(end), end]
                # looks like : [minute value of start for comparing in next steps , slot in string format]

                if start_minutes[0] + meeting_duration <= end_minutes[0]:
                    # checking if there is enough time for the meeting
                    shorter_duration = []
                    # We assume end_minutes to be shorter than other_end_minutes
                    shorter_duration.insert(0, end_minutes[0] - start_minutes[0])
                    shorter_duration.append(start_minutes[1])
                    shorter_duration.append(end_minutes[1])
                    # shorter duration looks like [int Time difference , start time slot , end time slot]

                    # earlier we assumes that end_minutes is lesser than other_end_minutes. We check if its true and set
                    # the shorter_duration accordingly
                    if other_end_minutes[0] - start_minutes[0] < shorter_duration[0]:
                        shorter_duration = other_end_minutes

                    # We no more need the duration of common slot. Thus we pop it out
                    shorter_duration.pop(0)
                    result.append(shorter_duration)

    return result
