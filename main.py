import sys
import random

def get_valid_input(prompt, min_val=None, max_val=None):
    while True:
        sys.stdout.buffer.write(prompt.encode('utf-8'))
        sys.stdout.flush()
        try:
            value = int(sys.stdin.buffer.readline().decode().strip())
            if (min_val is None or value >= min_val) and (max_val is None or value <= max_val):
                return value
            sys.stdout.buffer.write(f"{min_val}から{max_val}の間の数字を入力してください。\n".encode('utf-8'))
        except ValueError:
            sys.stdout.buffer.write("有効な整数を入力してください。\n".encode('utf-8'))
        sys.stdout.flush()

def write_and_flush(message):
    sys.stdout.buffer.write(message.encode('utf-8'))
    sys.stdout.flush()

# ユーザーから範囲を取得
n = get_valid_input("最小値を入力してください: ")
m = get_valid_input(f"最大値を入力してください（{n}以上）: ", min_val=n)

# ランダムな数字を生成してゲームをセットアップ
target = random.randint(n, m)
max_attempts = 10
write_and_flush(f"{n}から{m}の間の数字を選びました。当ててみてください！\n")

# メインのゲームループをします
for attempt in range(1, max_attempts + 1):
    guess = get_valid_input(f"試行 {attempt}/{max_attempts}. 予想を入力してください: ")
    
    if guess == target:
        write_and_flush(f"おめでとうございます！{attempt}回目で数字を当てました。\n")
        sys.exit(0)
    
    hint = "小さすぎます！もう一度。\n" if guess < target else "大きすぎます！もう一度。\n"
    write_and_flush(hint)

write_and_flush(f"残念ですが、試行回数を使い切りました。正解は{target}でした。\n")
