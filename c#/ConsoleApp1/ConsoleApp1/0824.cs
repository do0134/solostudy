// See https://aka.ms/new-console-template for more information
int n = int.Parse(Console.ReadLine());
int minValue = int.MaxValue;
int[] answer = new int[2];
for (int i = 0; i< n; i++)
{
    string[] xy = Console.ReadLine().Split(' ');
    int x = int.Parse(xy[0]); int y = int.Parse(xy[1]);
    if (y < minValue)
    {
        minValue = y;
        answer[0] = x; answer[1] = y;
    }
}

Console.WriteLine($"{answer[0]} {answer[1]}");