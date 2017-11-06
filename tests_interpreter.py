import unittest

from main import *


class Test(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter("testdb")
        data = [('e01', 'm', 20, 20, 'Normal', 100, '12-06-17'),
                ('e02', 'f', 21, 21, 'Underweight', 125, '12-07-17'),
                ('e03', 'm', 21, 21, 'Overweight', 119, '12-07-17'),
                ('e04', 'f', 22, 22, 'Normal', 114, '12-08-17'),
                ('e05', 'm', 21, 21, 'Underweight', 119, '12-07-17'),
                ('e06', 'f', 22, 22, 'Obesity', 113, '12-08-17'),
                ('e07', 'm', 21, 21, 'Overweight', 126, '12-07-17'),
                ('e08', 'f', 22, 22, 'Obesity', 130, '12-08-17'),
                ('e10', 'f', 21, 21, 'Overweight', 140, '12-07-17'),
                ('e11', 'm', 22, 22, 'Normal', 149, '12-08-17'),
                ('e12', 'f', 21, 21, 'Underweight', 144, '12-07-17'),
                ('e13', 'm', 22, 22, 'Obesity', 147, '12-08-17'),
                ('e14', 'f', 21, 21, 'Overweight', 167, '12-07-17'),
                ('e15', 'm', 22, 22, 'Obesity', 159, '12-08-17'),
                ('e16', 'f', 22, 22, 'Normal', 195, '12-08-17')]

        self.interpreter.database.write_to_database(data)

    def test_display_data(self):
        try:
            self.interpreter.do_display_data("testdata.txt")
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_backup_database_option(self):
            self.interpreter.do_backup_database("-o save_to_db")
            self.assertTrue(True)

    def test_backup_database_no_option(self):
            self.interpreter.do_backup_database("save_to_db3")
            self.assertTrue(True)

    def test_backup_database_get_data(self):
            data = self.interpreter.do_get_data("""select * from employee""")
            self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()