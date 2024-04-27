// HackerRank PlusMinus

public static void plusMinus(List<int> arr)
{
    int n = arr.Count;

    int positive = 0;
    int negative = 0;
    int zero = 0;

    for (int i = 0; i < n; i++)
    {
        if (arr[i] > 0)
        positive++;
        else if (arr[i] < 0)
        negative++;
        else
        zero++;
    }

    Console.WriteLine(string.Format("{0:N7}", (float)positive/n));
    Console.WriteLine(string.Format("{0:N7}", (float)negative/n));
    Console.WriteLine(string.Format("{0:N7}", (float)zero/n));
}