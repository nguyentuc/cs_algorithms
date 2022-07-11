# python program for activity selection problem when input activities may not sorted
def MaxActivities(arr, n):
    selected = []

    # sort jobs according to finish time
    arr.sort(key=lambda x: x[1]) # sap xep theo x[1]

    # the first activity always gets selected
    i = 0
    selected.append(arr[i])

    for j in range(1, n):
        # If this activity has start time greater than or equal to the finish time
        # of previous selected activity, then select it
        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j
    return selected


# Initialization code
activities = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
n = len(activities)

selected = MaxActivities(activities, n)
print("Following activities are selected :", selected)
