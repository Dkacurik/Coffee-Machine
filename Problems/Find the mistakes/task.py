class MyClass:
    n_objects = 0

    def __new__(cls, *args, **kwargs):
        if (cls.n_objects < 5):
            cls.n_objects += 1
            return cls.n_objects

    def __str__(self):
        return "An Object of MyClass"
