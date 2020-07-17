class ReverseWordsInString:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        temp_list = s.split(" ")
        str_list = [i for i in temp_list if i != '']
        start, end = 0, len(str_list)-1
        while start < end:
            str_list[start], str_list[end] = str_list[end], str_list[start]
            start += 1
            end -= 1
        return " ".join(str_list)


obj = ReverseWordsInString()
print(obj.reverseWords("the sky is blue"))
print(obj.reverseWords("  hello world!  "))
print(obj.reverseWords("a good   example"))