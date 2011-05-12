# -*- coding:  utf-8 -*-

import time
import unittest
import os.path

from daemon import Daemon


class TestDaemon(Daemon):
    def run(self):
        while True:
            print('bbbbbb')
            time.sleep(1)

class DaemonTestCase(unittest.TestCase):
    def setUp(self):
        self.pidfile = '/tmp/daemon-teste.pid'
        

    def teadDown(self):
        daemon = TestDaemon(self.pidfile)
        daemon.stop()
        pass

    def test_create(self):
        daemon1 = TestDaemon(self.pidfile)
        try:
            pf = file(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
        if not pid:
            daemon1.start()
        else:
            daemon1.stop()
        


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DaemonTestCase))
    return suite
    

if __name__ == '__main__':
    unittest.main(defaultTest = "suite")
