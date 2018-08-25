class Solution(object):    
    def threeSum(self,num):
        num.sort()
        res=[]
        i=0
        while (i < len(num)-2):
            if (i == 0 or (i > 0 and num[i] != num[i-1])):
                lo = i+1
                hi = len(num)-1
                sum = 0 - num[i]
                while (lo < hi):
                    curre=[]
                    if (num[lo] + num[hi] == sum):
                        curre.append(num[i])
                        curre.append(num[lo])
                        curre.append(num[hi])
                        res.append(curre)
                        while (lo < hi and num[lo] == num[lo+1]):
                            lo=lo+1
                        while (lo < hi and num[hi] == num[hi-1]):
                            hi=hi-1
                        lo=lo+1
                        hi=hi-1
                    elif (num[lo] + num[hi] < sum):
                        lo=lo+1
                    else:
                        hi=hi-1
            i=i+1
        
        return res


