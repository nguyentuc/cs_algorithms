# Given a text txt[0..n-1] and a pattern pat[0..m-1],
# write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[].
# You may assume that n > m.
# Example
# Input:  txt[] = "THIS IS A TEST TEXT"
#         pat[] = "TEST"
# Output: Pattern found at index 10
#
# Input:  txt[] =  "AABAACAADAABAABA"
#         pat[] =  "AABA"
# Output: Pattern found at index 0
#         Pattern found at index 9
#         Pattern found at index 12

# Python3 program for Naive Pattern searching algorithm
def search(pat, txt):
    M = len(pat)
    N = len(txt)
    # A loop to slide pat[] one by one
    for i in range(N - M + 1):
        j = 0
        # for current index i, check for pattern match
        while j < M:
            if txt[i + j] != pat[j]:
                break
            j += 1
        if j == M:
            print("Pattern found at index: ", i)


# Driver code
if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)

# Trường hợp tốt nhất khi ký tự đầu tiên của pattern không xuất hiện trọng đoạn text
# Độ phúc tạp 0(n)
# Trường hợp tồi nhất khi tất cả các ký tự trong chuỗi text và đoạn pattern giống nhau
# Hoặc khi chỉ có ký tự cuối cùng của chuỗi pattern là khác
# Độ phức tạp thuật toán trong trường hợp tồi nhất: O(m *(n-m+1))
