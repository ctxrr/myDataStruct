根据下面的二叉树，对所有的路径值拼接组成的字符的数值进行求和

[![binary-tree](https://github.com/ctxrr/myDataStruct/blob/my-algorithm-exercise/my-algorithm-exercise/binary-tree.jpg)](#features)

所有路径包括：
```
8-4-2-1 => 8421
9-4-2-1 => 9421
10-5-2-1 => 10521
11-5-2-1 => 11521
6-3-1 => 631
7-3-1 => 731

total: 41246
```

#验证：
```
$ python exercise.py
```

#算法分析：

    时间复杂度:O(n) //不考虑乘方

#程序分析：

    1.首先找到二叉树的树叶(leaf),通过递归将当前树叶所在的深度确定，例如第H节点n=3，当前值应为8 * 10^3

    2.函数返回一个数组array,array[1]代表了该节点的树叶子节点个数。例如第D节点,包含树叶子节点为2个，因此它要被计算2次.

    3.同理，第B节点包含4个树叶子节点(HIJK)，代表它要被计算4次。

#我的更多关于数据结构的练习代码：
* [ctxrr/myDataStruct](https://github.com/ctxrr/myDataStruct)
