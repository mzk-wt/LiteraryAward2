import shutil
import os
import json
from jinja2 import Environment, FileSystemLoader
from generator import RestPageGenerator, JsonGenerator

## jinja2用の環境設定
env = Environment(
    loader = FileSystemLoader('templates', encoding='utf8'),
    trim_blocks = True
)

## ページ作成
def generate():
    # 出力先フォルダをクリア
    shutil.rmtree('output')
    os.mkdir('output')
    os.mkdir('output/json')
    os.mkdir('output/json/awarddetail')
    os.mkdir('output/json/bookdetail')
    os.mkdir('output/json/authordetail')
    os.mkdir('output/rest')
    os.mkdir('output/rest/bookdetail')

    # JSONデータ作成
    JsonGenerator.generate(env)

    # ページ作成
    RestPageGenerator.generate(env)

if __name__ == '__main__':
    generate()
