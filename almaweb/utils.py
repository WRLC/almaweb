import json
import requests
import xml.dom.minidom as md

# utility functions, reused in various controllers
def alma_get(resource, apikey, params=None, fmt='json'):
    '''
    makes a generic get request to alma api.
    '''
    params = params or {}
    params['apikey'] = apikey
    params['format'] = fmt
    r = requests.get(resource, params=params)
    r.raise_for_status()
    return r

def alma_post(resource, apikey, payload=None, params=None, fmt='json'):
    '''
    makes a generic post request to alma api.
    '''
    payload = payload or {}
    params = params or {}
    params['format'] = fmt
    headers =  {'Authorization' : 'apikey ' + apikey}
    r = requests.post(resource,
                     headers=headers,
                     params=params,
                     data=payload)
    r.raise_for_status()
    return r

def pprint_xml(xml_str):
    try:
        parsed_xml = md.parseString(xml_str)
        return parsed_xml.toprettyxml() 
    except Exception as e:
        return e