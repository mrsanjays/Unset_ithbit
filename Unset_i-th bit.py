def check_bit(A,B):
    if A&(1<<B):
        return True
    return False
"""
You are given two integers A and B.
If B-th bit in A is set, make it unset.
If B-th bit in A is unset, leave as it is.
Return the updated A value.
"""
def Unset_ithbit(A,B):
    if check_bit(A,B):
        return A^(1<<B)
    return A

if __name__ == '__main__':
    A=int(input())
    B=int(input())
    print(Unset_ithbit(A,B))
