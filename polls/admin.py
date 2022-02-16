from django.contrib import admin
from .models import Question

# Register your models here.

# ところで、 polls アプリはどこにあるんでしょう？ admin のインデックスページを見ても表示されていませんね。
# やるべきことは1つです:
#   Question オブジェクトがadmin インタフェースを持つということを、adminに伝える必要があります。
#   これを行うために、ファイル polls/admin.py を開いてこのように編集しましょう
admin.site.register(Question)