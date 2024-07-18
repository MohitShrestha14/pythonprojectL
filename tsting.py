def person_detail(name_, age_, gender_):

    conditions = {
        'male': 'you are male',
        'female': 'you are female'
    }

    if age > 18:
        if gender_ == "male":
            print(f"Hello, {name_}, {gender_} and age is {age_} so you are "
              f"eligible for vote.{conditions.get(gender_)}")
        else:
            print(f"Hello, {name_}, {gender_} and age is {age_} so you are "
                  f"eligible for vote.{conditions[gender_]}")

    else:
        print(f"Hello, {name_}, {gender_} and age is {age_} so you are "
              f"not eligible for vote.")


if __name__ == "__main__":
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    person_detail(gender_=gender, name_=name, age_=age)
