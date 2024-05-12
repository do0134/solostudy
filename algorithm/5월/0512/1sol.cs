// HackerRank Plus Minus

public static void plusMinus(List<int> arr)
{
    float p = 0;
    float m = 0;
    float z = 0;
    int n = arr.Count();

    foreach (int i in arr)
    {
        if (i > 0)
        {
            p += 1.0f;
        }
        else if (i < 0)
        {
            m += 1.0f;
        }
        else
        {
            z += 1.0f;
        }
    }

    float plus = p / n;
    float minus = m / n;
    float zero = z / n;

    Console.WriteLine(string.Format("{0:F6}", plus));
    Console.WriteLine(string.Format("{0:F6}", minus));
    Console.WriteLine(string.Format("{0:F6}", zero));
}