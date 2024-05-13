// HackerRank Birthday Cake Candles

public static int birthdayCakeCandles(List<int> candles)
{
    long max_v = 0;
    int answer = 0;

    foreach (int candle in candles)
    {
        if (candle > max_v)
        {
            answer = 1;
            max_v = candle;
        }
        else if (candle == max_v)
        {
            answer += 1;
        }
    }

    return answer;

}