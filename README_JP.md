# 単一位相同期論理回路 簡易シミュレータ  
  
## 1. **概要**  
  
**binarylogicroutine** ライブラリは、Python 上で単一位相の同期論理回路をシミュレートすることを可能にする。  
視覚障害のある学生にも利用しやすいよう設計されており、フリップフロップを用いた回路を完全なテキストベース環境でモデル化することができる。  
このライブラリは自己完結型であり、Python 以外の外部依存関係を必要としない。  
  
## 2. **使用例**  
  
### 2.1 サンプルプログラム  
  
サンプルプログラムでは、ネガティブエッジトリガの JK フリップフロップを用いた３進カウンタ回路をシミュレートしている。  
このとき状態 `(x1, x2)` は、周期的に `(0, 0) → (0, 1) → (1, 0)` と遷移する。  
  
この例では出力変数は使用しておらず、代わりにクロック信号（`clk`）と状態変数（`x1`, `x2`）を出力している。  
  
```python
# testTernaryJK.py
from binarylogicroutine import FlipFlopController

# Initial Settings
fPos = 0
print("Negative edge trigger" if fPos == 0 else "Positive edge trigger")

# Create a flip-flop controller
FFC = FlipFlopController()

# Reset the flip-flops
resetResJK = FFC.resetFF(fPos, 'JKFF', 2)  # 2: number of flip-flops
clk, x0, x1 = resetResJK[0], resetResJK[1], resetResJK[2]
print(f"Initial state -> clk={clk}, x0={x0}, x1={x1}")

# Generate 10 clock cycles and update the flip-flop states
for ir in range(10):  # Repeat for 10 clock cycles
    for ic in range(2):  # Each clock has two states (0 and 1)
        clk = 1 - clk    # Toggle the clock signal
        j0 = x1          # Input value J for JKFF0
        k0 = 1           # Input value K for JKFF0
        j1 = int(not x0) # Input value J for JKFF1 (convert bool to int)
        k1 = 1           # Input value K for JKFF1

        # Update flip-flop states
        x0 = FFC.jkff(fPos, 0, clk, j0, k0)  # JKFF0
        x1 = FFC.jkff(fPos, 1, clk, j1, k1)  # JKFF1
        print(f"clk={clk}, x0={x0}, x1={x1}")
```

### 2.2 実行結果  

```
Negative edge trigger
Initial state -> clk=0, x0=0, x1=0
clk=1, x0=0, x1=0
clk=0, x0=0, x1=1
clk=1, x0=0, x1=1
clk=0, x0=1, x1=0
clk=1, x0=1, x1=0
clk=0, x0=0, x1=0
clk=1, x0=0, x1=0
clk=0, x0=0, x1=1
clk=1, x0=0, x1=1
clk=0, x0=1, x1=0
clk=1, x0=1, x1=0
clk=0, x0=0, x1=0
clk=1, x0=0, x1=0
clk=0, x0=0, x1=1
clk=1, x0=0, x1=1
clk=0, x0=1, x1=0
clk=1, x0=1, x1=0
clk=0, x0=0, x1=0
clk=1, x0=0, x1=0
clk=0, x0=0, x1=1
```

## 3. **インストール**  

Python>=3.8   
  
```bash
pip install git+https://github.com/sekita/BinaryLogicPy.git
```
  
## 4. **使用法**  
  
- Pythonプログラムの中での記述  
```bash
from binarylogicroutine import FlipFlopController

obj = FlipFlopController()  
obj.doSomething()
```

- 実行例
```
# Ternary Counter
python testTernaryJK.py
python testTernaryD.py
python testTernarySR.py

# A simulation of a vending machine that sells 15-yen juice in a world where only 5-yen and 10-yen coins are used.
python testVM15YenJK.py
python testVM15YenD.py
python testVM15YenSR.py
```
  
## 5. **シミュレーションライブラリの詳細説明**  
  
### 5.1 制約事項  
  
フリップフロップ（FF）は、ポジティブエッジトリガまたはネガティブエッジトリガのいずれかに統一され、以下の制約が適用される：  
  
1. フリップフロップを通らないフィードバックループは禁止されている。  
2. 組合せ回路内の論理演算素子による遅延時間は考慮されない。処理はプログラム中の記述順に従って実行される。  
3. 素子に対する入力の数（fan-in）および出力の数（fan-out）に関する制限は考慮されない。  
  
### 5.2 フリップフロップの種類と ID  
  
本ライブラリでは、以下の 4 種類のフリップフロップを実装しており、それぞれ以下の関数名を用いる：  
  
* JK フリップフロップ：`JKFF`  
* SR（または RS）フリップフロップ：`SRFF` または `RSFF`  
* D フリップフロップ：`DFF`  
* T フリップフロップ：`TFF`  
  
また、各種フリップフロップには FFID（フリップフロップ識別子）として 0から99 の整数が割り当てられる。  
  
### 5.3 組合せ論理回路の作成  
  
組合せ論理回路そのものには本ライブラリは必須ではないが、順序回路内で使用する場合には必要となる。  
以下にその使用方法を説明する：  
  
論理演算は Python の論理式を用いて記述する。  
具体的には、論理積（AND）は `and`、論理和（OR）は `or`、論理否定（NOT）は `not` を用いる。  
論理変数は左辺に、論理式は右辺に記述する。複数行に分けて記述する際は、既に定義済みの値を再利用すること。  
  
例：  
  
* 単一文で記述する場合：  
  `a = b and c or d`  
  
* ２文に分けて記述する場合：  
  
  ```python
  e = b and c
  a = e or d
  ```
  
  ただし、以下のように未定義の `e` を参照することは許されない：  
  
  ```python
  a = e or d
  e = b and c
  ```
  
必要に応じて、`int()` 関数を使用することで `True` および `False` をそれぞれ `1` および `0` に変換できる。  
逆に、Python では `1` と `0` を `True` および `False` として扱うことも可能である。  
また、Python における論理演算子の優先順位は、標準の順序（`not` > `and` > `or`）に従う。  
  
### 5.4 順序論理回路の作成  
  
プログラムは通常、**初期化セクション**と、各シミュレーションサイクルごとに繰り返し実行される**クロックサイクルセクション**の 2 つの部分から構成される。  
  
#### **初期化セクション**  
  
初期化セクションでは、`FlipFlopController` クラスのインポート、エッジトリガの種類の設定、フリップフロップの初期化を行う。  
  
1. **クラスのインポート**  
  
   ```python
   from binarylogicroutine import FlipFlopController
   ```
  
2. **エッジトリガの種類を設定**  
   たとえば、エッジトリガ種別（`flagPositive`）を変数 `fPos` によって表す場合、  
   ポジティブエッジリガは `fPos = 1`、ネガティブエッジトリガは `fPos = 0` と設定する。  
  
   ```python
   fPos = 0  # 0 はネガティブエッジトリガ、1 はポジティブエッジトリガ
   ```
  
3. **フリップフロップの初期化**  
   `FlipFlopController` クラスから `FFC` というオブジェクトを生成した場合、  
   `FFC.resetFF()` 関数を用いてフリップフロップの出力を初期化できる。  
   `resetFF()` 関数の引数には、エッジトリガ種別（flagPositive）、フリップフロップの種類（ffType。5.2節に記載のいずれか）、  
   およびフリップフロップの個数（numFF）を指定する。  
  
   ```python
   FFC = FlipFlopController()
   FFC.resetFF(fPos, ffType, numFF)
   ```
  
   戻り値は、エッジトリガ直後のクロック信号（ポジティブエッジトリガなら 1、ネガティブエッジトリガなら 0）と、各フリップフロップの出力値（初期値は 0）である。  
  
#### クロックサイクルセクション  
  
1. **外部入力および論理式の設定**  
   必要に応じて外部入力を設定し、各フリップフロップの入力変数に対して、組合せ回路により求められた論理式を設定する。  
  
2. **フリップフロップ関数の呼び出し**  
   フリップフロップの関数を呼び出す。関数の引数には、エッジトリガ種別（flagPositive）、FFID、クロック信号、フリップフロップへの入力を与える。  
   戻り値は、フリップフロップの Q 出力である。  
  
   例えば、FFID 0 および 1 を持つ JK フリップフロップ（JKFF）がクロック信号 clk に同期している場合、  
   各 FF に対する入力は Jn および Kn（n = 0, 1）とし、以下のように記述する：  
  
   ```python
   newQ1 = FFC.jkff(fPos, 0, clk, J1, K1)
   newQ2 = FFC.jkff(fPos, 1, clk, J2, K2)
   ```
  
   D フリップフロップの場合：  
  
   ```python
   newQ1 = FFC.dff(fPos, 0, clk, D1)
   newQ2 = FFC.dff(fPos, 1, clk, D2)
   ```
  
   RS フリップフロップ（RSFF）の場合：  
  
   ```python
   newQ1 = FFC.rsff(fPos, 0, clk, R1, S1)
   newQ2 = FFC.rsff(fPos, 1, clk, R2, S2)
   ```
  
   SR フリップフロップ（SRFF）の場合：  
  
   ```python
   newQ1 = FFC.srff(fPos, 0, clk, S1, R1)
   newQ2 = FFC.srff(fPos, 1, clk, S2, R2)
   ```
  
   T フリップフロップ（TFF）の場合：  
  
   ```python
   newQ1 = FFC.tff(fPos, 0, clk, T1)
   newQ2 = FFC.tff(fPos, 1, clk, T2)
   ```
  
3. **出力変数の設定**  
   必要に応じて、組合せ回路から得られた論理式に基づいて出力変数の値を設定する。  
  
  
## 6. **ライセンス**  
  
本プロジェクトは MIT ライセンスの下で提供されている。詳細は LICENSE ファイルを参照されたい。  
  
## 7. **連絡先**  
  
関田 巖（SEKITA, Iwao）  
[sekita@cs.k.tsukuba-tech.ac.jp](mailto:sekita@cs.k.tsukuba-tech.ac.jp)  
