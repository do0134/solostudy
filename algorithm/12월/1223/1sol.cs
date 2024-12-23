using System;
// 14651 걷다보니 신천역 삼
namespace Algo1
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            long answer = 2;
            if (n == 1)
                answer = 0;
            else if (n == 2)
                answer = 2;
            else
            {
                for (int i = 2; i < n; i++)
                {
                    answer *= 3;
                    answer %= 1000000009;
                }
            }
            Console.WriteLine(answer);
        }
    }
}
