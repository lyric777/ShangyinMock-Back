from flask import Flask, jsonify
from flask_cors import CORS
import time

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

app.url_map.strict_slashes = False

'''
create schema shangyinmock default character set utf8 collate utf8_general_ci;
create user 'dev_user'@'%' identified by 'shangyinmock';
grant select,insert,update,delete,create on shangyinmock.* to root;
grant select,insert,update,delete,create on shangyinmock.* to dev_user;
flush privileges;
'''

flag = 0


@app.route('/use_api/<api>')
def use_api(api):
    '''
    dkjiejuh = ['207210410003154', 'AP7CD4EDozF5ISnutPVeal65PgPfm0', '578169136352940173174852605741', 'IkhfawWybQTRfusJmZlsBXPkQutDab', '']
    hetongbh = ['22476386404305218315240479965629', 'jht5GPtPKD7ijvi0HHEahhzeTRpV3lCv', 'abrnwqCzMmjFIpfvehnvJsoYLtqkaZtH', 'L1572071780202008190947169887', '', None]
    huobdhao = ['156', '300', '0', '', None]
    huankjee =  [-100, 0.0, 3455, 9999999999, None]
    huankzhh = ['03003867117', '70435825006818224895468822378471', 'XZhbypZhbLDc5pS1l2sNpMezWQNsfnqd', '', None]
    huakzhgs = ['', None, '1', '2', '0', '11']
    tqhkhxfs = ['', None, '0', '1', '2', '3', '4', '21']
    huakzhlx = ['', None, 'C', 'A', 'I', 'P', 'E', 'q', 'at']
    hukzhmch = ['', None, '2JTZN29ywJ9lccWrFthxwc1M0GYmIk2C76P9u6fE', '上海汽车集团财务有限责任公司']
    hukzhkhh = ['nvTRKItaClUPgbFQtsksovKduBTmuZdB', '', None, '上海银行天山支行']
    hkbeizhu = ['HG58saCK6iLNDZSCaklTSMpePEUCfr', '', None]
    result = []
    for i in dkjiejuh:
        for j in hetongbh:
            for k in huobdhao:
                for m in huankjee:
                    for n in huankzhh:
                        for n1 in huakzhgs:
                            for n2 in tqhkhxfs:
                                for n3 in huakzhlx:
                                    for n4 in hukzhmch:
                                        for n5 in hukzhkhh:
                                            for n6 in hkbeizhu:
                                                result.append({'dkjiejuh': i, 'hetongbh': j, 'huobdhao': k, 'huankjee': m, 'huankzhh': n, 'huakzhgs': n1, 'tqhkhxfs': n2, 'huakzhlx': n3, 'hukzhmch': n4, 'hukzhkhh': n5, 'hkbeizhu':n6})
    '''
    comname = ['sjfhu', '', 'sdfghjkiuytvb']
    rolldate = ['', '20200913', '20190901', '20290913']
    type = ['001', '002', '010', '0', '']
    comID = ['123454566543', '0', '123', '', '0987654334567890654456789']
    num = [None, 0, 9999.00, -1, 123, 99999999999.00]
    result = []
    for i in comname:
        for j in rolldate:
            for k in type:
                for m in comID:
                    for n in num:
                        result.append({'comname': i, 'rolldata': j, 'type': k, 'comID': m, 'num': n})
    return jsonify(result)


@app.route('/login', methods=['post'])
def login():
    '''
    if request.method == 'POST':
        host = '127.0.0.1'
        client = MongoClient(host, 27017)
        db = client.recruit
        user = db.user
        email = request.get_json()['email']
        password = request.get_json()['password']
        doc = user.find_one({'email': email})
        if doc is not None:
            if doc['password'] == password:
                return jsonify({'status': True})  # 登录成功
        else:
            return jsonify({'status': False})
    '''

    '''
    data = [{'comname':  ['sjfhu', '', 'sdfghjkiuytvb']},
            {'rolldate': ['', '20200913', '20190901', '20290913']},
            {'type': ['001', '002', '010', '0', '']},
            {'comID': ['123454566543', '0', '123', '', '0987654334567890654456789']},
            {'num': [None, 0, 9999.00, -1, 123, 99999999999.00]}]
    result = []
    for i in len(data):
        for k, v in data[i].items():
            for it in v:
    '''
    comname = ['sjfhu', '', 'sdfghjkiuytvb']
    rolldate = ['', '20200913', '20190901', '20290913']
    type = ['001', '002', '010', '0', '']
    comID = ['123454566543', '0', '123', '', '0987654334567890654456789']
    num = [None, 0, 9999.00, -1, 123, 99999999999.00]
    result = []
    for i in comname:
        for j in rolldate:
            for k in type:
                for m in comID:
                    for n in num:
                        result.append({'comname': i, 'rolldata': j, 'type': k, 'comID': m, 'num': n})
    return jsonify(result)


@app.route('/upload', methods=['get', 'post'])
def upload():
    flag = 1
    print(flag)
    return jsonify({
        "status": "done"
    })


@app.route('/get_api_all')
def get_api_all():
    flag = 1
    if flag == 1:
        upload_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data = {"results": [
            {'key': '1', 'api_name': '3026', 'api_name_cn': '多借据放款', 'api_sys': '新个贷', 'upload_time': upload_time,
             'fields': 'dkjiejuh hzfhthao hezuofbh htshexrq htshixrq hetongbh chanpdma kehmingc zhengjlx zhengjhm shoujihm youjidiz youbiann shoujrxm dianziyx qixiriqi dkqixian daoqriqi yngyjigo zhngjigo hetongje jiejuuje bencfkje'},
            {'key': '2', 'api_name': '7334', 'api_name_cn': '407科目余额查询', 'api_sys': '新个贷', 'upload_time': upload_time,
             'fields': 'jiaoyirq jigouhao chanphao kemuhaoo qishibis chxunbis'},
            {'key': '3', 'api_name': '3266', 'api_name_cn': '贷款提前还款', 'api_sys': '新个贷', 'upload_time': upload_time,
             'fields': 'dkjiejuh hetongbh huobdhao huankjee huankzhh huakzhgs tqhkhxfs huakzhlx hukzhmch hukzhkhh hkbeizhu'}]}

        return jsonify(data)
    else:
        return {}


@app.route('/get_api')
def get_api():
    data = {"results": [
        {"key": "1", "field": "dkjiejuh", "alias_field": "LoanDblNo", "field_cn": "贷款借据号", "type": "string", "length": "30",
         "options": "", "required": "是", "default": "''", "fixed_value": "", "description": "借据号必须输入，检查借据是否存在"},
        {"key": "2", "field": "hetongbh", "alias_field": "CtrNo", "field_cn": "合同编号", "type": "string", "length": "32",
         "options": "",
         "required": "否", "default": "''", "fixed_value": "", "description": "非必输，可由前端根据借据号查询回显用。"},
        {"key": "3", "field": "huobdhao", "alias_field": "Ccy", "field_cn": "货币代号", "type": "string", "length": "3",
         "options": "156--人民币", "required": "是", "default": "", "fixed_value": "", "description": ""},
        {"key": "4", "field": "huankjee", "alias_field": "RepymtAmt", "field_cn": "还款金额", "type": "decimal", "length": "(20,2)",
         "options": "", "required": "是", "default": 0.0, "fixed_value": "", "description": "必须大于0"},
        {"key": "5", "field": "huankzhh", "alias_field": "RepymtAcctNo", "field_cn": "还款账号", "type": "string", "length": "32",
         "options": "", "required": "是", "default": "''", "fixed_value": "", "description": "一般传入借据对应的默认还款账号"},
        {"key": "6", "field": "huakzhgs", "alias_field": "RepymtAcctAtchTp", "field_cn": "还款账户归属", "type": "string", "length": "1",
         "options": "1--T24\n2--互联网核心", "required": "是", "default": "", "fixed_value": "", "description": ""},
        {"key": "7", "field": "tqhkhxfs", "alias_field": "ElyRepymtRepyIntMd", "field_cn": "提前还款还息方式", "type": "string",
         "length": "1",
         "options": "0-不还息\n1-部分还息\n2-全部还息\n3-优先还本", "required": "是", "default": "", "fixed_value": "",
         "description": "根据不同产品需求上送对应还息方式"},
        {"key": "8", "field": "huakzhlx", "alias_field": "RepymtAcctTp", "field_cn": "还款账户type", "type": "string", "length": "1",
         "options": "C--个人银行卡\nA--对公账户\nI--内部账户\nP--个人存折\nE--互联网核心E账户", "required": "否", "default": "",
         "fixed_value": "",
         "description": ""},
        {"key": "9", "field": "hukzhmch", "alias_field": "RepymtAcctNm", "field_cn": "还款账户名称", "type": "string", "length": "384",
         "options": "", "required": "否", "default": "", "fixed_value": "", "description": ""},
        {"key": "10", "field": "hukzhkhh", "alias_field": "RepymtAcctOpnBnkNo", "field_cn": "还款账户开户行", "type": "string",
         "length": "32",
         "options": "", "required": "否", "default": "", "fixed_value": "", "description": ""},
        {"key": "11", "field": "hkbeizhu", "alias_field": "TxnRmk", "field_cn": "还款备注", "type": "string", "length": "1500",
         "options": "", "required": "否", "default": "", "fixed_value": "", "description": "备注将会体现在后续的明细查询中。"}
    ], "trade_name_cn": "贷款提前还款", "trade_id": "3266", "business_category": "1"}
    return jsonify(data)


@app.route('/get_api_result_all')
def get_api_result_all():
    data = {"results": [
        {'key': '1', 'api_name': '3026', 'api_name_cn': '多借据放款', 'api_sys': '新个贷',
         'fields': 'dkjiejuh hzfhthao hezuofbh htshexrq htshixrq hetongbh chanpdma kehmingc zhengjlx zhengjhm shoujihm youjidiz youbiann shoujrxm dianziyx qixiriqi dkqixian daoqriqi yngyjigo zhngjigo hetongje jiejuuje bencfkje'},
        {'key': '2', 'api_name': '7334', 'api_name_cn': '407科目余额查询', 'api_sys': '新个贷',
         'fields': 'jiaoyirq jigouhao chanphao kemuhaoo qishibis chxunbis'},
        {'key': '3', 'api_name': '3266', 'api_name_cn': '贷款提前还款', 'api_sys': '新个贷',
         'fields': 'dkjiejuh hetongbh huobdhao huankjee huankzhh huakzhgs tqhkhxfs huakzhlx hukzhmch hukzhkhh hkbeizhu'}]}
    return jsonify(data)


@app.route('/get_api_result')
def get_api_result():
    data = {"results": [
        {"key": "1", "field": "dkjiejuh", "field_cn": "贷款借据号", "type": "string",
         "length": "30",
         "options": "", "required": "是", "default": "''", "fixed_value": "", "enumeration": "['207210410003154', 'AP7CD4EDozF5ISnutPVeal65PgPfm0', '578169136352940173174852605741', 'IkhfawWybQTRfusJmZlsBXPkQutDab', '']"},
        {"key": "2", "field": "hetongbh", "field_cn": "合同编号", "type": "string", "length": "32",
         "options": "",
         "required": "否", "default": "''", "fixed_value": "", "enumeration": "['22476386404305218315240479965629', 'jht5GPtPKD7ijvi0HHEahhzeTRpV3lCv', 'abrnwqCzMmjFIpfvehnvJsoYLtqkaZtH', 'L1572071780202008190947169887', '', null]"},
        {"key": "3", "field": "huobdhao", "field_cn": "货币代号", "type": "string", "length": "3",
         "options": "156--人民币", "required": "是", "default": "", "fixed_value": "", "enumeration": "['156', '300', '0','', null]"},
        {"key": "4", "field": "huankjee", "field_cn": "还款金额", "type": "decimal",
         "length": "(20,2)",
         "options": "", "required": "是", "default": 0.0, "fixed_value": "", "enumeration": "[-100, 0.0, 3455, 9999999999, null]"},
        {"key": "5", "field": "huankzhh", "field_cn": "还款账号", "type": "string",
         "length": "32",
         "options": "", "required": "是", "default": "''", "fixed_value": "", "enumeration": "['03003867117', '70435825006818224895468822378471', 'XZhbypZhbLDc5pS1l2sNpMezWQNsfnqd', '', null]"},
        {"key": "6", "field": "huakzhgs", "field_cn": "还款账户归属", "type": "string",
         "length": "1",
         "options": "1--T24\n2--互联网核心", "required": "是", "default": "", "fixed_value": "", "enumeration": "['', null, '1', '2', '0', '11']"},
        {"key": "7", "field": "tqhkhxfs", "field_cn": "提前还款还息方式", "type": "string",
         "length": "1",
         "options": "0-不还息\n1-部分还息\n2-全部还息\n3-优先还本", "required": "是", "default": "", "fixed_value": "",
         "enumeration": "['', null, '0', '1', '2', '3', '4', '21']"},
        {"key": "8", "field": "huakzhlx", "field_cn": "还款账户type", "type": "string",
         "length": "1",
         "options": "C--个人银行卡\nA--对公账户\nI--内部账户\nP--个人存折\nE--互联网核心E账户", "required": "否", "default": "",
         "fixed_value": "",
         "enumeration": "['', null, 'C', 'A', 'I', 'P', 'E', 'q', 'at']"},
        {"key": "9", "field": "hukzhmch", "field_cn": "还款账户名称", "type": "string",
         "length": "384",
         "options": "", "required": "否", "default": "", "fixed_value": "", "enumeration": "['', null, '2JTZN29ywJ9lccWrFthxwc1M0GYmIk2C76P9u6fE', '上海汽车集团财务有限责任公司']"},
        {"key": "10", "field": "hukzhkhh", "field_cn": "还款账户开户行", "type": "string",
         "length": "32",
         "options": "", "required": "否", "default": "", "fixed_value": "", "enumeration": "['nvTRKItaClUPgbFQtsksovKduBTmuZdB', '', null, '上海银行天山支行']"},
        {"key": "11", "field": "hkbeizhu", "field_cn": "还款备注", "type": "string",
         "length": "1500",
         "options": "", "required": "否", "default": "", "fixed_value": "", "enumeration": "['HG58saCK6iLNDZSCaklTSMpePEUCfr', '', null]"}
    ], "trade_name_cn": "贷款提前还款", "trade_id": "3266", "business_category": "1"}
    return jsonify(data)


'''
# 上传excel，新增记录
def post(self):
    try:
        # 上传excel文件
        f = request.files.get('file')
        if f:
            # 重命名文件名称，使用secure_filename去除中文名，否则截取的file_type错误
            file_type = secure_filename(f.filename).split('.')[-1]
            now = datetime.now().strftime('%Y%m%d%H%M%S')  # 重命名为时间戳文件名
            file_name = now+'.' + file_type
            file_allow = current_app.config['ALLOWED_EXTENSIONS']
            if file_type in file_allow:  # 验证文件后缀
                # file_path = current_app.config['UPLOAD_PATH'] +file_name # linux
                file_path = os.path.abspath(
                    '.') + "\\app\\static\\upload\\" + file_name  # windows
                print(file_path)
                f.save(file_path)
                df = pd.read_excel(file_path, encoding="UTF-8")
                print(df)
                # 连接mysql
                conn = current_app.config['SQLALCHEMY_DATABASE_URI']
                engine = create_engine(conn)
                # dataframe写入mysql
                df.to_sql(name='complain', con=engine,
                          if_exists='append', index=False)
            else:
                return jsonify({"file": "上传文件格式不支持，仅支持xlsx或xls"})

        # img.img_url = file_name
        # db.session.add(img)
        # db.session.flush() #在commit提交之前db.session.flush(),获得新增的ID
        # img_id = img.img_id
        # db.session.commit()
        # #返回新增的数据
        # res = Image.query.get_or_404(img_id)
        # data = queryToDict(res)# 转换为dic
        return jsonify({"data": "upload success!", "code": 20000})
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"data": "upload fail!", "code": 500})
    finally:
        db.session.close()
'''

if __name__ == '__main__':
    app.run()
