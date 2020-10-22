import requests

def test_get():
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/')
    print(r)
    print(r)

    def send_fault(self, fault):
        base = "'http://127.0.0.1:8080/'"
        resource = 'faults'
        try:
            response = self.session.post(f'{base}/{resource}?script=json', json={"cmd": fault})
            if response.status_code != 200:
                raise ValueError(f"Failed to send fault cmd={fault}. Returned {response.json()}")
            return response.json()
        except Exception as e:
            print(f"Exception thrown in  {e}")



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
    test_put()
    # test_get()


