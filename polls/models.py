'''
いずれも django.db.models.Model のサブクラスです.
各モデルには複数のクラス変数があり、個々のクラス変数はモデルのデータベースフィールドを表現しています。
Field インスタンスそれぞれの名前(例: question_text や pub_date)は、機械可読なフィールド名です。
このフィールド名はPythonコードで使うとともに、データベースも列の名前として使うことになります。
このファイルは、テキストデーたや値を扱うぷろぐらむ
'''

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    ''' 
    Field クラスの中には必須の引数を持つものがあります。
    例えば CharField には max_length を指定する必要があります。
    この引数はデータベーススキーマで使われる他、後で述べるバリデーションでも使われます。
    上の例では、 Question.pub_date にだけ人間可読なフィールド名を指定しました。
    モデルの他のフィールドでは、フィールドの機械可読な名前は人間可読な名前としても十分なので定義していません。
    '''
    question_test = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_test

    def was_publishd_recently(self):
        return self.pub_date >= timezone.now()

datetime.timedelta(days=1)

class Choice(models.Model):
    '''
    最後に、 ForeignKey を使用してリレーションシップが定義されていることに注目してください。
    これは、それぞれの Choice が一つの Question に関連付けられることを Django に伝えます。 
    Django は 多対一、多対多、そして一対一のような一般的なデータベースリレーションシップすべてをサポートします。
    '''
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    '''
    テキストを出力する際、オブジェクトではなく、値自身を返すメソッド
    '''
    def __str__(self):
        return self.choice_test
    
