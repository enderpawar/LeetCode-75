class Solution:
    def compress(self, chars):
        write = 0
        read = 0

        while read < len(chars):
            crt_char = chars[read]
            char_cnt = 0

            # 같은 문자가 이어지는 동안 read를 끝까지 밀어붙임
            while read < len(chars) and chars[read] == crt_char:
                read += 1
                char_cnt += 1

            # 문자 먼저 쓰고 포인터 증가
            chars[write] = crt_char
            write += 1

            # 길이가 2 이상일 때만 자릿수별로 기록
            if char_cnt > 1:
                for digit in str(char_cnt):
                    chars[write] = digit
                    write += 1

        return write