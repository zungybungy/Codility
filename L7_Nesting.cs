using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        String s = "(()(())()))";

        Console.WriteLine(solution(s));
    }

    public static int solution(string S)
    {
        var count = 0;

        foreach (var character in S)
        {
            if (character == '(')
            {
                count++;
            }
            else if (count == 0)
            {
                return 0;
            }
            else
            {
                count--;
            }
        }

        if (count == 0)
        {
            return 1;
        }

        return 0;
    }
}
}




