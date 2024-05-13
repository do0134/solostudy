// HackerRank Staircase

public static void staircase(int n)
{
    for (int i = 1; i <= n; i++)
    {
        string temp = "";

        for (int j = 0; j < n - i; j++)
        {
            temp += " ";
        }

        for (int j = 0; j < i; j++)
        {
            temp += "#";
        }
        Console.WriteLine(temp);
    }
}