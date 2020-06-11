# 蟻本2-2貪欲法の類題

* [AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)

## 例題 2-2-1　硬貨の問題

### [JOI 2007 予選 A おつり](https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_a)


## 例題 2-2-2　区間スケジューリング問題

* 区間スケジューリングの典型コード

```python
N, M = [int(item) for item in input().split()]
bridges = [[int(item) for item in input().split()] for _ in range(M)]

bridges = sorted(bridges, key=lambda x:x[1])
#終点が早い順に並び替える

res = 1 #数を数えるので最初は必ず1

prev = bridges[0][1] #index=0の終点を設定
for a, b in bridges: 
    # a始点　b終点 index=0は自動で弾かれる
    if a >= prev:
        res +=1 #重複しない数の数え上げ
        prev = b

print(res)

```


### [キーエンス プログラミング コンテスト 2020 B - Robot Arms](https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b)


#### 方針

* 「重ならないように」なので区間スケジューリング法を使う
  * 各点の始点と終点を算出する
  * 各点を終点が早い順にソートする
  * 現在の終点がおわるまで、次のロボットを選ばない

#### 実装

* 各点を始点と終点のリストに書きなおす
* `sorted()`で終点をkeyにソートする
* 先頭の終点を最初の閾値にして、次の始点が終点を超えるか調べる
* 最悪一つは残るのでカウンターの初期値は１にする

### [ABC103D - Islands War](https://atcoder.jp/contests/abc103/tasks/abc103_d)

#### 方針

* 争っている島の間の橋を取り除けば要望を満たせる
* 同じ区間をまたいで争っている島たちがあるのならば、その区間の橋を一つ壊せば良い
* つまり同じ区間を有する組み合わせは無視できる
* 上記制約の見方を変えると、他のと重複しない区間で争っている島の組み合わせがあるのならば、その区間の橋を壊さないといけない。
* 争いをなくすためには、通ずる橋をすべて破壊する必要があるから、区間が重複しない組み合わせ数の最大を選ぶ必要がある。
* よって、この問題は区間スケジューリングに帰結できる。
* 念のため題意を満たすか確認する
  * 他と重複しない区間の組み合わせ数の最大（※）を見つける。
  * それらの間の橋を一つずつ壊す
  * ※の組み合わせのどれかに重複する争いは、必ず一つ以上の壊れた橋を挟む
  * よって、題意を満たす

#### 実装

* 特に工夫無し
* 区間スケジューリングだと分かる事が大事な問題だった


### [ABC038D-プレゼント]](https://atcoder.jp/contests/abc038/tasks/abc038_d)

#### 方針

* ギブ
* BITを使わないと解けないらしい・・・ﾅﾆｿﾚ


## 例題 2-2-3 Best Cow Line (POJ No.3617)

### [ABC 076 C Dubious Document 2](https://atcoder.jp/contests/abc076/tasks/abc076_c)

