from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import dump

"""
[['私','は','人間',だ'],
 ['犬','の','世話','が','大変'],
]
すでに語分割された文書のリストのリストを引数として与える

分割された文字列をスペースでくっつける
['西洋', 'の', '料理'] -> ['西洋 の 料理']

tf-idfを用いたベクトル化
vectors.joblibファイルへオブジェクトを保存

使用するときはjoblibのloadで呼び出す
from jobilb import load
vectors = load('vectors.joblib')
"""


def serialize_tfidf_model(tokenized_division_documents_list: str):
    tfidf = TfidfVectorizer(use_idf=True, token_pattern="(?u)\\b\\w+\\b")
    # division_documents_list_joined = [" ".join(doc) for doc in division_documents_list]
    # print("division_documents_list_joined", division_documents_list_joined)
    # tfidfモデルの作成
    tfidf_model = tfidf.fit(tokenized_division_documents_list)

    dump(tfidf_model, "tfidf_model.joblib")

    # tfidfベクトルに変換
    # vectors = tfidf_model.transform(division_documents_list_joined).toarray()
    # dump(vectors, "vectors.joblib")


def tokenizer_documents_list(division_documents_list):
    """
       [['私','は','人間',だ'],
     ['犬','の','世話','が','大変'],
    ]
    すでに語分割された文書のリストのリストを引数として与える

    分割された文字列をスペースでくっつける
    ['西洋', 'の', '料理'] -> ['西洋 の 料理']

    入力: 単語のリストのリスト
    出力: 文字列のリスト
    """
    return [" ".join(doc) for doc in division_documents_list]
