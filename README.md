# リクエストに対してレスポンスを返す。

## リクエストの処理順番

1. config/urls.py
2. blog/urls.py
3. どの関数orクラスを発火させるか判定
4. 関数内で処理しreturn