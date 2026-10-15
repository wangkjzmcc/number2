from datetime import datetime
import random


def get_greeting(hour: int) -> str:
    if 5 <= hour < 9:
        period = "早上好"
    elif 9 <= hour < 12:
        period = "上午好"
    elif 12 <= hour < 14:
        period = "中午好"
    elif 14 <= hour < 18:
        period = "下午好"
    elif 18 <= hour < 23:
        period = "晚上好"
    else:
        period = "夜深了"

    extras = [
        "愿你今天心情愉快！",
        "今天也是元气满满的一天！",
        "记得多喝水哦！",
        "写代码顺利，没有 bug！",
        "别忘了起来活动一下！",
    ]
    return f"{period}，{random.choice(extras)}"


def main() -> None:
    now = datetime.now()
    print("Hello, World!")
    print(f"现在是：{now.strftime('%Y-%m-%d %H:%M:%S')} 星期{'一二三四五六日'[now.weekday()]}")
    print(get_greeting(now.hour))


if __name__ == "__main__":
    main()
