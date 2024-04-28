// HackerRank Birthday Cake Candles

public static int birthdayCakeCandles(List<int> candles)
{
    long max_v = candles.Max();
    return candles.Where(c => c == max_v).Count();
}