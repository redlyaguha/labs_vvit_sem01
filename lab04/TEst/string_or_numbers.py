def True_False(x,y):
    try:
        float(x)
        float(y)
        return True
    except ValueError:
        return exit()