# コマンドプロンプトより「"/Users/switch/Library/Python/3.9/bin/streamlit hello"」を実行
# 「pip3 streamlit install」を実行
# /Users/switch/Library/Python/3.9/bin/streamlit run /Users/switch/Desktop/MyPython/ingredients.py

import os  # パスの操作用ライブラリ
import streamlit as st
from PIL import Image

st.markdown(
    "<h1 style='text-align: center;'>Pokémon Sleep<br>食材備蓄アシスタント</h1>", 
    unsafe_allow_html=True
)
# st.title("Pokémon Sleep 備蓄食材アシスタント")

st.markdown(
    "<p style='text-align: right;'>作成者 <a href='https://twitter.com/Rump_htjtn' target='_blank'>@Rump_htjtn</a></p>",
    unsafe_allow_html=True
)


ingredients = {
    "apple"    :0,
    "milk"     :0,
    "soybeans" :0,
    "honey"    :0,
    "meat"     :0,
    "ginger"   :0,
    "tomato"   :0,
    "egg"      :0,
    "oil"      :0,
    "potato"   :0,
    "herb"     :0,
    "corn"     :0,
    "cacao"    :0,
    "coffee"   :0,
    "mushroom" :0,
    "leek"     :0,
    "tail"     :0,}

labels = {
    "apple": "りんご", 
    "milk": "ミルク", 
    "soybeans": "大豆", 
    "honey": "ミツ", 
    "meat": "マメミート", 
    "ginger": "ジンジャー", 
    "tomato": "トマト", 
    "egg": "エッグ", 
    "oil": "オイル", 
    "potato": "ポテト", 
    "herb": "ハーブ", 
    "corn": "コーン", 
    "cacao": "カカオ", 
    "coffee": "コーヒー", 
    "mushroom": "きのこ", 
    "leek": "ネギ", 
    "tail": "シッポ"
          }

# 画像ファイルのベースパス
# image_base_path = "/Users/switch/Desktop/MyPython"

ingredient_images = {
    "ネギ": os.path.join("leek.png"),
    "きのこ": os.path.join("mushroom.png"),
    "エッグ": os.path.join("egg.png"),
    "ポテト": os.path.join("potato.png"),
    "りんご": os.path.join("apple.png"),
    "ハーブ": os.path.join("herb.png"),
    "マメミート": os.path.join("meat.png"),
    "ミルク": os.path.join("milk.png"),
    "ミツ": os.path.join("honey.png"),
    "オイル": os.path.join("oil.png"),
    "ジンジャー": os.path.join("ginger.png"),
    "トマト": os.path.join("tomato.png"),
    "カカオ": os.path.join("cacao.png"),
    "シッポ": os.path.join("tail.png"),
    "大豆": os.path.join("soybeans.png"),
    "コーン": os.path.join("corn.png"),
    "コーヒー": os.path.join("coffee.png"),
}

# recipes_curry = [
#      "めざめるパワーシチュー",
#      "れんごくコーンキーマカレー",
#      "ニンジャカレー",
#      "ぜったいねむりバターカレー",
#      "あぶりテールカレー",
#      "からくちネギもりカレー",
#      "ピヨピヨパンチ辛口カレー",
#      "じゅうなんコーンシチュー",
#      "おやこあいカレー",
#      "キノコのほうしカレー",
#      "ビルドアップマメカレー",
#      "ほっこりポテトシチュー",
#      "とけるオムカレー"
#      "サンパワートマトカレー",
#      "ひでりカツカレー",
#      "満腹チーズバーグカレー",
#      "マメバーグカレー",
#      "ベイビィハニーカレー",
#      "たんじゅんホワイトシチュー",
#      "とくせんリンゴカレー"]

# 料理順番及び食材数確認完了 2024.12.13
recipe_curry = {
     "めざめるパワーシチュー": [("soybeans", 28),("tomato", 25),("coffee", 16),("mushroom", 23)],
     "れんごくコーンキーマカレー": [("meat", 24),("ginger", 12),("herb", 27),("corn", 14)],
     "ニンジャカレー": [("soybeans", 24),("meat", 9),("mushroom", 5),("leek", 12)],
     "ぜったいねむりバターカレー": [("milk", 10),("tomato", 15),("potato", 18),("cacao", 12)],
     "あぶりテールカレー": [("herb", 25),("tail", 8)],
     "からくちネギもりカレー": [("ginger", 10),("herb", 8),("leek", 14)],
     "ピヨピヨパンチ辛口カレー": [("honey", 11),("herb", 11),("coffee", 11)],
     "じゅうなんコーンシチュー": [("milk", 8),("potato", 8),("corn", 14)],
     "おやこあいカレー": [("apple", 11),("honey", 12),("egg", 8),("potato", 4)],
     "キノコのほうしカレー": [("potato", 9),("mushroom", 14)],
     "ビルドアップマメカレー": [("soybeans", 12),("meat", 6),("egg", 4),("herb", 4)],
     "ほっこりポテトシチュー": [("milk", 10),("potato", 8),("mushroom", 4)],
     "とけるオムカレー": [("tomato", 6),("egg", 10)],
     "サンパワートマトカレー": [("tomato", 10),("herb", 5)],
     "ひでりカツカレー": [("meat", 10),("oil", 5)],
     "満腹チーズバーグカレー": [("milk", 8),("meat", 8)],
     "マメバーグカレー": [("meat", 7)],
     "ベイビィハニーカレー": [("honey", 7)],
     "たんじゅんホワイトシチュー": [("milk", 7)],
     "とくせんリンゴカレー": [("apple", 7)],
}
# 料理順番及び食材数確認完了 2024.12.13
recipe_salad = {
     "まけんきコーヒーサラダ": [("meat" , 28),("oil", 22),("potato" , 22),("coffee" , 28)],
     "ニンジャサラダ": [("soybeans" , 19),("ginger" , 11),("mushroom" , 12),("leek" , 15)],
     "ワカクササラダ": [("apple" , 14),("potato" , 9),("oil" , 22),("corn" , 17)],
     "クロスチョップドサラダ": [("meat" , 15),("tomato" , 10),("egg" , 20),("corn" , 11)],
     "ヤドンテールのペッパーサラダ": [("oil" , 15),("herb" , 10),("tail" , 10)],
     "めいそうスイートサラダ": [("apple" , 21),("honey" , 16),("corn" , 12)],
     "キノコのほうしサラダ": [("tomato" , 8),("oil" , 8),("mushroom" , 17)],
     "オーバーヒートサラダ": [("ginger" , 10),("tomato" , 8),("herb" , 17)],
     "くいしんぼうポテトサラダ": [("apple" , 6),("meat" , 7),("egg" , 9),("potato" , 14)],
     "ムラっけチョコミートサラダ": [("meat" , 9),("cacao" , 14)],
     "うるおいとうふサラダ": [("soybeans" , 15),("tomato" , 9)],
     "ばかぢからワイルドサラダ": [("meat" , 9),("ginger" , 6),("egg" , 5),("potato" , 3)],
     "モーモーカプレーゼ": [("milk" , 12),("tomato" , 6),("oil" , 5)],
     "みだれづきコーンサラダ": [("oil" , 8),("corn" , 9)],
     "めんえきネギサラダ": [("ginger" , 5),("leek" , 10)],
     "メロメロりんごのチーズサラダ": [("apple" , 15),("milk" , 5),("oil" , 3)],
     "ねっぷうとうふサラダ": [("soybeans" , 10),("herb" , 6)],
     "ゆきかきシーザーサラダ": [("milk" , 10),("meat" , 6)],
     "あんみんトマトサラダ": [("tomato" , 8)],
     "マメハムサラダ": [("meat" , 8)],
     "とくせんリンゴサラダ": [("apple" , 8)],
}
# 料理順番及び食材数確認完了 2024.12.13
recipe_drink = {
     "スパークスパイスコーラ": [("apple" , 35),("ginger" , 20),("coffee" , 12),("leek" , 20)],
     "フラワーギフトマカロン": [("milk" , 10),("honey" , 17),("egg" , 25),("cacao" , 25)],
     "おちゃかいコーンスコーン": [("apple" , 20),("milk" , 9),("ginger" , 20),("corn" , 18)],
     "プリンのプリンアラモード": [("apple" , 10),("milk" , 10),("honey" , 20),("egg" , 15)],
     "はやおきコーヒーゼリー": [("milk" , 14),("honey" , 12),("coffee" , 16)],
     "だいばくはつポップコーン": [("milk" , 7),("oil" , 14),("corn" , 15)],
     "ちからもちソイドーナツ": [("soybeans" , 16),("oil" , 12),("cacao" , 7)],
     "ネロリのデトックスティー": [("apple" , 15),("ginger" , 11),("mushroom" , 9)],
     "ふくつのジンジャークッキー": [("honey" , 14),("ginger" , 12),("egg" , 4),("cacao" , 5)],
     "あくまのフルーツキッスオレ": [("apple" , 11),("milk" , 9),("honey" , 7),("cacao" , 8)],
     "はなびらのまいタルト": [("apple" , 11),("cacao" , 11)],
     "あまいかおりのチョコケーキ": [("milk" , 7),("honey" , 9),("cacao" , 8)],
     "はりきりプロテインスムージー": [("soybeans" , 15),("cacao" , 8)],
     "おおきいマラサダ": [("milk" , 7),("honey" , 6),("oil" , 10)],
     "かるわざソイケーキ": [("soybeans" , 7),("egg" , 8)],
     "マイペースやさいジュース": [("apple" , 7),("tomato" , 9)],
     "ひのこのジンジャーティー": [("apple" , 7),("ginger" , 9)],
     "じゅくせいスイートポテト": [("milk" , 5),("potato" , 9)],
     "ねがいごとアップルパイ": [("apple" , 12),("milk" , 4)],
     "クラフトサイコソーダ": [("honey" , 9)],
     "とくせんリンゴジュース": [("apple" , 8)],
     "モーモーホットミルク": [("milk" , 7)],
}


# 料理回数セレクトボックス（カテゴリごと）
def recipe_selector(key, recipe_category, max_count):
    col1, col2 = st.columns([4, 1])
    with col1:
        recipe = st.selectbox(
            "",
            ["リストから選択"] + list(recipe_category.keys()),
            key=f"recipe_{key}",
            index=0
        )
    with col2:
        # 最大値を設定（合計回数制限）
        count = st.number_input("", min_value=0, max_value=max_count, step=1, key=f"count_{key}", value=0)
    return recipe, count

# 各カテゴリの動的セレクトボックスの管理
def dynamic_recipe_selector(recipe_category, key_prefix, max_count):
    selected_recipes = []
    counts = []
    num_selectors = st.session_state.get(f"{key_prefix}_num_selectors", 1)  # デフォルトで1つ表示
    total_count = 0  # カテゴリ内の合計回数を追跡

    for i in range(1, num_selectors + 1):
        recipe, count = recipe_selector(key=f"{key_prefix}_{i}", recipe_category=recipe_category, max_count=max_count - total_count)
        if recipe != "リストから選択":
            selected_recipes.append(recipe)
            counts.append(count)
            total_count += count  # 合計回数に追加

    # 新しいセレクトボックスを追加する条件
    if selected_recipes and len(selected_recipes) == num_selectors:
        st.session_state[f"{key_prefix}_num_selectors"] = num_selectors + 1

    return selected_recipes, counts

# 折りたたみ可能なカテゴリ
with st.expander("カレー・シチュー", expanded=True):
    recipes_selected_curry, cooking_counts_curry = dynamic_recipe_selector(recipe_curry, "curry", 21)

with st.expander("サラダ", expanded=True):
    recipes_selected_salad, cooking_counts_salad = dynamic_recipe_selector(recipe_salad, "salad", 21)

with st.expander("デザート・ドリンク", expanded=True):
    recipes_selected_drink, cooking_counts_drink = dynamic_recipe_selector(recipe_drink, "drink", 21)



# 食材の加算
all_selected_recipes = {
    "カレー・シチュー": (recipes_selected_curry, cooking_counts_curry, recipe_curry),
    "サラダ": (recipes_selected_salad, cooking_counts_salad, recipe_salad),
    "デザート・ドリンク": (recipes_selected_drink, cooking_counts_drink, recipe_drink),
}

# カテゴリごとの食材合計を計算する関数
def calculate_max_ingredients(selected_recipes, counts, recipe_data):
    ingredient_totals = {}  # 各カテゴリ内での合計値を保存する辞書
    for recipe, count in zip(selected_recipes, counts):
        for ingredient, amount in recipe_data[recipe]:
            if ingredient not in ingredient_totals:
                ingredient_totals[ingredient] = 0
            ingredient_totals[ingredient] += amount * count
    return ingredient_totals


# 各カテゴリごとに食材数を計算
ingredient_totals_curry = calculate_max_ingredients(recipes_selected_curry, cooking_counts_curry, recipe_curry)
ingredient_totals_salad = calculate_max_ingredients(recipes_selected_salad, cooking_counts_salad, recipe_salad)
ingredient_totals_drink = calculate_max_ingredients(recipes_selected_drink, cooking_counts_drink, recipe_drink)

# 全カテゴリの食材最大値を統合
final_ingredient_totals = {}

all_categories = [ingredient_totals_curry, ingredient_totals_salad, ingredient_totals_drink]
for category_totals in all_categories:
    for ingredient, total in category_totals.items():
        if ingredient not in final_ingredient_totals:
            final_ingredient_totals[ingredient] = 0
        # カテゴリ間での最大値を保存
        final_ingredient_totals[ingredient] = max(final_ingredient_totals[ingredient], total)


# 現在の食材の個数を表示
st.subheader("準備する食材:")
non_zero_ingredients = {key: count for key, count in final_ingredient_totals.items() if count > 0}

if non_zero_ingredients:
    # グリッドの作成
    cols = st.columns(6)  # 6つの列を作成
    col_index = 0  # 現在の列インデックス


    # カスタム順序で指定
    custom_order = ['leek','mushroom','egg','potato','apple','meat','herb','milk','honey','oil','ginger','tomato',
                    'cacao','tail','soybeans','corn','coffee']  # 例: 自分の希望する順番に並べる
    sorted_ingredients = [(ingredient, non_zero_ingredients[ingredient]) for ingredient in custom_order if ingredient in non_zero_ingredients]

    for ingredient, count in sorted_ingredients:
        # 該当食材の画像が存在する場合に表示
        if labels[ingredient] in ingredient_images:
            image_path = ingredient_images[labels[ingredient]]
            # ファイルが存在するかを確認
            if os.path.exists(image_path):
                # PILで画像を開く
                img = Image.open(image_path)

                # 現在の列に画像とキャプションを表示
                with cols[col_index]:
                    st.image(img, use_container_width=True)
                    # キャプションをスタイル付きで表示
                    st.markdown(
                        f"<div style='text-align: center; font-size: 22px; font-weight: bold; color: black;'>{count}個</div>",
                        unsafe_allow_html=True
                    )
                    st.markdown("<br><br>", unsafe_allow_html=True)
                col_index = (col_index + 1) % 6
            else:
                st.warning(f"画像が見つかりません: {image_path}")
else:
    st.write("")


st.subheader("作成できる料理:")

# 料理カテゴリと選択された料理を表示
all_selected_recipes = {
    "カレー・シチュー": (recipes_selected_curry, cooking_counts_curry, recipe_curry),
    "サラダ": (recipes_selected_salad, cooking_counts_salad, recipe_salad),
    "デザート・ドリンク": (recipes_selected_drink, cooking_counts_drink, recipe_drink),
}

for category, (selected_recipes, counts, _) in all_selected_recipes.items():
    if selected_recipes:  # 料理が選択されている場合のみ表示
        # 料理カテゴリ名を表示
        st.write(f"**{category}**")

        # 選択された料理とその数を表示（インデント）
        for recipe, count in zip(selected_recipes, counts):
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;{recipe}： {count}回", unsafe_allow_html=True)



# 全ての食材の最大数を計算して表示
total_count = sum(final_ingredient_totals.values())

# 1行の改行を挟む
st.markdown("<br>", unsafe_allow_html=True)

# 「合計 n 個」の表示を右揃えにする
st.markdown(f"<div style='text-align: right;'>合計 {total_count} 個</div>", unsafe_allow_html=True)

# 2行の改行を挟む
st.markdown("<br><br>", unsafe_allow_html=True)

# バッグ容量を設定するシークバー
bags = st.slider("食材バッグ容量", 100, 700, 700, step=20)


# バッグ容量を超えた場合に警告を中央揃えで表示
if total_count > bags:
    st.markdown(
        "<p style='text-align: center;'>⚠️ バッグから食材が溢れています！手に入れやすい食材は翌週に調達しましょう ⚠️</p>",
        unsafe_allow_html=True
    )

