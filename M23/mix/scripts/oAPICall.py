import scripts.auth as auth
import scripts.oConfig as octConf
import json
import requests

token = auth.get_token()


def callNexar(mpn):
    global token
    try:
        print("trying request building")
        print(octConf.NEXAR_URL)
        print(mpn)
        r = requests.post(octConf.NEXAR_URL,
                          json={"query": octConf.QUERY_MPN, "variables": {"mpn": mpn}},
                          headers={"token": token},
                          )

        data = json.loads(r.text)["data"]["supSearchMpn"]
    except Exception:
        raise Exception("Error while getting Nexar response")
    return data

#
# def get_part_info_from_mpn_2(mpn,m_oct_id):
#     global token
#     r = None
#     final_query_mpn = octConf.QUERY_MPN_2.replace("$mpn_oct_id",f"""["{m_oct_id}"]""")
#     try:
#         r = requests.post(octConf.NEXAR_URL,
#                           json={"query": final_query_mpn, "variables": {"mpn": mpn}},
#                           headers={"token": token},timeout=10
#                           )
#
#         data = json.loads(r.text)
#         dataError = data.get("errors")
#         if data.get("errors") is not None:
#             print("Api Error for mpn",mpn)
#             print(dataError)
#             return None
#         data = data.get("data",{}).get("supSearchMpn")
#         if data is None:
#             print("No Data from api for mpn",mpn)
#             return None
#         if data['hits'] == 0:
#             return None
#         else:
#             if data['hits'] > 1:
#
#                 print("hits more than one for ",mpn," with mpnoct ",m_oct_id)
#     except Exception:
#         if r is not None and "text" in r:
#             print("octopart api issue:",json.dumps(json.loads(r.text),indent = 1))
#         else:
#             print("octopart api issue")
#         # raise Exception("Error while getting Nexar response")
#         return None
#     return data





