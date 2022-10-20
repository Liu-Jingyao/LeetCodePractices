from itertools import chain, repeat, islice
import numpy as np
from time import time
import logging

INF = 1E9
logger = logging.getLogger()


def inp():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a


def selection_problem(n, k, s, m):
    if m == 'search':
        logging.info("search first %d small number in %s" % (k, s))
    # 不足一组时, 直接判断
    if n <= 5:
        return sorted(s)[k - 1]
    # 将s划分为[n/5]组 O(n)
    a_divided = [list(islice(chain(s[i:], repeat(INF)), 5)) for i in range(0, n, 5)]
    # print(a_divided)
    # 排序每组元素, 分别确定每组的中位数 O(n)
    a_medians = [sorted(li)[2] for li in a_divided]
    # 计算[n/5]个中位数的中位数p T(n/5)
    p = selection_problem(len(a_medians), len(a_medians) // 2, a_medians, 'median')
    # 如果是在查找中位数就直接返回p
    if m == 'median':
        return p

    # 用p将s划分为三个子集s1, s2和s3
    # 其中s1元素小于p, s2元素等于p, s3元素大于p O(n)
    l, r = 0, n - 1
    # 由于不清楚p的位置，使用双指针来做Partition（或者先找p的下标再常规Partition也可以）
    while l < r:
        # 如果a[l]<p, l++; 如果a[r]>p r--
        # 如果a[l]=>p且a[r]<=p, 交换a[l], a[r], (若a[l]!=p) l++, (若a[r]!=p) r--
        while s[l] < p:
            l += 1
        while s[r] > p:
            r -= 1
        if s[l] >= p >= s[r]:
            s[l], s[r] = s[r], s[l]
            if not s[l] == p:
                l += 1
            if not s[r] == p:
                r -= 1
            # 判断有多个元素值等于p的情况
            if not l == r and s[l] == p and s[r] == p:
                s[l], s[r - 1] = s[r - 1], s[l]
                r -= 1

    s1 = s[0:l]
    s2 = s[l:l + 1]
    s3 = s[l + 1:n]
    logging.info("s1: %s s2: %s s3: %s" % (s1, s2, s3))
    # 若|S1|>=k，则递归地在S1中搜索第k小元素；
    # 否则，若|S1|+|S2|>=k，则p即为S中第k小元素；
    # 否则，令k'=k-|S1|-|S2|，递归地在S3中搜索第k'小元素
    # T(3n/4)
    if len(s1) >= k:
        return selection_problem(len(s1), k, s1, 'search')
    elif len(s1) + len(s2) >= k:
        return s2[0]
    else:
        return selection_problem(len(s3), k - len(s1) - len(s2), s3, 'search')


def main():
    # 开启过程输出
    # logging.basicConfig(level=logging.NOTSET,
    #                     format='%(asctime)s - [line:%(lineno)d] - %(message)s')

    # 程序本体
    # 输入格式：
    #   元素个数 寻找的第k小
    #   元素列表（空格分隔）
    # 举例：
    #   5 1
    #   4 3 2 1 5
    # n, k, a = inp()
    # print(selection_problem(n, k, a, 'search'))

    # 正确性测试
    while True:
        start = time()
        # n = np.random.randint(100000)
        n = 100000
        k = np.random.randint(n)
        a = np.random.randint(INF, size=n)
        test_ans = selection_problem(n, k, a, 'search')
        test_stop = time()
        correct_ans = sorted(a)[k - 1]
        correct_stop = time()
        flag = correct_ans == test_ans
        print(flag, "n=", n, "k=", k, "分治用时:", str(test_stop - start) + "秒", "sorted()用时:",
              str(correct_stop - test_stop) + "秒")
        # 可见, 手写算法其实是比使用python内置库慢很多的..
        assert flag


if __name__ == "__main__":
    main()
