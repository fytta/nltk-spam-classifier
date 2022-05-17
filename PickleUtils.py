import pickle

class PickleUtils:

    def save(path, filename, data):
        fullpath = path+'/'+filename+'.pickle'
        f = open(fullpath, 'wb')
        pickle.dump(data, f, -1)
        f.close()
        print('File ', fullpath, ' saved')
        

    def load(path, filename):
        fullpath = path+'/'+filename+'.pickle'
        f = open(fullpath, 'rb')
        data = pickle.load(f)
        f.close()
        return data