from inspect import signature

def type_safe(func):
    """
    Wrapper function to force a function to be type safe
    """
    def force_safety(*args, **kwargs):
        flag = True
        classCheck = False
        for argType in [args, kwargs.values()]:
            for index in range(0, len(argType)):
                arg = argType[index]

                try:
                    reqType = list(func.__annotations__.values())[index]
                except IndexError:
                    reqType = list(func.__annotations__.values())[index - 1]

                # skip self if in class
                if func.__qualname__ and not classCheck:
                    classCheck = True
                    continue

                if type(arg) == reqType or reqType == object:
                    continue
                else:
                    flag = False
                    raise Exception(f"argument {arg} is not type of {reqType}")
                    break

        if flag:
            return func(*args, **kwargs)

    return force_safety

safe = type_safe