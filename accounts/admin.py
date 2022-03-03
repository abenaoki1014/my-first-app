from django.contrib import admin

# CustomUserをインポート
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    '''
    管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    # レコード一覧にidとusernameを表示
    list_display = ('id', 'username')
    # 表示するカラムにリンクを表示
    list_display_link = ('id', 'username')

# Django管理サイトにCustomUser, CustomUserAdminを追加する
admin.site.register(CustomUser, CustomUserAdmin)
