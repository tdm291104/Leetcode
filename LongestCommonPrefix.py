from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        # Sắp xếp danh sách chuỗi theo thứ tự từ điển
        strs = sorted(strs)
        # Lấy chuỗi đầu tiên và cuối cùng
        first = strs[0]
        last = strs[-1]
        # So sánh từng ký tự của chuỗi đầu tiên và cuối cùng
        for i in range(min(len(first), len(last))):
            # Nếu ký tự tại vị trí i của chuỗi đầu tiên khác ký tự tại vị trí i của chuỗi cuối cùng
            if first[i]!=last[i] :
                return result
            result += first[i]
        return result

# Demo
s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # Kết quả: "fl"
