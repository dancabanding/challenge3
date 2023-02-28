def get_value_from_nested_object(obj, key):
    keys = key.split("/")
    for k in keys:
        obj = obj.get(k)
        if obj is None:
            return None
    return obj

obj1 = {"a":{"b":{"c":"d"}}}
key1 = "a/b/c"
value1 = get_value_from_nested_object(obj1, key1)
print(value1) 

obj2 = {"x":{"y":{"z":"a"}}}
key2 = "x/y/z"
value2 = get_value_from_nested_object(obj2, key2)
print(value2)  
