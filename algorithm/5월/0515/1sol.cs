// HackerRank Bill Division

public static void bonAppetit(List<int> bill, int k, int b)
{
    int total = 0;
    for (int i = 0; i < bill.Count; i++)
    {
        if (i == k)
        {
            continue;
        }

        total += bill[i];
    }

    int avg = total / 2;

    if (avg >= b)
    {
        Console.WriteLine("Bon Appetit");
    }
    else
    {
        Console.WriteLine(Math.Abs(b - avg));
    }


}