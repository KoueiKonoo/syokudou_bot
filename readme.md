# 産技高専のための食堂メニュー配信BOT
- このBOTは、産業技術高等専門学校の食堂メニューを配信するためのBOTです。

## このBOTは、以下の機能を持っています。 
- 食堂メニューの配信
- 作者についての情報の配信

## このBOTは、以下のスラッシュコマンドを受け付けます。
- /今日のメニュー: 今日の食堂メニューを配信します。
- /author: 作者についての情報を配信します。

## このBOTは、以下の環境変数を利用します。
- SYOKUDOU_BOT_TOKEN: developer.discord.com で取得したBOTのトークン

## このBOTは、以下のライブラリを利用しています。

This project uses the following external libraries:

- [discord.py](https://discordpy.readthedocs.io/) - A Python wrapper for the Discord API.
- [pandas](https://pandas.pydata.org/) - Data analysis and manipulation library.
- [python-dotenv](https://github.com/theskumar/python-dotenv), licensed under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

Copyright (c) 2025 Saurabh Kumar

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions, and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Please refer to the LICENSE files of the respective libraries for detailed license terms.

## このBOTは、以下のライブラリをインストールすることで利用できます。
```bash
pip install discord.py pandas python-dotenv threading
```

## このBOTは、以下のAPIと連携しています。

This project interacts with the following APIs:

- [Discord API](https://discord.com/developers/docs/intro) - Used to connect the bot to Discord servers and perform various bot functions.

Please ensure that you comply with the [Discord API Terms of Service](https://discord.com/developers/docs/legal) when using this bot.

## このソフトウェアを利用する際は、以下の手順に従ってください。
1. このリポジトリをクローンします。
```bash
git clone https://github.com/KoueiKonoo/syokudou_bot.git
```
2. このリポジトリに移動します。
```bash
cd syokudou_bot
```
3. .envファイルを作成し、以下の内容を記述します。
```bash
SYOKUDOU_BOT_TOKEN=YOUR_BOT_TOKEN
```
4. このBOTを起動します。
```bash
chmod +x main.py
./main.py
```

## このBOTは、以下のリポジトリで公開されています。
github.com/KoueiKonoo/syokudou-bot

## このBOTは、以下のライセンスで公開されています。
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
