#!/usr/bin/python3
#
import cgi
import cgitb
import os

#--------------------------------------------

cgitb.enable()
form = cgi.FieldStorage()
# mode の値を取得して変数にセット
# mode が不定値の際は、0を入れる
if 'mode' not in form:
    mode = '0'
else:
    mode = form.getfirst('mode')

#-------------------------------------------- LED点灯、消灯
cmd = './cgi-bin/kadai02_sample3.py ' + mode
os.system(cmd)

#-------------------------------------------- ブラウザに送るHTMLのデータ
print("Content-Type: text/html")
print()

htmlText = '''
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
</head>
<body bgcolor="lightyellow">
    <h1>IO31 KADAI03 Python CGI test</h1>
    <table cellpadding="10">
    <tr>
        <td>
        <form method="get" action="/cgi-bin/index.py">
        <input type="submit" id="G" value=" 在籍 ">
        <input type="hidden" name="mode" value="4">
        </form>
        </td>
        
        <td>
        <form method="get" action="/cgi-bin/index.py">
        <input type="submit" id="R" value=" 離席 ">
        <input type="hidden" name="mode" value="1">
        </form>
        </td>
        
        <td>
        <form method="get" action="/cgi-bin/index.py">
        <input type="submit" id="Y" value=" 校外 ">
        <input type="hidden" name="mode" value="2">
        </form>
        </td>
        
        <td>
        <form method="get" action="/cgi-bin/index.py">
        <input type="hidden" name="mode" value="0">
        <input type="submit" id="Z" value=" 帰宅 ">
        </form>
        </td>
          
        <td>
        <form method="get" action="/cgi-bin/index.py">
        <input type="submit" id="L" value=" レインボータイム ">
        <input type="hidden" name="mode" value="4649">
        </form>
        </td>
    </tr>
    </table>
<script>
mode = ''' + mode + ''';
document.getElementById("G").style.backgroundColor = "";
document.getElementById("Y").style.backgroundColor = "";
document.getElementById("R").style.backgroundColor = "";
document.getElementById("L").style.backgroundColor = "";
switch(mode) {
    case 4: // 緑ボタン処理
            document.getElementById("G").style.backgroundColor = "#00ff00";
            break;
    case 2: // 黄ボタン処理
            document.getElementById("Y").style.backgroundColor = "#ffff00";
            break;
    case 1: // 赤ボタン処理
            document.getElementById("R").style.backgroundColor = "#ff0000";
            break;
    case 4649: // レインぼボタン処理
            document.getElementById("L").style.backgroundColor = "#ffffff";
            break;        
}
</script>
</body>
</html>
'''

print(htmlText)
