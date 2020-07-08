import pytest
import time

def random_create_data():

 return {
  "dayOfBirth": "1938-07-07",
  "email": str(time.time()) + '@fakemail.com',
  "firstName": "string",
  "lastName": "string"
}

class TestSmoke:
 @pytest.mark.parametrize("id_test", [str(i) for i in range(1,21)])
 def test_check_count_users(self, client,id_test):
    res = client.get_user(id_test)
    assert res.json()["id"] == int(id_test)
    assert res.status_code == 200

 def test_check_create_user(self, client):
     data = random_create_data()
     res = client.vr(client.create_user(data), [200, 201])
     assert res.json()["id"] > 21


 def test_check_update_user(self,client):
     create_user = client.vr(client.create_user(random_create_data()), [200, 201])
     id_user = create_user.json()["id"]

     data = {
          "firstName": "Pasha",
          "lastName": "Ivanov"
      }
     res = client.vr(client.update_user(id_user, data))
     updated = res.json()
     assert updated["firstName"] == "Pasha"
     assert updated ["lastName"] == "Ivanov"

 def test_check_delete_user(self,client):

     create_user = client.vr(client.create_user(random_create_data()), [200, 201])
     id_user = create_user.json()["id"]
     client.delete_user(id_user)
     assert client.get_user(id_user).status_code == 404

