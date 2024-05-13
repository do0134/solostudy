// HackerRank Mini-Max Sum

public static void miniMaxSum(List<int> arr)
{
    arr.Sort();

    long a = 0;
    long b = 0;

    for (int i = 0; i < arr.Count - 1; i++)
    {
        a += arr[i];
    }

    for (int i = 1; i < arr.Count; i++)
    {
        b += arr[i];
    }

    string answer = $"{a} {b}";
    Console.Write(answer);
}
