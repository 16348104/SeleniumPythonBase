#coding=utf-8
import json
class HandleJson:
    def load_json(self):
        with open('E:\\Teacher\\Imooc\\SeleniumPythonBase\\ThreeNode\\config\\cookie.json') as fp:
            data = json.load(fp)
        return data
    
    def get_data(self):
        return self.load_json()
    
    def write_data(self,data):
        with open('E:\\Teacher\\Imooc\\SeleniumPythonBase\\ThreeNode\\config\\cookie.json','w') as fp:
            fp.write(json.dumps(data))
'''  
if __name__ == '__main__':
    hand = HandleJson()
    print(hand.get_data())
'''
handle_json = HandleJson()