# cho truoc n hanh dong co the thuc hien voi thoi gian bat dau va ket thuc tuong ung
# trong mot khoang thoi gian cho truoc
# hay dua ra so hanh dong lon nhat ma mot nguoi co the thuc hien
# trong mot thoi diem thi mot nguoi chi co the lam mot viec

# lựa chọn tham lam luôn chọn hành động tiếp theo là hành động có thời gian
# kết thúc nhỏ nhất và thời gian bắt đầu lớn hơn hoặc bằng thời gian của
# hành động trước đó

# the following implementation assumes that the activities already sorted
# according to their finish time
# Out: print the maximum set of activities that can be done by a single person
# n -> total number of activities
# s[] -> an array contains start time of all activities
# f[] -> an array contains finish time of all activities

def printMaxActivities(s, f):
    n = len(f)
    print("The following activities are selected:")
    # the first actitivity is always selected
    i = 0
    print(i)

    # consider the rest of the actitities
    for j in range(n):
        # if this activity has start time greater than or equal to the finish time of
        # previously seleted activity, then select it
        if s[j] >= f[i]:
            print(j)
            i = j


# initialization program to test above function
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
printMaxActivities(s,f)
