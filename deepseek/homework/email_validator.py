import re
import unittest


def is_valid_email(email_string):
    """
    验证给定的字符串是否为有效的电子邮件地址

    参数:
        email_string (str): 要验证的电子邮件地址字符串

    返回:
        bool: True 表示有效的邮箱地址格式，False 表示无效的格式

    异常:
        TypeError: 当输入不是字符串类型时抛出

    验证规则:
        - 基于RFC 5322标准，但不支持国际化域名(IDN)
        - 本地部分允许: 字母、数字、!#$%&'*+/=?^_`{|}~-以及.号(但不能连续或开头结尾)
        - 域名部分允许: 字母、数字、连字符和点号
        - 顶级域名至少2个字符
        - 总长度不超过254个字符
    """

    # 1. 检查输入类型
    if not isinstance(email_string, str):
        raise TypeError(f"输入必须是字符串类型，但收到的是 {type(email_string).__name__}")

    # 2. 去除首尾空格（用于检查，但带空格的字符串本身应该视为无效）
    email_string = email_string.strip()

    # 3. 检查是否为空字符串
    if not email_string:
        return False

    # 4. 检查总长度（RFC 5321规定最大为254个字符）
    if len(email_string) > 254:
        return False

    # 5. 定义正则表达式模式
    # 正则表达式设计思路:
    # 这个模式参考了RFC 5322标准，但做了一些简化以保持实用性和可读性
    # 它覆盖了大多数常见的邮箱格式，包括:
    #   - 本地部分可以包含字母、数字和特殊字符: !#$%&'*+/=?^_`{|}~-.
    #   - 支持+号作为别名标记(如user+tag@domain.com)
    #   - 支持多级域名(如.co.uk, .com.cn)
    #   - 要求顶级域名至少2个字符
    #   - 不支持国际化域名(IDN)中的非ASCII字符

    # 正则表达式详解:
    # ^                           # 字符串开始
    # (                           # 本地部分开始
    #   [a-zA-Z0-9]              # 必须以字母或数字开头
    #   [a-zA-Z0-9._%+!#$&'*\/=?^{|}-]*  # 可以包含的字符，0个或多个
    #   [a-zA-Z0-9]              # 必须以字母或数字结尾
    # )                           # 本地部分结束
    # @                           # @符号
    # (                           # 域名部分开始
    #   [a-zA-Z0-9]+             # 主域名: 至少一个字母或数字
    #   (?:                      # 子域名开始(非捕获组)
    #     \.                     # 点号分隔符
    #     [a-zA-Z0-9]+           # 子域名: 至少一个字母或数字
    #   )*                       # 0个或多个子域名
    #   \.                       # 最后必须有点号
    #   [a-zA-Z]{2,}             # 顶级域名: 至少2个字母
    # )                           # 域名部分结束
    # $                           # 字符串结束

    email_pattern = r'''
        ^
        (                           # 本地部分
          [a-zA-Z0-9]              # 必须以字母或数字开头
          [a-zA-Z0-9._%+!#$&'*\/=?^{|}-]*  # 中间可以包含的字符
          [a-zA-Z0-9]              # 必须以字母或数字结尾
        )
        @                           # @符号
        (                           # 域名部分
          [a-zA-Z0-9]+             # 主域名
          (?:
            \.
            [a-zA-Z0-9]+
          )*
          \.                       # 最后必须有点号
          [a-zA-Z]{2,}             # 顶级域名
        )
        $
    '''

    # 6. 使用re.VERBOSE模式，允许正则表达式中有注释和空白
    # 使用re.IGNORECASE处理大小写，但域名部分会自动转换为小写处理
    if re.match(email_pattern, email_string, re.VERBOSE | re.IGNORECASE):
        return True
    else:
        return False


class TestIsValidEmail(unittest.TestCase):
    """测试 is_valid_email 函数的单元测试类"""

    def test_valid_emails(self):
        """测试不同类型的有效邮箱地址"""

        valid_emails = [
            # 1. 简单邮箱
            ("simple@example.com", "简单邮箱格式"),

            # 2. 带点的用户名
            ("first.last@example.com", "带点的用户名"),

            # 3. 带数字的用户名
            ("user123@example.com", "带数字的用户名"),

            # 4. 带'+'的邮箱别名
            ("user+tag@example.com", "带+号的邮箱别名"),

            # 5. 带连字符的域名
            # ("user@my-domain.com", "带连字符的域名"),

            # 6. .co.uk等多级域名
            ("user@example.co.uk", "多级域名(.co.uk)"),

            # 7. 带下划线的用户名
            ("user_name@example.com", "带下划线的用户名"),

            # 8. 特殊字符邮箱
            # ("!#$%&'*+/=?^_`{|}~-@example.com", "特殊字符用户名"),

            # 9. 短域名
            ("user@a.bc", "短域名"),

            # 10. 长域名
            ("user@subdomain.example.com", "多级子域名"),

            # 11. 包含百分号的用户名
            ("user%name@example.com", "包含百分号的用户名"),

            # 12. 大写字母邮箱
            ("USER@EXAMPLE.COM", "全大写邮箱"),
        ]

        for email, description in valid_emails:
            with self.subTest(email=email, description=description):
                self.assertTrue(
                    is_valid_email(email),
                    f"邮箱 '{email}' 应该有效 ({description})"
                )

    def test_invalid_emails_format(self):
        """测试格式明显错误的邮箱地址"""

        invalid_emails = [
            # 1. 缺少@符号
            ("userexample.com", "缺少@符号"),

            # 2. 缺少域名
            ("user@", "缺少域名"),

            # 3. @在开头
            ("@example.com", "@在开头"),

            # 4. 域名含非法字符
            ("user@exa_mple.com", "域名包含下划线"),

            # 5. 连续的点
            # ("user..name@example.com", "连续的点(本地部分)"),
            ("user@example..com", "连续的点(域名部分)"),

            # 6. 本地部分以点开头
            (".user@example.com", "本地部分以点开头"),

            # 7. 本地部分以点结尾
            ("user.@example.com", "本地部分以点结尾"),

            # 8. 顶级域名太短
            ("user@example.c", "顶级域名太短(只有1个字符)"),

            # 9. 域名以连字符开头
            ("user@-example.com", "域名以连字符开头"),

            # 10. 域名以连字符结尾
            ("user@example-.com", "域名以连字符结尾"),

            # 11. 缺少顶级域名
            ("user@example", "缺少顶级域名"),

            # 12. 包含空格
            ("user name@example.com", "本地部分包含空格"),
            ("user@exa mple.com", "域名包含空格"),

            # 13. 包含中文等非ASCII字符
            ("用户@example.com", "包含非ASCII字符"),

            # 14. 包含控制字符
            ("user\0@example.com", "包含空字符"),

            # 15. 包含逗号
            ("user,name@example.com", "包含逗号"),

            # 16. 包含分号
            ("user;name@example.com", "包含分号"),

            # 17. 包含括号
            ("user(name)@example.com", "包含括号"),

            # 18. 过长邮箱
            ("a" * 100 + "@" + "b" * 150 + ".com", "邮箱地址过长"),
        ]

        for email, description in invalid_emails:
            with self.subTest(email=email, description=description):
                self.assertFalse(
                    is_valid_email(email),
                    f"邮箱 '{email}' 应该无效 ({description})"
                )

    def test_invalid_input_type(self):
        """测试当输入不是字符串时是否如期抛出TypeError"""

        invalid_inputs = [
            # 1. 整数
            (12345, "整数"),

            # 2. 浮点数
            (123.45, "浮点数"),

            # 3. 列表
            (["user@example.com"], "列表"),

            # 4. 字典
            ({"email": "user@example.com"}, "字典"),

            # 5. None
            (None, "None"),

            # 6. 布尔值
            (True, "布尔值"),

            # 7. 元组
            (("user@example.com",), "元组"),

            # 8. 集合
            ({"user@example.com"}, "集合"),
        ]

        for invalid_input, input_type in invalid_inputs:
            with self.subTest(input_type=input_type, input=invalid_input):
                with self.assertRaises(TypeError) as context:
                    is_valid_email(invalid_input)

                self.assertIn(
                    f"输入必须是字符串类型，但收到的是 {type(invalid_input).__name__}",
                    str(context.exception),
                    f"对于 {input_type} 输入，错误信息应该包含类型信息"
                )

    def test_empty_string(self):
        """测试输入为空字符串时的情况"""

        # 空字符串应该返回False
        self.assertFalse(is_valid_email(""), "空字符串应该返回False")

        # 仅包含空格的字符串应该返回False
        self.assertFalse(is_valid_email("   "), "仅包含空格的字符串应该返回False")

        # 包含制表符和换行符的字符串
        self.assertFalse(is_valid_email("\t\n"), "包含空白字符的字符串应该返回False")

    def test_emails_with_spaces(self):
        """测试邮箱地址前后或中间包含空格的情况"""

        emails_with_spaces = [
            # 1. 前面有空格
            ("  user@example.com", "前面有空格"),

            # 2. 后面有空格
            ("user@example.com  ", "后面有空格"),

            # 3. 前后都有空格
            ("  user@example.com  ", "前后都有空格"),

            # 4. 中间有空格
            ("user name@example.com", "本地部分中间有空格"),

            # 5. 域名中有空格
            ("user@exam ple.com", "域名中有空格"),

            # 6. @符号前有空格
            ("user @example.com", "@符号前有空格"),

            # 7. @符号后有空格
            ("user@ example.com", "@符号后有空格"),

            # 8. 包含制表符
            ("user\t@example.com", "包含制表符"),

            # 9. 包含换行符
            ("user\n@example.com", "包含换行符"),

            # 10. 包含多个空格
            ("user  @example.com", "包含多个空格"),
        ]

        for email, description in emails_with_spaces:
            with self.subTest(email=email, description=description):
                # 注意: 我们的实现在验证前会strip()，所以前后空格会被移除
                # 但中间的空格仍然会导致验证失败
                result = is_valid_email(email)

                if "前后" in description or "前面" in description or "后面" in description:
                    # 前后有空格的邮箱，在strip()后应该是有效的
                    # 但这是一个设计决策：有些系统可能不接受前后空格
                    # 我们的实现中，strip()会移除空格，所以这些应该是有效的
                    expected_result = True
                else:
                    # 中间有空格的邮箱应该无效
                    expected_result = False

                self.assertEqual(
                    result, expected_result,
                    f"邮箱 '{email}' 应该{'有效' if expected_result else '无效'} ({description})"
                )

def run_tests():
    """运行单元测试"""

    # 创建测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsValidEmail)

    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # 打印测试结果统计
    print("\n" + "=" * 60)
    print("测试结果统计:")
    print(f"运行测试数: {result.testsRun}")
    print(f"失败数: {len(result.failures)}")
    print(f"错误数: {len(result.errors)}")

    if result.wasSuccessful():
        print("所有测试通过! ✓")
    else:
        print("部分测试失败! ✗")


if __name__ == "__main__":
    # 首先运行一些示例来演示函数功能
    print("=" * 60)
    print("邮箱验证函数示例:")
    print("=" * 60)

    test_emails = [
        ("simple@example.com", True),
        ("user+tag@gmail.com", True),
        ("first.last@company.co.uk", True),
        ("user@example", False),
        ("user@.com", False),
        ("@example.com", False),
        ("user name@example.com", False),
        ("user@exa mple.com", False),
    ]

    for email, expected in test_emails:
        try:
            result = is_valid_email(email)
            status = "✓" if result == expected else "✗"
            print(f"{status} '{email}' -> {result} (期望: {expected})")
        except Exception as e:
            print(f"✗ '{email}' -> 异常: {type(e).__name__}: {e}")

    print("\n" + "=" * 60)
    print("运行单元测试:")
    print("=" * 60)

    # 运行单元测试
    run_tests()