// HackerRank Diagonal Difference

public static int diagonalDifference(List<List<int>> arr)
{
    int n = arr.Count;
    int a = 0;
    int b = 0;


    for (int i = 0; i < n; i++)
    {
        a += arr[i][i];
        b += arr[i][n - i - 1];
    }

    return Math.Abs(a - b);
}