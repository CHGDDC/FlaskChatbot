from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot',methods=('POST','GET'))
def chatbot():
    req = request.get_json(force=True)
    if req['queryResult']['intent']['displayName'] == 'pizza-order':
        print(req)
        return jsonify(fulfillment_messages = [
            {
                "payload" : {
                    "richContent" : [
                        [
                            {
                                "type" : "image" ,
                                "rawUrl" : "https://www.yyg.go.kr/www/citizen_participation/publicity/ybmodule.file/board_www/www_company_pr/300x1/1642656888.jpeg"
                            },
                            {
                                "type": "info",
                                "title": "피자메뉴",
                                "subtitle": "피자메뉴판",
                                "actionLink": "https://www.yyg.go.kr/www/citizen_participation/publicity/ybmodule.file/board_www/www_company_pr/300x1/1642656888.jpeg"
                            }
                        ]
                    ]
                }
            }
        ])

    elif req['queryResult']['intent']['displayName'] == 'pizza-order - custom':
        print(req)
        return jsonify(fulfillment_messages=[
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "accordion",
                                "title": "포테이토 피자",
                                "subtitle": "#도미노피자 No.1 레전드",
                                "image": {
                                    "src": {
                                        "rawUrl": "https://cdn.dominos.co.kr/admin/upload/goods/20200311_M9Q50gtd.jpg"
                                    }
                                },
                                "text": "* 알레르기 유발 가능 물질 : 알류(가금류에 한한다), 우유, 메밀, 땅콩, 대두, 밀, 고등어, 게, 새우, 돼지고기, 복숭아, 토마토, 아황산류, 호두, 닭고기, 쇠고기, 오징어, 조개류(굴, 전복, 홍합 포함), 잣"
                            }
                        ]
                    ]
                }
            }
        ])

if __name__=='__main__':
    app.run('0.0.0.0', port=5001, debug=True)