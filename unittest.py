# -*- coding: utf-8 -*-

import unittest


def struct_is_info( struct ):
    test_1 = True
    for key in struct.keys():
        test_1 = test_1 and key == 'num_mesa'
    
    return test_1

def struct_is_tree( struct ):
    test_1 = True
    for key in struct.keys():
        test_1 = test_1 and key in ['name', 'type', 'child']

    test_2 = True
    for val in struct.values():
        test_2 = test_2 and (struct_is_tree(val) or struct_is_info(val) )

    return test_1 and test_2


class ONPEcrawlerTest(unittest.TestCase):
    def proper_hierarchy(self):
        """
        asda
        """
        #Check if struct is tree
        self.assertTrue( struct_is_tree(self.tree) )
        for key in struct.keys():
            self.assertIn( key, ['name', 'type', 'child'])

    def leaves_are_struct_info(self):
        pass

    def type_correspondance(self):
        pass


if __name__ == '__main__':
    unittest.main()
