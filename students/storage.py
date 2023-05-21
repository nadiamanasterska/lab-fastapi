from functools import lru_cache

student_list = []

@lru_cache()
def get_student_list():
    return student_list
