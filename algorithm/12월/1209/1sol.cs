using System;

namespace Algo1
{
    class Program
    {
        // 백준 25377 빵
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int answer = -1;
            for (int i = 0; i < n; i++)
            {
                string[] store = Console.ReadLine().Split(' ');
                int a = int.Parse(store[0]);
                int b = int.Parse(store[1]);
                if (a > b)
                    continue;
                int c = Math.Max(a,b);
                if (answer == -1 || answer > c)
                    answer = c;
            }

            Console.WriteLine(answer);
        }
    }
}
