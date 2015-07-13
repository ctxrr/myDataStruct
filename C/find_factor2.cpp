//copyright@ 2011 zhouzhenren

//输入两个整数 n 和 m，从数列1，2，3.......n 中 随意取几个数,
//使其和等于 m ,要求将其中所有的可能组合列出来。

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

/**
 * 输入t， r， 尝试Wk
 */
void sumofsub(int t, int k ,int r, int& M, bool& flag, bool* X)
{
    X[k] = true;   // 选第k个数
    if (t + k == M) // 若找到一个和为M，则设置解向量的标志位，输出解
    {
        flag = true;
        for (int i = 1; i <= k; ++i)
        {
            if (X[i] == 1)
            {
                printf("%d ", i);
            }
        }
        printf("\n");
    }
    else
    {   // 若第k+1个数满足条件，则递归左子树
        if (t + k + (k+1) <= M)
        {
            sumofsub(t + k, k + 1, r - k, M, flag, X);
        }
        // 若不选第k个数，选第k+1个数满足条件，则递归右子树
        if ((t + r - k >= M) && (t + (k+1) <= M))
        {
            X[k] = false;
            sumofsub(t, k + 1, r - k, M, flag, X);
        }
    }
}

void search(int& N, int& M)
{
    // 初始化解空间
    bool* X = (bool*)malloc(sizeof(bool) * (N+1));
    memset(X, false, sizeof(bool) * (N+1));
    int sum = (N + 1) * N * 0.5f;
    if (1 > M || sum < M) // 预先排除无解情况
    {
        printf("not found\n");
        return;
    }
    bool f = false;
    sumofsub(0, 1, sum, M, f, X);
    if (!f)
    {
        printf("not found\n");
    }
    free(X);
}

int main()
{
    int N, M;
    printf("请输入整数N和M\n");
    scanf("%d%d", &N, &M);
    search(N, M);
    return 0;
}
