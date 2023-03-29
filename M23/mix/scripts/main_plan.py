# For each new request for set of mpns, set a request_id in the database
# upload mpns in a temporary list and send API request to nexar for each mpn
    # request_id = str(uuid.uuid4()) Gerate request id and set it in the database
    # upload MPN via CSV right now and store in a temporary list
    # send API request to nexar for each mpn
        #1. Get token from nexar
        #2. build API post request using token , requet URL, JSON body
        #3. send API request to nexar for each mpn
        #4. Each received response validate it and print message
        #5. if response is not valid, print error message
        #6. if response is not valid, send another API request to nexar for next mpn
        #6. if response is valid, print message
        #7. if response is valid, and call Serializer to parse and store in the database
        #8. if response takes too long, stop request and learn to retry


import pandas
import threading
import scripts.oAPICall as oAPICall
from django.http import JsonResponse
from threading import Thread

from mixapp.serializers import PartSerializer
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oMain.settings')

def fetchMfnList():
    data = pandas.read_csv('scripts/mfn.csv')
    return data

# def saveToDB:
#     with open('scripts/data1.json') as file:
#         data = json.load(file)
#     json_data = data
#     print("JSON_DATA<>>>>>>>>>>>")
#     # print(json_data)
#     print("JSON_DATA<>>>>>>>>>>>")
#     serializer = UserSerializer(data=json_data)
#     # serializer = ManufacturerSerializer(data=json_data)
#     print(repr(serializer))
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#     else:
#         for error in serializer.errors:
#             print(error)




def fetch_process():
    print("fetch_process called")
    try:
        # req_id = kwargs.get('req_id', {})
        # mpns = kwargs.get('mpn', {})
        df = fetchMfnList()
        print(type(df))

        for ind in df.index:
            # t = Thread(target=oAPICall.callNexar, args=(mpn,))
            # print("starting thread")
            # t.start()
            # # --------------- manufacturer info parsing to db --------------
            # print(t)
            print(df['MFN'][ind])
            mfn = df['MFN'][ind]


            response = oAPICall.callNexar(mfn)

            print("nexar called")

            data= response['results'][0]
            json_data = data
            serializer = PartSerializer(data=json_data['part'])
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else:
                for error in serializer.errors:
                    print("Serializer Errors")
                    print(error)

            # else get data from response and call saveToDB

    except Exception as e:
        print("fetch_process exception called: ", e)



def startFetch():
    thread = threading.Thread(target=fetch_process)
    thread.start()
    return True



def run():
    startFetch()
    print("Running main function")





