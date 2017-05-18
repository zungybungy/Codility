using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        String s = "{[()()]}";

        Console.WriteLine(solution(s));
    }

    public static int solution(String S)
    {
        var stack = new Stack<int>();

        foreach (var bracket in S)
        {
            switch (bracket)
            {
                case '(':
                    stack.Push(0);
                    break;
                case '[':
                    stack.Push(1);
                    break;
                case '{':
                    stack.Push(2);
                    break;

                case ')':
                    if (stack.Count == 0 || stack.Pop() != 0)
                    {
                        return 0;
                    }
                    break;
                case ']':
                    if (stack.Count == 0 || stack.Pop() != 1)
                    {
                        return 0;
                    }
                    break;
                case '}':
                    if (stack.Count == 0 || stack.Pop() != 2)
                    {
                        return 0;
                    }
                    break;
            }
        }

        if (stack.Count == 0)
        {
            return 1;
        }

        return 0;
    }
}




