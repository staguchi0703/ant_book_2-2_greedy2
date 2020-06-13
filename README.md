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

#### 方針

* 辞書順で最初のものを見つけるので、？はなるべく残してaとする
* 上記を実現するために、文字を反転して後ろからマッチングを行う
* 探される文字列（S'）を探す文字列（T）の長さだけ切り出して合致するか判定する。

#### 実装

* 探される文字列（S'）が探す文字列（T）より短いと解にならないから場合分けする
* 探される文字列と探す文字列の長さの差をインデックスにループを回したいから`for i in range(len(S'[::-1]) - len(T[::-1]) + 1):`とする。
  * index=0でループを回すには`range(1)`でなければならない。
  * `range(0)`だとループを回せないので注意



### [ABC007B自書式順序](https://atcoder.jp/contests/abc007/tasks/abc007_2)

#### 方針

* 考えることなし

### [ABC009C](https://atcoder.jp/contests/abc009/tasks/abc009_3)

#### 方針

* 問題文の解説見ても頭に入って来ないのでパス

## 例題 2-2-4　Saruman's Army (POJ No.3069)

### [ABC083C Multiple Gift](https://atcoder.jp/contests/abc083/tasks/arc088_a)

#### 方針

* ~~そんなプレゼントは貰ってもうれしくない。。。~~
* 倍数である　＆　数列長さの最大を求めるだから2倍の等比数列で考える

#### 実装工夫なし


### [ARC006C-積み重ね](https://atcoder.jp/contests/arc006/tasks/arc006_3)

#### 方針

* 荷物リストの先頭は確実に床に置くこととなる
* 荷物は順番に運び込まれないといけないが、床に置くのが確定したタイミングでカウントすればよい
* 床に置くと確定できるのはリストを検索するときに最初に並んでいる物のみ
* その他の荷物は軽ければ最初の荷物の上における場合がある
* リストを検索して最初の荷物に載せられるものをきめておくことができる
* 載せられないものはそのままリストに残すしかない
* 上記に気が付くと以下の方法で解ける
  * 荷物リストの並び順先頭を床に置く
  * 残りの荷物を順に検索して、床においた荷物に載せられるか判定する
  * 載せられるなら、載せられる荷物の閾値を更新して、その荷物はリストから除く
  * 最後まで探索したら、リストの最初から同じ処理を繰り返す

#### 実装

* 荷物リストをqueで持ちたくなったが、最初の荷物の上におけるかどうか探索することになるのでlistで持つ
* 載せられるか探索中に、載せられるものをみつけらたらリストから削除するのだが、ループ中のリストを変更するとループがバグるので注意
  * [公式8.3 for文](https://docs.python.org/ja/3/reference/compound_stmts.html)

  * どういうことかというと
    * これはバグる
    
      ```python:bug.py
      for i in weights:
        if temp >= i:
            weights.remove(i)
            temp = i
      ```

    * バグを回避しようと思うとこう書きたくなる

      ```python:no_good.py
      for i in range(len(weights)):
          if temp >= weights[i]:
            memo.append(weights[i])
            temp = weights[i]
      for item in memo:
          weights.remove(item)
      ```

    * 公式を参照して書くとすっきり書ける

      ```python:beautiful.py
      for i in weights[:]:
        if temp >= i:
            weights.remove(i)
            temp = i
      ```

