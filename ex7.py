def studList():
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    for name in studentNames:
        print(f"{name} Evans")


def addToList():
    new_name = input("请输入一个新的名字添加到列表中: ")
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    studentNames.append(new_name)
    for name in studentNames:
        print(f"{name} Evans")


if __name__ == "__main__":
    print("原始列表:")
    studList()
    print("\n添加新名字后的列表:")
    addToList()    
