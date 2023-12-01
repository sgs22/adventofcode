class Solution:
    def get_calibration_values_sum(self) -> int:
        sum = 0
        with open('calibration_document.txt') as file:
            for line in file:
                value = self.calculate_line_value(line)
                sum += value
        return sum

    def calculate_line_value(self, line: str) -> int:
        line = self.process_line_digits(line)
        value = ""
        for char in line:
            if char.isdigit():
                value += char
                break
        for char in line[::-1]:
            if char.isdigit():
                value += char
                break
        if len(value) == 0:
            return 0
        return int(value)

    def process_line_digits(self, line: str) -> str:
        integers_lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
                           'seven': '7', 'eight': '8', 'nine': '9'}
        left = 0
        right = 1
        while left <= len(line) - 1 and right <= len(line):
            while right <= len(line):
                if line[left:right] in integers_lookup.keys():
                    line = line.replace(line[left:right], integers_lookup[line[left:right]])
                right += 1
            right = left + 1
            left += 1
        return line
               
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.get_calibration_values_sum())
    # print(solution.calculate_line_value("qp4"))