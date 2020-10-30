import functions

# Input Data
Person1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
Person1_Avail = [['9:00', '20:00']]

Person2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
Person2_Avail = [['10:00', '18:30']]

Duration = 30


def Arrange_Meeting(Person1, Person1_Avail, Person2, Person2_Avail):
    # includes the start and end time boundaries for each person
    Person1_busy = functions.Include_boundaries(Person1, Person1_Avail)
    Person2_busy = functions.Include_boundaries(Person2, Person2_Avail)

    Person1_free = functions.Find_free_slots(Person1, Duration)
    Person2_free = functions.Find_free_slots(Person2, Duration)

    result1 = functions.Find_common_slots(Person1_free, Person2_free, Duration)
    result2 = functions.Find_common_slots(Person2_free, Person1_free, Duration)

    return result1 + result2


print(Arrange_Meeting(Person1, Person1_Avail, Person2, Person2_Avail))
