import requests


def get(url, params=None):
    try:
        req = requests.get(url=url, params=params)
        exc = None
        msg = "OK"
    except requests.exceptions.HTTPError as http_exc:
        msg = "Http ERROR"
        exc = http_exc
    except requests.exceptions.ConnectionError as conn_exc:
        msg = "Connection ERROR"
        exc = conn_exc
    except requests.exceptions.Timeout as timeout_exc:
        msg = "Timeout ERROR"
        exc = timeout_exc
    except requests.exceptions.RequestException  as exc:
        msg = "Unknown request ERROR"
        exc = exc
    
    return {
        'status': req.status_code, 
        'request': req,
        'msg': msg,
        'exception': exc
    }