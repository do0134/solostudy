// HackerRank 2D Array -DS

public static int hourglassSum(List<List<int>> arr)
{
    int answer = -64;

    for (int i = 1; i < 5; i++) {
        for (int j = 1; j < 5; j++) {
            int temp = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1];
            answer = Math.Max(temp, answer);
        }
    }

    return answer;
}