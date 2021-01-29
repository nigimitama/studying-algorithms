# [AtCoder Programming Guide for beginners (APG4b) - AtCoder](https://atcoder.jp/contests/apg4b)



## 「おまじない」部分について

[B - 1.01.出力とコメント](https://atcoder.jp/contests/apg4b/tasks/APG4b_b)


```cpp
#include <bits/stdc++.h>
using namespace std;
```

### #include <bits/stdc++.h>

`#include `はC++の機能を「全て」読み込むための命令です。例えばすでに紹介した`cout`や`endl`は`#include `によって読み込まれた機能です。 今後の解説で出てくるC++の機能の多くは`#include `と書くことで利用できるようになります。これを書かずに読み込みが必要な機能を使った場合、エラーが発生します。

機能は個別に読み込むこともできます。このページで用いた`cout`と`endl`だけであれば、`#include `と書くことによって読み込めます。
ただし、はじめのうちは機能の読み込み忘れによるエラーで詰まってしまうことがよくあるので、`#include `を使って一括で読み込むことをおすすめします。

### using namespace std;

`using namespace std;`はプログラムを短く書くための機能です。`#include`で読み込んだC++の機能を利用するためには、通常は`std::cout`や`std::endl`のように`std::`をはじめに付ける必要があります。 `using namespace std;`を利用すると、この`std::`を省略して書くことができます。


## 標準出力

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
  cout << "Hello, world!" << endl;
}
```

# 関数

## sort

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    vector<int> v = {1, 5, 2, 3, 4};
    // std::sortでは、greater<int>を利用することで降順にソートできる
    sort(v.begin(), v.end(), greater<int>());
    for (int i=0; i < v.size(); i++) {
        cout << v.at(i) << endl;
    }
}
```


# collection

## 連想配列（map）
http://vivi.dyndns.org/tech/cpp/map.html

> map は C++標準ライブラリに含まれており、「#include <map>」を記述することで利用可能になる。

> 名前空間は「std」なので、使用の度に「std::」を前置するか、または「using namespace std;」を記述しておく。

```cpp
#include <map>       // ヘッダファイルインクルード
using namespace std;         //  名前空間指定
int main()
{
  // map<キー型, 値型> オブジェクト名;　と宣言する
    map<string, int> mp;       // 変数mp を生成　（文字列 → 整数の連想配列）
    mp["a"] = 1;
    cout << mp["a"] << endl;  // 値の取得
}
```

