# vscode-django-note

 如何使用 VScode 執行 Django 📝

* [(等待新增)Youtube Tutorial PART 1 - 如何使用 VScode 執行 Django - 基本篇](XXX)

* [(等待新增)Youtube Tutorial PART 2 - 如何使用 VScode 執行 Django Testing](XXX)

* [(等待新增)Youtube Tutorial PART 3 - 如何使用 VScode 執行 Django - 安裝 pylint_django ](XXX)

## 教學

### 安裝環境

建議大家先閱讀以下這篇文章 ( 假如你沒用 VScode 寫過 Python )，

[Visual Studio Code Python 基本設定篇](https://youtu.be/tS4beaq9ies)

安裝 [requirements.txt](requirements.txt)

> pip install -r requirements.txt

安裝 VScode Python 套件

![alt tag](https://i.imgur.com/5lZFm5f.png)

### 設定 Django Debug

選取 `Debug > Add Configuration`，會跳出 [launch.json](https://github.com/twtrubiks/vscode_django_note/blob/master/.vscode/launch.json)，

![alt tag](https://i.imgur.com/42G2mFL.png)

這邊是預設的設定，其他更詳細的設定可參考 [tutorial-django](https://code.visualstudio.com/docs/python/tutorial-django)。

### 執行 Django Debug

選取 `Debug > Start Debugging` 或是 F5 開始 Debug

![alt tag](https://i.imgur.com/o75KTkt.png)

成功執行

![alt tag](https://i.imgur.com/zdkvmfS.png)

### Vscode 設定中斷點

中斷點也很簡單，在需要中斷的地方點一下，會有一個紅色的點。

![alt tag](https://i.imgur.com/1QDe6bM.png)

左邊可以看目前的變數，下方的 DEBUG CONSOLE 也很好用，

可以在這邊輸入你想執行的程式。

### 設定 Django Testing

在 Django 中執行 Testing 的指令為

> python manage.py test

如果我只想單純對某個資料夾 ( 例如 musics ) 底下跑 testing

> python manage.py test musics

更多詳細可參考

[Writing and running tests](https://docs.djangoproject.com/en/2.2/topics/testing/overview/)

這邊有一個簡單的 [musics/test.py](https://github.com/twtrubiks/vscode_django_note/blob/master/musics/tests.py)，

該如何設定讓他執行呢 ?

當然，可以直接在命令列下指令，可是我希望整合 VSCode，

回到剛剛前面介紹的 [launch.json](https://github.com/twtrubiks/vscode_django_note/blob/master/.vscode/launch.json)，

在這邊只需要再加一個即可 args 的部分改成 test，

就相當於是執行，

> python manage.py test

![alt tag](https://i.imgur.com/MCbvVJ9.png)

儲存後，如果你點選下方，你會發現你多了一個選項 ( Django Test )

![alt tag](https://i.imgur.com/1mXqm4b.png)

選擇 Django Test 就會開始跑 Testing 了

![alt tag](https://i.imgur.com/msP7Uzm.png)

延伸思考，假如我現在希望跑 Testing 的時候，我想要中斷點到 Django 的某一行，

這時候該如何設定呢 ?

其實也很簡單，就是先執行 Django ( 設定中斷點 )，然後再執行 Django Test 即可。

( 這邊請注意，請開兩個 Terminal 分別執行 Django 以及 Django Test ，

如果不了解介紹看影片說明)

![alt tag](https://i.imgur.com/oCQSp0F.png)

### 設定 pylint_django

之前再 [Visual Studio Code Python 基本設定篇](https://youtu.be/tS4beaq9ies) 這篇有教大家

`pip install pylint`，但這邊卻是要 `pip install pylint_django`，原因是因為如果

只安裝 pylint，自己定義的 ORM 很多會出現在 PROBLEMS 裡面，

![alt tag](https://i.imgur.com/9Sp7g4Z.png)

所以要安裝 pylint_django 修正他，安裝完之後須再 [settings.json](https://github.com/twtrubiks/vscode_django_note/blob/master/.vscode/settings.json) 加上

```json
"python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
    ]
```

儲存之後，你就會發現被修正了 ( 剛剛的錯誤消失了 )，

然後底下會有一些 pylint 的建議。

![alt tag](https://i.imgur.com/uHaLSBH.png)

更多 pylint_django 說明可參考 [pylint_django](https://github.com/PyCQA/pylint-django)。

## 執行環境

* Python 3.6.6

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

[Thank-you-for-donate](https://github.com/twtrubiks/Thank-you-for-donate)

## License

MIT license
