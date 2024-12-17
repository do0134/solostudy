// 12121 Pretty Good Proportion (Small) 

using System.Collections;

int t = int.Parse(Console.ReadLine());
double epsilon = Math.Pow(10, -6);
for (int i = 1; i < t+1; i++)
{
    int answer = 0;
    double minDiff = 1;

    string[] inputs = Console.ReadLine().Split(' ');
    int n = int.Parse(inputs[0]);
    double f = double.Parse(inputs[1]);

    string s = Console.ReadLine();

    for (int j = 0; j < n; j++)
    {
        double oneCount = 0;
        bool flag = false;
        for (int k = j; k < n; k++)
        {
            if (s[k].Equals('1')) 
                oneCount++;


            double diff = (oneCount / (k-j+1));
            double curDiff = Math.Abs(f - diff);

            if (minDiff > curDiff)
            {
                answer = j;
                minDiff = curDiff;
            }
            
            else if (curDiff < epsilon)
            {
                answer = Math.Min(answer, j);
            }
        }
    }
    if (answer == int.MaxValue)
        answer = 0;
    Console.WriteLine($"Case #{i}: {answer}");
}