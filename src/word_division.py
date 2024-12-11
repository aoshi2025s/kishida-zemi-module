from janome.tokenizer import Tokenizer  # type: ignore

t = Tokenizer()

"""
token.surface(表層形)
token.part_of_speech(品詞)
token.base_form(基本形、見出し語)
token.reading(読み)
"""
"""
「アキラは犬の散歩に出かけた」のような一文を形態素解析し、そのlistを返す
['アキラ', 'は', '犬', 'の', '散歩', 'に', '出かけ', 'た']
"""


def division_documents(document):
    # [token.suface for token in t.tokenize(document)]
    return list(t.tokenize(document, wakati=True))


def division_documents_to_pos(document):
    return [token.part_of_speech.split(",")[0] for token in t.tokenize(document)]


def pure_division_documents(document):
    return [token for token in t.tokenize(document)]


"""
特定の品詞のみをリストアップして分かちがき
pos_list = ['名詞', '動詞', '形容詞', '助動詞', '助詞', '副詞']
"""


def division_documents_by_pos(
    document, pos_list=["名詞", "助詞", "形容詞", "助動詞", "助詞", "副詞"]
):
    return [
        token.surface
        for token in t.tokenize(document)
        if any(token.part_of_speech.startswith(pos) for pos in pos_list)
    ]


"""
前処理
全角を半角に
正規表現でHTMLタグを消去(空文字列で置換)
名詞のみを抽出してアルファベットを小文字化
surfaceのみ抽出
複合名詞化 '日本国' '憲法' -> '日本国憲法'
"""

from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *


def advance_division_document(
    document, pos_list=["名詞", "動詞", "形容詞", "助動詞", "助詞", "副詞"]
):
    char_filters = [UnicodeNormalizeCharFilter(), RegexReplaceCharFilter("<.*?>", "")]
    token_filters = [
        CompoundNounFilter(),
        POSKeepFilter(pos_list),
        LowerCaseFilter(),
        ExtractAttributeFilter("surface"),
    ]
    a = Analyzer(char_filters=char_filters, token_filters=token_filters)
    return [token for token in a.analyze(document)]
