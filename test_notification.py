import v3_notification
import unittest
import sys

class test_notification(unittest.TestCase):

    def test_query(self):
        v3_notification.define_params()
        result = v3_notification.query_gen()
        self.assertEqual('http://www.smsgate.cn/gb.asp?usr=rpci&pwd=rpscm&tel=18615761805&msg=job1_failed@1', result)
        
        
if __name__ == '__main__': 
    unittest.main() 