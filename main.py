import datetime

from flask import Flask, Response, request, render_template
from pybadges import badge
from hashlib import md5
import requests
from os import environ
from dotenv import find_dotenv,load_dotenv

from logos import list_logos, resolve_logo

load_dotenv(find_dotenv())

app = Flask(__name__)


def invalid_count_resp(err_msg) -> Response:
    """
    Return a svg badge with error info when cannot process repo_id param from request
    :return: A response with invalid request badge
    """
    svg = badge(left_text="Error", right_text=err_msg,
                whole_link="https://visitor-badge.laobi.icu")
    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0', 'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(response=svg, content_type="image/svg+xml", headers=headers)


def update_counter(key, action):
    url = 'http://127.0.0.1:8080/count?keyword={0}&action={1}'.format(key,action)
    try:
        resp = requests.get(url)
        if resp and resp.status_code == 200:
            return resp.json()['value']
        else:
            return None
    except Exception as e:
        return None

def format_count(count):
    count = float('{:.3g}'.format(count))
    magnitude = 0
    while abs(count) >= 1000:
        magnitude += 1
        count /= 1000.0
    return '{}{}'.format('{:f}'.format(count).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

@app.route("/badge")
def visitor_svg() -> Response:
    """
    Return a svg badge with latest visitor count of 'Referer' header value

    :return: A svg badge with latest visitor count
    """

    req_source = identity_request_source()

    if not req_source:
        return invalid_count_resp('Missing required param: page_id')

    action = "update"
    if request.args.get("query_only") is not None:
        action = "query"

    # get count
    latest_count = update_counter(req_source, action)

    if not latest_count:
        return invalid_count_resp("Count API Failed")

    # get left color and right color
    left_color = "#595959" 
    if request.args.get("left_color") is not None:
      left_color = request.args.get("left_color")
    
    right_color = "#1283c3"
    if request.args.get("right_color") is not None:
      right_color = request.args.get("right_color")

    left_text = request.args.get("left_text")

    if left_text is None or len(left_text) == 0:
        left_text = request.args.get('title')

    if left_text is None or len(left_text) == 0:
    	left_text = 'visitors'

    if request.args.get("format") is not None:
        latest_count = format_count(latest_count)

    home = "https://visitor-badge.laobi.icu"
    logo = resolve_logo(request.args.get('logo'))

    svg = badge(left_text=left_text, right_text=str(latest_count), left_color=str(left_color), right_color=str(right_color), right_link=home, left_link=home, logo=logo)
    # 修复 QQ Bot 不识别 xlink:href 的问题
    svg = svg.replace('xlink:href=', 'href=')

    # 自定义尺寸 & 圆角
    new_radius = request.args.get('radius')
    new_height = request.args.get('height')
    if new_radius:
        svg = svg.replace('rx="3"', f'rx="{new_radius}"')
    if new_height:
        h = int(new_height)
        ratio = h / 20.0
        import re

        def scale_attrs(m):
            tag = m.group(0)
            def repl_num(k):
                m2 = re.search(r'(?<=\s)' + k + r'="([\d.]+)"', tag)
                if m2:
                    old = tag[m2.start():m2.end()]
                    new = f'{k}="{float(m2.group(1))*ratio:.1f}"'
                    return tag[:m2.start()] + new + tag[m2.end():], True
                return tag, False
            # 缩放 SVG、rect、linearGradient 等所有标签的数字属性
            for k in ('width', 'height', 'x', 'y', 'rx'):
                tag, _ = repl_num(k)
            return tag

        # 等比例缩放所有标签的数字属性
        svg = re.sub(r'<[a-z]+[^>]*>', lambda m: scale_attrs(m), svg)
        # font-size 和 textLength
        svg = re.sub(r'(font-size=")(\d+)(")',
            lambda m: f'{m.group(1)}{float(m.group(2))*ratio:.0f}{m.group(3)}', svg)
        svg = re.sub(r'(textLength=")([\d.]+)(")',
            lambda m: f'{m.group(1)}{float(m.group(2))*ratio:.1f}{m.group(3)}', svg)

    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0,no-store,s-maxage=0,proxy-revalidate',
               'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(response=svg, content_type="image/svg+xml", headers=headers)


@app.route("/health")
def health():
    try:
        resp = requests.get('http://127.0.0.1:8080/count?keyword=health&action=query', timeout=5)
        if resp.status_code == 200:
            return {'status': 'ok', 'count': resp.json().get('value', 0)}
        return {'status': 'error'}, 502
    except Exception as e:
        return {'status': 'error', 'detail': str(e)}, 502


@app.route("/stats")
def stats():
    try:
        resp = requests.get('http://127.0.0.1:8080/stats', timeout=5)
        if resp.status_code == 200:
            return {'total_keys': resp.json().get('total_keys', 0)}
        return {'status': 'error'}, 502
    except Exception as e:
        return {'status': 'error', 'detail': str(e)}, 502


@app.route("/index.html")
@app.route("/index")
@app.route("/")
def index() -> Response:
    return render_template('index.html', logos=list_logos())


def identity_request_source() -> str:
    page_id = request.args.get('page_id')
    if page_id is not None and len(page_id):
        m = md5(page_id.encode('utf-8'))
        m.update(environ.get('md5_key').encode('utf-8'))
        return m.hexdigest()
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=55000)
