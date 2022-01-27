import orjson 
import json
import numpy as np



def dic2json(path,dic):
    """
    Saving a Dictionary as json, using orjson to serialize Numpy

    Parameters:
    ---------------
    path : string
        A string containing the path to the saving location

    dic : dict
        Dictionary that is to be saved as a json

    """
    with open(path,"wb") as file:
        s = orjson.dumps(dic,option=orjson.OPT_SERIALIZE_NUMPY)
        file.write(s)


def json2dic(path,numpy_unpack=True):
    """
    Loading a json into a dictionary

    Parameters
    ----------------

    path : string
        A string containing the location of the json file

    numpy_unpack : bool
        Option to unpack the json into a dictionary containing numpy arrays

    Returns
    ---------------

    dic : dict
        A dictionary containing the json files 
    """

    with open(path,"r") as file:

        dic = json.load(file)

        if numpy_unpack == True:

            dic = __numpydic(dic)

    return dic

def __numpydic(dic):
    """
    Turn the lists in the array into numpy array
    """
    workdic = dic
    for key in dic.keys():
        
        if isinstance(dic[key], dict):
            workdic[key] = __numpydic(dic[key])
            
        if isinstance(dic[key],list):
            
            workdic[key] = np.array(dic[key])
            
        else:
            workdic[key] = dic[key]

    return workdic
