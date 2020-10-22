import requests
import uuid
def test_get():
    s = requests.Session()

def add_fault(fault):
    s = requests.Session()
    base = 'http://127.0.0.1:8080/'
    resource = 'faults'
    fault_id = str(uuid.uuid4())
    try:
        response = s.post(f'{base}{resource}/{fault_id}', json=fault)
        if response.status_code != 200:
            raise ValueError(f"Failed to send fault ={fault}. Returned {response.json()}")
        return response.json()
    except Exception as e:
        print(f"Exception {e}")


def remove_fault(fault_id):
    s = requests.Session()
    base = 'http://127.0.0.1:8080/'
    resource = 'faults'
    try:
        response = s.delete(f'{base}{resource}/{fault_id}')
        if response.status_code != 200:
            raise ValueError(f"Failed to delete fault ={fault_id}. Returned {response.json()}")
        return response.json()
    except Exception as e:
        print(f"Exception {e}")



def test_put():
    s = requests.Session()
    r = s.put('http://127.0.0.1:8080/', params={'another_string': 'try'})
    print(r)
    print(r)
    r = s.get('http://127.0.0.1:8080/')
    print(r)
    r = s.put('http://127.0.0.1:8080/', params={'another_string': 'try'})
    print(r)
    print(r)
    r = s.get('http://127.0.0.1:8080/')
    print(r)

    print(r)
    print(r)


if __name__ == '__main__':
    response = add_fault({'name':'post fault method'})
    print(f'response={response}')
    response = remove_fault('NOT_FOUND')
    print(f'remove "not found" response={response}')

    #test_put()
    # test_get()


