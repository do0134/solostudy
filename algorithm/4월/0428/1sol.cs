// HackerRank Staircase

public static void staircase(int n)
{
    int i = 1;
    while (i <= n)
    {
        string temp = "";

        for (int j = 1;j <= n;j++)
        {
            if (n-i >= j)
            temp += " ";
            else
            temp += "#";
        }

        Console.WriteLine(temp);
        i++;
    }
}