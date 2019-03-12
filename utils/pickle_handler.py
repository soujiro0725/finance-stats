import pickle

def save_dict(obj, name ):
    with open('data/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_dict(name ):
    with open('data/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)