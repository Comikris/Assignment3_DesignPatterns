from FileManagement.interface_filehandler import *
# Brendan
import pickle
import os
import sys
import data_validator


class FileFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_file_operator(self):
        pass


class FactoryWriter(FileFactory):
    def make_file_operator(self):
        return FileWriter()


class FactorySaver(FileFactory):
    def make_file_operator(self):
        return FileSaver()


class FileProduct(object):
    def status(self, msg):
        pass

    def load(self, file, validator):
        pass

    def save(self, file, data):
        pass


class FileWriter(FileProduct):
    def load(self, file, validator):
        contents = []
        try:
            the_file = open(file, 'r')
        except FileNotFoundError:
            print("file does not exist.")
        else:
            for line in the_file:
                line = tuple(line.replace('\n', "").split(','))
                contents.append(line)
            the_file.close()
            contents = validator.start(contents)
            return contents


class FileSaver(FileProduct):
    def save(self, file, data):
        the_file = open(file, 'w')
        string = ""
        for l in data:
            new_data = [l[0], l[1], l[2], l[3], l[4], l[5], l[6]]
            for i in range(len(new_data)):
                string += str(new_data[i])
                # prevent a space at the end of a line
                if i != len(new_data) - 1:
                    string += ','

            string += "\n"
        the_file.write(string)
        the_file.close()


# Kris Little design
class FileHandler(IFileHandler):
    def __init__(self):
        self.valid = True
        self.validator = data_validator.DataValidator()
        self.fileSaver = self.build_file_operator("save")
        self.fileWriter = self.build_file_operator("write")

    def build_file_operator(self, arg):
        if arg == "save":
            return FileSaver()
        elif arg == "write":
            return FileWriter()

    # Kris
    def load_file(self, file):
        # put error handling here
        contents = self.fileWriter.load(file, self.validator)
        return contents

    # Kris
    def write_file(self, file, data):
        self.fileSaver.save(file, data)

    # Brendan Holt
    # Used to pickle the loaded graphs to default pickle file
    def pack_pickle(self, graphs):
        # Raises exception if the default file does not exits and creates it should this exception be raised
        try:
            realfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\pickle.dat"
            if not os.path.exists(realfilepath):
                raise IOError
        except IOError:
            os.makedirs(os.path.dirname(realfilepath))
            pass
        # The pickle process
        pickleout = open(realfilepath, "wb")
        pickle.dump(graphs, pickleout)
        pickleout.close()

    # Brendan Holt
    # Used to unpickle graphs in the pickle file and return them to the interpreters graph list
    def unpack_pickle(self, filepath):
        # Raises exception if for some reason the default file has been deleted
        try:
            if os.path.exists(filepath) is False:
                raise IOError
        except IOError:
            print('File does not exits')
            return
        # The unpickle process
        picklein = open(filepath, "rb")
        graphs = pickle.load(picklein)
        picklein.close()
        # Return the graphs to the interpreter
        return graphs

    # Brendan Holt
    # Used to pickle the entire database to default pickle file
    def pickle_all(self, data):
        # Raises exception if for some reason the default file has been deleted
        try:
            realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
            if os.path.exists(realfiledirectory) is False:
                raise IOError
        except IOError:
            os.makedirs(os.path.dirname(realfiledirectory))
            return
        # The pickle process
        pickleout = open(realfiledirectory + "\\db_backup.dat", "wb")
        pickle.dump(data, pickleout)
        pickleout.close()
