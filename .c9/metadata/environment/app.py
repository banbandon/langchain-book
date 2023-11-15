{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":69,"position":69,"stack":[[{"start":{"row":0,"column":0},"end":{"row":5,"column":47},"action":"insert","lines":["import os","from slack_bolt import App","from slack_bolt.adapter.socket_mode import SocketModeHandler","","SLACK_BOT_TOKEN = os.environ.get(\"SLACK_BOT_TOKEN\")","SLACK_APP_TOKEN = os.environ[\"SLACK_APP_TOKEN\"]"],"id":1}],[{"start":{"row":0,"column":9},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["d"],"id":3},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["o"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["e"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["t"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["t"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["n"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["v"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["v"],"id":4},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["n"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"remove","lines":["t"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"remove","lines":["t"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["e"]}],[{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["t"],"id":5},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["e"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["n"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["v"]}],[{"start":{"row":6,"column":47},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":15},"action":"insert","lines":["import * as dotenv from 'dotenv'","dotenv.config()"],"id":7}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":32},"action":"remove","lines":["import * as dotenv from 'dotenv'"],"id":8}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":32},"action":"insert","lines":["import * as dotenv from 'dotenv'"],"id":9}],[{"start":{"row":1,"column":33},"end":{"row":1,"column":38},"action":"remove","lines":["otenv"],"id":10},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"remove","lines":["d"]}],[{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":[" "],"id":11},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"remove","lines":["v"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":["n"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["e"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["t"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":["o"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":["d"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":[" "]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"remove","lines":["s"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"remove","lines":["a"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":[" "]}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["*"],"id":12},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":[" "]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["t"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"remove","lines":["r"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"remove","lines":["o"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["p"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":["m"]},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["i"]}],[{"start":{"row":1,"column":13},"end":{"row":1,"column":23},"action":"insert","lines":["import App"],"id":13}],[{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":["'"],"id":14}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["'"],"id":15}],[{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":[" "],"id":16}],[{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["p"],"id":17},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["p"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"remove","lines":["A"]}],[{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["l"],"id":18},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["o"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["a"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["d"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["?"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["d"]}],[{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["o"],"id":19},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["t"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["e"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["n"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["v"]}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"remove","lines":["?"],"id":20}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["_"],"id":21}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":25},"action":"insert","lines":["","load_dotenv(verbose=True)"],"id":23}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":["e"],"id":24},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["u"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["r"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["T"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["="]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":["e"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":["s"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"remove","lines":["o"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["b"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"remove","lines":["r"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["e"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["v"]}],[{"start":{"row":8,"column":0},"end":{"row":12,"column":15},"action":"remove","lines":["SLACK_BOT_TOKEN = os.environ.get(\"SLACK_BOT_TOKEN\")","SLACK_APP_TOKEN = os.environ[\"SLACK_APP_TOKEN\"]","","","dotenv.config()"],"id":25},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":26}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":7,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します","app = App(token=os.environ.get(\"SLACK_BOT_TOKEN\"))","","# アプリを起動します","if __name__ == \"__main__\":","    SocketModeHandler(app, os.environ[\"SLACK_APP_TOKEN\"]).start()",""],"id":28}],[{"start":{"row":12,"column":65},"end":{"row":13,"column":0},"action":"remove","lines":["",""],"id":29}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["#"],"id":30}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"remove","lines":["#"],"id":32}],[{"start":{"row":12,"column":65},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":33},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"insert","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":34},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"remove","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":36},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":4},"end":{"row":16,"column":0},"action":"insert","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "],"id":38}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["@"],"id":39},{"start":{"row":16,"column":1},"end":{"row":16,"column":2},"action":"insert","lines":["a"]},{"start":{"row":16,"column":2},"end":{"row":16,"column":3},"action":"insert","lines":["p"]},{"start":{"row":16,"column":3},"end":{"row":16,"column":4},"action":"insert","lines":["p"]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["."],"id":40},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":["e"]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["v"]},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["n"],"id":41},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":10},"end":{"row":16,"column":12},"action":"insert","lines":["()"],"id":42}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":13},"action":"insert","lines":["\"\""],"id":43}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["a"],"id":44},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["p"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["p"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["_"]},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":["m"]},{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"insert","lines":["e"]},{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"insert","lines":["n"]},{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"insert","lines":["i"],"id":45},{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"insert","lines":["o"]},{"start":{"row":16,"column":22},"end":{"row":16,"column":23},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["@"],"id":46}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["@"],"id":47}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["@"],"id":48}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["@"],"id":49},{"start":{"row":16,"column":1},"end":{"row":16,"column":2},"action":"insert","lines":["@"]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["@"],"id":50}],[{"start":{"row":15,"column":4},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "],"id":52},{"start":{"row":15,"column":4},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":25},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":53},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["d"]},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"remove","lines":["de"],"id":54},{"start":{"row":17,"column":0},"end":{"row":17,"column":3},"action":"insert","lines":["def"]}],[{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":[" "],"id":55}],[{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"remove","lines":[" "],"id":56},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":17,"column":4},"end":{"row":19,"column":32},"action":"insert","lines":["def say_hello(message, say):","    user = message['user']","    say(f\"Hi there, <@{user}>!\")"],"id":57}],[{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"remove","lines":[" "],"id":58},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["f"]},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"remove","lines":["e"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"remove","lines":["d"]}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["p"],"id":59},{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["y"]},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["h"]}],[{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"remove","lines":["h"],"id":60}],[{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["t"],"id":61},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["h"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["o"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["n"]}],[{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":[" "],"id":62}],[{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"remove","lines":[" "],"id":63},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"remove","lines":["n"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"remove","lines":["o"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"remove","lines":["h"]},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"remove","lines":["t"]},{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"remove","lines":["y"]},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"remove","lines":["p"]}],[{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"remove","lines":["e"],"id":64},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"remove","lines":["g"]},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"remove","lines":["a"]},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"remove","lines":["s"]},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"remove","lines":["s"]},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"remove","lines":["e"]},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"remove","lines":["m"]}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["e"],"id":65},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["v"]},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["e"]},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["n"]},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"remove","lines":["e"],"id":66},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"remove","lines":["g"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"remove","lines":["a"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"remove","lines":["s"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"remove","lines":["s"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"remove","lines":["e"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"remove","lines":["m"]}],[{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["e"],"id":67},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["v"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["e"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["n"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":32},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":68},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":21,"column":0},"action":"insert","lines":["",""]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "],"id":69}],[{"start":{"row":21,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["@app.event(\"message\")","def handle_message_events(body, logger):","    logger.info(body)",""],"id":70}],[{"start":{"row":21,"column":1},"end":{"row":23,"column":21},"action":"remove","lines":["app.event(\"message\")","def handle_message_events(body, logger):","    logger.info(body)"],"id":71},{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"remove","lines":["@"]},{"start":{"row":20,"column":4},"end":{"row":21,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":4},"end":{"row":20,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1700063306671,"hash":"1e09624f766d46c7726d01092bf39de9d51ff02c"}