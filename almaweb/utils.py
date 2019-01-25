# utility functions, reused in various controllers
def alma_get(resource, apikey, params=None, fmt='json'):
    '''
    makes a generic alma api call, pass in a resource
    '''
    params = params or {}
    params['apikey'] = apikey
    params['format'] = fmt
    r = requests.get(resource, params=params)
    r.raise_for_status()
    return r

def alma_post(resource, apikey, payload=None, params=None, fmt='json'):
    '''
    makes a generic put request to alma api. puts xml data.
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

def get_message():
   return "this is the message"
